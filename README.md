# CoffeaHZZAnalysis

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/stormsomething/CoffeaHZZAnalysis/HEAD?filepath=CoffeaHZZAnalysis.ipynb)

Based on https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata/blob/master/13-TeV-examples/uproot_python/HZZAnalysis.ipynb.

Also makes use of code from https://github.com/alexander-held/PyHEP-2021-cabinetry and https://github.com/gordonwatts/pyhep-2021-SX-OpenDataDemo.

## Runtime Comparisons:

* Original (data from https): 16 minutes

* Original (data stored locally): 33 seconds

* Coffea Processor (data from https): 46 seconds (161 seconds on Binder)

* Coffea Processor (data stored locally): 6 seconds

* Coffea Processor (data from ServiceX, uncached): 33 seconds

* Coffea Processor (data from ServiceX, cached): 2 seconds

* Cabinetry with Uproot Backend (data stored locally): 4 seconds (also 4 seconds on coffea-casa)

* Cabinetry with Coffea Backend (data stored locally): 10 seconds

---

* Coffea Processor (with list comprehension): ~20 minutes

* Coffea Processor (with cuts vectorized): ~11 minutes

* Coffea Processor (with all vectorized functions except calc_weight): ~2 minutes

* Coffea Processor (with all vectorized functions): ~3 seconds

* Coffea Processor (using hist package instead of coffea.hist): ~4 seconds

---

Cut order and method does not seem to significantly affect runtime.

* Cut on Charge, then Type: 5.0 seconds

* Cut on Type, then Charge: 5.3 seconds

* Cut on Charge and Type Simultaneously with Boolean Operators: 4.8 seconds

* Cut on Charge and Type Simultaneously with a Single Function: 5.2 seconds

* Cut on Charge, then Type Directly in Processor without a Function: 4.6 seconds

## Discovery Significance Comparisons:

Bin Width is 5 GeV except where stated otherwise.

Bounds are 80-250 GeV except where stated otherwise.

* Original Bins

  * Observed Significance: 2.345

  * Expected Significance: 1.301

* Bin Width: 10 GeV

  * Observed Significance: 2.090

  * Expected Significance: 1.253

* Bin Width: 2 GeV

  * Observed Significance: 1.887

  * Expected Significance: 1.509

* Bin Width: 17 GeV

  * Observed Significance: 1.303

  * Expected Significance: 0.996

* Bin Width: 1 GeV

  * Observed Significance: 2.674

  * Expected Significance: 1.688

* Bin Width: 34 GeV

  * Observed Significance: 0.013

  * Expected Significance: 0.481

* Bin Width: 1 GeV between 110 GeV and 140 GeV and 10 GeV elsewhere

  * Observed Significance: 2.244

  * Expected Significance: 1.624

* Bin Width: 10 GeV between 110 GeV and 140 GeV and 1 GeV elsewhere

  * Observed Significance: 2.676

  * Expected Significance: 1.344

* Bin Width: 30 GeV between 110 GeV and 140 GeV and 1 GeV elsewhere

  * Observed Significance: 1.429

  * Expected Significance: 0.743

* Bounds: 110-140 GeV 

  * Observed Significance: 2.743

  * Expected Significance: 1.044

* Bounds: 95-195 GeV 

  * Observed Significance: 2.223

  * Expected Significance: 1.253

* Bounds: 30-300 GeV 

  * Observed Significance: 2.112

  * Expected Significance: 1.282

* Bin Width: 1 GeV, Bounds: 110-140 GeV 

  * Observed Significance: 2.044

  * Expected Significance: 1.335

* Bin Width: 10 GeV, Bounds: 110-140 GeV 

  * Observed Significance: 2.476

  * Expected Significance: 1.020
