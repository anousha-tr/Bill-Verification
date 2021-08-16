import pandas as pd
from datetime import datetime
from datetime import timedelta

timerange = pd.date_range('2019', periods = 3, freq = 'Y')
index = pd.MultiIndex.from_product([[2019, 2020, 2021], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])

ADJUSTMENT_FACTOR = pd.Series([1.0272, 1.0272, 1.0192], index = timerange)

METERING_FACTOR = pd.Series([0.99, 0.99, 0.99], index = timerange)
GA = pd.Series([1, 1, 1, 0.06358, 0.06358, 0.08991, 0.08991, 0.05628, 0.05628, 0.11513, 0.11513, 0.10727, 0.08323, 0.12451, 0.10432, 0.13707, 0.09293, 0.115, 0.10305, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], index = index)

PDF = pd.Series([5.666e-05, 5.666e-05, 5.666e-05, 5.666e-05, 5.666e-05, 5.666e-05,\
      6.327e-05, 6.327e-05, 6.327e-05, 6.327e-05, 6.327e-05, 6.327e-05, \
      6.327e-05, 6.327e-05, 6.327e-05, 6.327e-05, 6.327e-05,6.327e-05, \
      5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, \
      5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, \
      5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05, 5.166e-05], index = index)

CUSTOMER_CHARGE = pd.Series([1007.33, 1007.33, 968.50], index = timerange)

ADMIN_CHARGE = pd.Series([0.25, 0.25, 0.25], index = timerange)

CAPACITY_CHARGE = pd.Series([0.0004, 0.00032, 0.00032], index = timerange)


DISTRIBUTION_CHARGE = pd.Series([6.602, 6.8, 6.8], index = timerange)

TRANSFORMER_ALLOWANCE = pd.Series([0.62, 0.62, 0.62], index = timerange)

TRANSMISSION_NETWORK_CHARGE = pd.Series(pd.Series([2.5677, 2.8833, 2.6113], index = timerange))

TRANSMISSION_CONNECTION_CHARGE = pd.Series([2.303, 2.3797, 2.1371], index = timerange)

WHOLE_MARKET_SERVICE_CHARGE = pd.Series([0.0035, 0.0035, 0.0035], index = timerange)

TAX = 1.13

HOEP = pd.Series([0.02798, 0.02811, 0.02712, 0.01536, 0.00738, 0.0051, 0.02163, \
    0.01641, 0.01507, 0.00824, 0.02182, 0.02209, 0.01536, 0.01517, 0.01413, 0.00591, \
    0.00837, 0.01251, 0.02031, 0.01913, 0.0146, 0.01136, 0.01063, 0.01569, 0.0173, \
    0.03319, 0.01705, 0.00893, 0.01484, 0, 0, 0, 0, 0, 0, 0], index = index)

POWER_FACTOR = pd.Series([0.9924, 0.975, 0.992, 0.958, 0.963, 0.957, 0.957, 0.955, 0.955, \
    0.952, 0.992, 0.992 ,0.992, 0.975, 0.992, 0.958, 0.963, 0.957, 0.957, 0.955, 0.955, \
    0.955, 0.955, 0.955,0,0,0,0,0,0,0,0,0,0,0,0], index = index)

