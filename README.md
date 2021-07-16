# CoffeaHZZAnalysis

Based on https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata/blob/master/13-TeV-examples/uproot_python/HZZAnalysis.ipynb.

Runtime Comparisons:

-Original (data from https): ~15 minutes

-Original (data stored locally): ~1 minute

--

-Coffea Processor (with list comprehension): ~20 minutes

-Coffea Processor (with cuts vectorized): ~11 minutes

-Coffea Processor (with all vectorized functions except calc_weight): ~2 minutes

-Coffea Processor (with all vectorized functions): ~3 seconds

-Coffea Processor (using hist package instead of coffea.hist): ~4 seconds

--

Cut order and method does not seem to significantly affect runtime.

-Cut on Charge, then Type: 2.7-3.9 seconds

-Cut on Type, then Charge: 3.1-3.9 seconds

-Cut on Charge and Type Simultaneously with Boolean Operators: 3.1-3.3 seconds

-Cut on Charge and Type Simultaneously with a Single Function: 2.7-3.3 seconds

-Cut on Charge, then Type Directly in Processor without a Function: 2.7-3.6 seconds

--

-Cabinetry: ~7 seconds
