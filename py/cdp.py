
import os
import numpy as np
import pandas as pd

START_AMT = 5000

prices = pd.read_csv('../data/prices.csv')











class CDP(object):

    def __init__(self):
        self.deposited = START_AMT
        self.liquidation_price = 0
        self.generated = 0

        pass



prices.head()
