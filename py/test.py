import math
import numpy as np
import pandas as pd
from datetime import datetime
from cdp import CDP


START_AMT = 5000
prices = pd.read_csv('../data/prices.csv')
prices.iloc[0]

eth = START_AMT/prices['Close'][0]

cdp.deposit(eth)
