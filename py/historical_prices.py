import os
import sys
import json
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

''' January 2017 - December 2018  '''

# TODO: Update CSV first

TICKER = 'ETH/USDT'
OLD_FILE = '../data/eth_since_2017.json'
NEW_FILE = '../data/eth_since_2017_new.json'

COLUMNS = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']

# NOTE: does this save as list or numpy array?
old_data = np.array(pd.read_json(OLD_FILE)).tolist()


new_data = []

for row in old_data:
    new_data.append(dict(zip(COLUMNS, rows)))

# Convert dictionaries to right datatype
# string to parse date- remember to update CSV
'%b %d, %Y'



with open(NEW_FILE, 'w') as outfile:
    json.dump(new_data, outfile)
