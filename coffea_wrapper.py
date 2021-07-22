import pathlib
from typing import List, Optional, Tuple

import coffea.hist
from coffea.nanoevents.methods.base import NanoEventsArray
import coffea.processor
import numpy as np
import awkward as ak


default_functions = {
    "abs": np.absolute,
    "absolute": np.absolute,
    "acos": np.arccos,
    "arccos": np.arccos,
    "acosh": np.arccosh,
    "arccosh": np.arccosh,
    "asin": np.arcsin,
    "arcsin": np.arcsin,
    "asinh": np.arcsinh,
    "arcsinh": np.arcsinh,
    "atan": np.arctan,
    "atan2": np.arctan2,
    "arctan": np.arctan,
    "arctan2": np.arctan2,
    "atanh": np.arctanh,
    "arctanh": np.arctanh,
    "cbrt": np.cbrt,
    "ceil": np.ceil,
    "conj": np.conjugate,
    "conjugate": np.conjugate,
    "copysign": np.copysign,
    "cos": np.cos,
    "cosh": np.cosh,
    "exp": np.exp,
    "exp2": np.exp2,
    "expm1": np.expm1,
    "fabs": np.fabs,
    "floor": np.floor,
    "fmax": np.fmax,
    "fmin": np.fmin,
    "hypot": np.hypot,
    "imag": np.imag,
    "isfinite": np.isfinite,
    "isinf": np.isinf,
    "isnan": np.isnan,
    "log": np.log,
    "log10": np.log10,
    "log1p": np.log1p,
    "log2": np.log2,
    "logical_and": np.logical_and,
    "logical_or": np.logical_or,
    "neg": np.negative,
    "nextafter": np.nextafter,
    "real": np.real,
    "rint": np.rint,
    "round": np.round,
    "signbit": np.signbit,
    "sin": np.sin,
    "sinh": np.sinh,
    "sqrt": np.sqrt,
    "tan": np.tan,
    "tanh": np.tanh,
    "trunc": np.trunc,
    "where": np.where,
}


class SingleHistProcessor(coffea.processor.ProcessorABC):

    def __init__(self, channel_info: List[dict], template_info: dict) -> None:
        if channel_info is None or template_info is None:
            raise ValueError

        # set up accumulator from histogram info
        # channels are in dict and not an axis, since binning per channel can vary
        # accumulator structure:
        # - dict with channels as keys
        #   - axis with sample/dataset name
        # TODO: consider always using "observable" as first arg of hist.Bin to allow
        #       hard-coding it in process() and avoid **{}
        #       - observable name still preserved in second argument (label)
        self._accumulator = coffea.processor.dict_accumulator()
        for ch in channel_info:
            self._accumulator.update(
                {
                    ch["name"]: coffea.hist.Hist(
                        "events",
                        coffea.hist.Cat("dataset", "dataset"),
                        coffea.hist.Cat("template", "systematic template"),
                        coffea.hist.Bin(
                            ch["variable"], ch["observable_label"], ch["binning"]
                        ),
                    )
                }
            )
        self.channel_info = channel_info
        self.template_info = template_info

    @property
    def accumulator(self) -> coffea.processor.dict_accumulator:
        return self._accumulator

    def process(self, events: NanoEventsArray) -> coffea.processor.dict_accumulator:
        out = self.accumulator.identity()

        # dataset from metadata
        dataset = events.metadata["dataset"]

        # loop over channels
        for ch in self.channel_info:
            # get relevant info for building histogram from metadata
            channel_name = ch["name"]
            variable = ch["variable"]

            # loop over templates
            for template in self.template_info[dataset]:
                template_name = template["name"]
                selection_filter = template["selection_filter"]

                # apply cuts
                # TODO: could also use numexpr.evaluate
                events_records = dict(zip(ak.fields(events), ak.unzip(events)))
                events_namespace = {**events_records, **default_functions}
                events_cut = events[eval(selection_filter, events_namespace)]

                events_cut_records = dict(zip(ak.fields(events_cut), ak.unzip(events_cut)))
                events_cut_namespace = {**events_cut_records, **default_functions}
                observables = eval(variable, events_cut_namespace)

                if template["weight"] is not None:
                    # weights are sample property
                    weight_expression = template["weight"]
                    weights = eval(weight_expression, events_cut_namespace)
                else:
                    weights = np.ones(len(observables))

                # need **{} to pass observable, since name is not hardcoded (while
                # "dataset" is hardcoded in constructor)
                out[channel_name].fill(
                    dataset=dataset,
                    template=template_name,
                    weight=weights,
                    **{variable: observables},
                )
        return out

    def postprocess(
        self, accumulator: coffea.processor.dict_accumulator
    ) -> coffea.processor.dict_accumulator:
        return accumulator


def build_single_histogram(
    ntuple_paths: List[pathlib.Path],
    pos_in_file: str,
    variable: str,
    bins: np.ndarray,
    weight: Optional[str] = None,
    selection_filter: Optional[str] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    # sample can have generic name, not needed here
    # need to convert list of paths to list of strings
    samples = {
        "generic_name": {
            "treename": pos_in_file,
            "files": [str(p) for p in ntuple_paths],
        }
    }

    # template: one at a time, template name not needed
    template_info = {
        "generic_name": [
            {
                "name": "generic_template_name",
                "weight": weight,
                "selection_filter": selection_filter,
            }
        ]
    }

    # channel info: more generic info that is not needed here
    channel_info = [
        {
            "name": "generic_channel_name",
            "variable": variable,
            "observable_label": "generic_label",  # for cosmetics
            "binning": bins,
        }
    ]

    result = coffea.processor.run_uproot_job(
        samples,  # "fileset"
        None,  # tree name is specified in fileset
        SingleHistProcessor(channel_info, template_info),
        coffea.processor.iterative_executor,
        {"schema": coffea.nanoevents.BaseSchema},
    )

    yields, variance = result["generic_channel_name"].values(sumw2=True)[
        ("generic_name", "generic_template_name")
    ]
    return yields, np.sqrt(variance)
