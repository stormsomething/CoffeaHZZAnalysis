# CoffeaHZZAnalysis

Based on https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata/blob/master/13-TeV-examples/uproot_python/HZZAnalysis.ipynb.

To Address:

-Want to use hist for histograms rather than coffea.hist

-The statistical uncertainties don't seem to line up exactly with what we have in the original analysis.

Runtime Comparisons:

-Original (data from https): ~15 minutes

-Original (data stored locally): ~1 minute

-Coffea Processor (with list comprehension): ~20 minutes

-Coffea Processor (with cuts vectorized): ~11 minutes

-Coffea Processor (with all vectorized functions except calc_weight): ~2 minutes

-Coffea Processor (with all vectorized functions): ~3 seconds
