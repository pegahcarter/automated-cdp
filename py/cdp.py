import math
import numpy as np
import pandas as pd
from position import Position

'''
1. Open CDP @ $100/ETH
2. Calculate position @ $200/ETH
    a. Make sure all CDP attributes are updated w/o any additional actions
    b. Criteria to trigger a re-lock
'''

cdp = CDP()
cdp.price
cdp.deposited
cdp.liq_price





# ------------------------------------------------------------------------------

prices = pd.read_csv('../data/prices.csv')['Close']
MAX_RATIO = 1.5
START_AMT = 5000

class CDP(object):

    def __init__(self):
        self.price = prices[0]
        self.deposited = START_AMT / prices[0]
        self.value = self.deposited * self.price
        self.generated = 2500
        self.ratio = self.value / self.generated
        self.liq_price = prices[0] * 0.66

    def refresh(self, )

    def calc_ratio(self, eth_price):
        return (eth_price * self.deposited) / self.generated

    def calc_liq_price(self, eth_price):
        return (self.generated * MAX_RATIO) / self.deposited

    def deposit(self, eth):
        self.deposited += eth
        # self.ratio = ???
        # self.liq_price = ???

    def withdraw(self, eth):
        if eth > self.deposited:
            return "Cannot withdraw more than the max."
        self.deposited -= eth
        # self.ratio = ???
        # self.liq_price = ???

    def generate(self, dai, eth_price):
        liquidation_price = calc_liquidation_price(dai)
        if liquidation_price > eth_price:
            return "DAI generation would liquidate account.  Stopping early."
        self.generated += dai
        # self.ratio = ???
        # self.liq_price = ???

    def calc_value(self, eth_price):
        return self.deposited * eth_price
