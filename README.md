# CoffeaHZZAnalysis

Based on https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata/blob/master/13-TeV-examples/uproot_python/HZZAnalysis.ipynb.

I don't want to have the processor use list comprehensions, but the other ways that I have tried haven't worked.

Runtime Comparisons:
-Original (data from https): ~15 minutes
-Original (data stored locally): ~1 minute
-Coffea Processor (with list comprehension): ~20 minutes
-Coffea Processor (with vectorized functions):
