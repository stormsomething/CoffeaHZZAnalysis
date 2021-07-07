# CoffeaHZZAnalysis

Based on https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata/blob/master/13-TeV-examples/uproot_python/HZZAnalysis.ipynb.

To Address:

-Overlay dataset labels are missing

-Error bars for the Monte Carlo datasets are missing

Runtime Comparisons:

-Original (data from https): ~15 minutes

-Original (data stored locally): ~1 minute

-Coffea Processor (with list comprehension): ~20 minutes

-Coffea Processor (with cuts vectorized): ~11 minutes

-Coffea Processor (with all vectorized functions except calc_weight): ~2 minutes

-Coffea Processor (with all vectorized functions): ~3 seconds

-Coffea Processor (using hist package instead of coffea.hist): ~3 seconds
