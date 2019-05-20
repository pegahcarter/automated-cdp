import pandas as pd
import matplotlib.pyplot as plt

# Withdrawal 1: $33.333...
# Withdrawal 2: $27.777...

# log_list = []
# val = 0
# for i in range(900):
#     val += (1.0/2.0)**i
#     log_list.append(val)

df = pd.read_csv('data/simulations/basic_comparison.csv')
df.set_index('Price', inplace=True)
fig, ax = plt.subplots(figsize=(5,5))
plt.plot(df['CDP-1'], color='red')
plt.plot(df['CDP-2'], color='blue')
plt.plot(df['CDP-3'], color='green')
plt.legend()

# Basic summary of every 150 data points
pd.DataFrame([df.iloc[i] for i in df.index if (i+1) % 150 == 0])

df_pct = pd.DataFrame()
df_pct['CDP-1'] = (df['CDP-1'] - df.index) / df.index
df_pct['CDP-2'] = (df['CDP-2'] - df.index) / df.index

plt.plot(df_pct['CDP-1'], color='red')
plt.plot(df_pct['CDP-2'], color='blue')
plt.legend()

df_pct['CDP-1'].iat[899]
df_pct['CDP-2'].iat[899]
