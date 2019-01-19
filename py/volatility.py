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
df['+ Pct'] = (df['High'] - df['Open']) / df['Open']
df['- Pct'] = (df['Open'] - df['Low']) / df['Open']
df['+- Pct'] = df['+ Pct'] + df['- Pct']


print(df['+- Pct'].std())
print(df.head())
