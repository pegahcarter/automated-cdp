import math
import numpy as np
import pandas as pd


class CDP(object):

    def __init__(self):
        self.deposited = 0
        self.liquidation_price = 0
        self.generated = 0
        self.fees = 0

    def deposit(self, eth):
        self.deposited += eth


    def withdraw(self, eth):
        if eth > self.deposited:
            return "Cannot withdraw more than the max."

        self.deposited -= eth

    def calc_liquidation_price(self):
        pass

    def generate(self, dai):

        if self.liquidation_price > current_price:
            return "DAI generation would liquidate account.  Stopping early."

        pass
