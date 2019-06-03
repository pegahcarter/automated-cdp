from py.cdp import CDP
import ccxt
from datetime import datetime, timedelta
import numpy as np

cdp = CDP(preload=True)
exchange = ccxt.bitmex()

start_eth = cdp['actions'][0]['quantity']
start_date = datetime.fromtimestamp(cdp['actions'][0]['date'])
end_date = datetime.now()
dates, prices = [], []

while start_date < end_date:
    start_date += timedelta(hours=1)
    candles = np.array(exchange.fetch_ohlcv('ETH/USD', '1h', since=start_date.timestamp()*1000, limit=500))
    # Only save the timestamp and close price
    dates += candles[:, 0]/1000
    prices += candles[:, 4]
    start_date += timedelta(hours=len(candles))

cdp_sim = CDP()
results = []
for hour, price in zip(dates, prices):
    if hour > cdp.actions[0]['date']:
        # add action
        data = cdp.actions.pop(0)
        _, date, action, _, quantity = data
        getattr(cdp_sim, data['action'])(data['quantity'], data['date'])

    cdp_sim.summarize(price)
    results.append({
        'date': date,
        'Non-CDP $ Value': price*start_eth,
        'CDP $ Value': cdp_sim['summary']['usd_value']
    })
