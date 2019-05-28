import json
import pandas as pd
from datetime import datetime

class CDP:

    slippage = .01
    MIN_RATIO = 3.0/2.0
    filename = 'data/simulations/cdp.json'

    def __init__(self, price):
        try:
            with open(self.filename, 'r') as f:
                cdp = json.load(f)
                for key, val in cdp.items():
                    setattr(self, key, val)
        except:
            self.start_price = price
            self.price = price
            self.usd_on_hand = 0
            self.eth_on_hand = 0
            self.eth_deposited = 0
            self.usd_generated = 0
            self.actions = []
            self.trades = []

    def _add_action(self, action, quantity, date=None):
        if date is None:
            date = datetime.now()
        self.actions.append({
            'date': datetime.timestamp(date),
            'action': action,
            'quantity': quantity,
        })
        self._update_calculations()

    def _update_calculations(self):
        self.liquidation_price = self.usd_generated * self.MIN_RATIO / self.eth_deposited
        self.usd_value = self.price * self.eth_deposited
        self.usd_available_to_generate = self.usd_value / self.MIN_RATIO - self.usd_generated

    def releverage(self, usd, date=None, price=None):
        self.generate(usd)
        eth = self.trade(side='BUY', usd=usd, date=date, price=price)
        self.deposit(eth=eth)

    def deposit(self, eth, ignore=False, date=None):
        if ignore is False:
            self.eth_on_hand -= eth
        self.eth_deposited += eth
        self._add_action(action='deposit', quantity=eth, date=date)

    def withdraw(self, eth, date=None):
        self.eth_deposited -= eth
        self.eth_on_hand += eth
        self._add_action(action='withdraw', quantity=eth, date=date)

    def payback(self, usd, date=None):
        self.usd_generated -= usd
        self.usd_on_hand -= usd
        self._add_action(action='payback', quantity=usd, date=date)

    def generate(self, usd, date=None):
        self.usd_generated += usd
        self.usd_on_hand += usd
        self._add_action(action='generate', quantity=usd, date=date)

    def trade(self, side, date=None, usd=None, price=None, eth=None):
        if price is None:
            price = self.price
        if date is None:
            date = datetime.now()
        # TODO: do we need a 'side' variable if usd or eth is None?
        if usd is None:
            usd = price*eth * (1.0 - self.slippage)
        elif eth is None:
            eth = usd/price * (1.0 - self.slippage)
        if side == 'BUY':
            self.eth_on_hand += eth
            self.usd_on_hand -= usd
        else: # side == 'SELL'
            self.eth_on_hand -= eth
            self.usd_on_hand += usd
        self.trades.append({
            'date': datetime.timestamp(date),
            'side': side,
            'usd': usd,
            'price': price,
            'eth': eth
        })
        self._update_calculations()
        return eth

    def update_price(self, price):
        self.price = price
        self._update_calculations()

    # NOTE: this is still saved as close() in loan/personal cdp
    def summarize(self, price=None):
        if price is None:
            price = self.price
        self.eth_owed = self.usd_generated / price
        self.end_eth = self.eth_deposited - self.eth_owed
        self.pct_change_eth_price = (price - self.start_price) / self.start_price
        # self.pct_change_eth_balance = (self.end_eth - self.start_eth_on_hand) / self.start_eth_on_hand
        with open(self.filename, 'w') as outfile:
            json.dump(self.__dict__, outfile)
