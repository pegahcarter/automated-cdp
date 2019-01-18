'''
This file converts the messy JSON web scraped from coinmarketcap.com for 2 years
of ETH price data, and saves the correct data format to CSV and JSON.
'''

import os
import sys
import json
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

''' January 2017 - December 2018  '''

TICKER = 'ETH/USDT'
OLD_FILE = '../data/eth_since_2017.json'
NEW_FILE_JSON = '../data/prices.json'
NEW_FILE_CSV = '../data/prices.csv'
COLUMNS = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']

data = pd.read_json(OLD_FILE)
data.columns = COLUMNS

data['Date'] = [int(datetime.timestamp(datetime.strptime(day, '%b %d, %Y'))) for day in data['Date']]
for col in COLUMNS[1:]:
    data[col] = [float(num) for num in data[col]]

data.to_csv(NEW_FILE_CSV, index=False)

# Convert to better JSON file
new_data = [dict(data[COLUMNS].iloc[day]) for day in range(len(data))]
with open(NEW_FILE_JSON, 'w') as outfile:
    json.dump(new_data, outfile)
