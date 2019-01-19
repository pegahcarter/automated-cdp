'''
This file is used to calculate daily volatility, EMA's, etc.
'''
import os
import sys
from datetime import datetime
import pandas as pd
import numpy as np


FILE = '../data/prices.csv'
df = pd.read_csv(FILE)
df.head()

data['Differences'] = data['High'] - data['Low']
