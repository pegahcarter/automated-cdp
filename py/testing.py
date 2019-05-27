# File to create initial CSV of CDP and actions
from py.cdp import CDP

cdp = CDP(price=100)
cdp.deposit(eth=1, ignore=True)

cdp.summarize()

file = pd.read_csv('data/simulations/actions.csv', index_col=0)
