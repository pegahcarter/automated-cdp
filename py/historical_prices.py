import os
import sys
import json
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

''' January 2017 - December 2018  '''

TICKER = 'ETH/USDT'
OLD_FILE = '../data/eth_since_2017.json'
NEW_FILE_JSON = '../data/data.json'
NEW_FILE_CSV = '../data/data.csv'
COLUMNS = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']

data = pd.read_json(OLD_FILE)
data.columns = COLUMNS

data['Date'] = [int(datetime.timestamp(datetime.strptime(day, '%b %d, %Y'))) for day in data['Date']]
for col in COLUMNS[1:]:
    data[col] = [float(num) for num in data[col]]

data.to_csv(NEW_FILE_CSV, index=False)





test = [dict(zip(COLUMNS, row)) for row in data.pivot]






# new_data = [dict(zip(COLUMNS, row)) for row in old_data]
epochs = [int(datetime.timestamp(datetime.strptime(day, '%b %d, %Y'))) for day in data['Date']]





































json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)
with open(NEW_FILE, 'w') as outfile:
    json.dump(new_data, outfile)
