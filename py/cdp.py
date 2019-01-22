import math
import numpy as np
import pandas as pd


class CDP(object):

    def __init__(self):
        START_AMT = 5000
        MAX_RATIO = 1.5
        self.prices = pd.read_csv('../data/prices.csv')['Close']
        self.deposited = START_AMT / self.prices[0]
        self.value = START_AMT
        self.generated = 2500
        self.ratio = 2.00
        self.liq_price = self.prices[0] * 0.75

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

    # def wipe(self, dai):
    #     pass
