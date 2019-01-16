import os
import sys
import ccxt
import time
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

''' January 2017 - December 2018  '''

exchange = ccxt.bittrex()


ticker = 'ETH/USDT'

start = datetime(2016, 12, 31, 18, 0)
end = datetime(2016, 12, 31, 18, 0)
datetime.timestamp(start)
datetime.timestamp(datetime(2016, 12, 31, 18, 0))

datetime.fromtimestamp(1483228800)

len(data)

datetime.fromtimestamp(data[0][0]/ 1000)
datetime.fromtimestamp(data[499][0]/ 1000)

datetime.fromtimestamp(1541417100)



file = '../data/eth_since_2017.json'

# data = np.array(pd.read_json(file))
old_data = np.array(pd.read_json(file)).tolist()

columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']

new_data = [{}]

for i, row in enumerate(old_data):
    new[data][a]
