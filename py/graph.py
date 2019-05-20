import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/simulations/basic_comparison.csv')

fig, ax = plt.subplots(figsize=(5,5))

plt.plot(df['Non-CDP'], color='black')
plt.plot(df['CDP-1'], color='red')
plt.plot(df['CDP-2'], color='blue')
plt.legend()
plt.show()

results = pd.DataFrame([df.iloc[i] for i in range(0, len(df), 150)])
results.index += 100
print(results)
