import math
import numpy as np
import pandas as pd
from datetime import datetime
from cdp import CDP

cdp = CDP()

daily_price = cdp.prices[4]

cdp.value = cdp.calc_value(daily_price)
cdp.ratio = cdp.value / cdp.generated

cdp.deposited * daily_price * (2/1.74818)
