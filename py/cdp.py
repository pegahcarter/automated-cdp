import json
from datetime import datetime
from pathlib import Path


class CDP:

    MIN_RATIO = 3.0/2.0

    def __init__(self, price, preload=False, eth_deposited=0.01, usd_generated=1, start_eth_on_hand=0):
        if preload and Path('cdp.json').exists():
            with open(self.filename, 'r') as f:
                cdp = json.load(f)
            for key, val in cdp.items():
                setattr(self, key, val)
        else:
            self.actions = []
            self.trades = []
            self.summary = {}
            self.summary['eth_on_hand'] = start_eth_on_hand
            self.summary['usd_on_hand'] = 0
            self.summary['eth_deposited'] = eth_deposited
            self.summary['usd_generated'] = usd_generated
            self.price = price
            self.start_price = price
            self.start_eth_on_hand = start_eth_on_hand
        self._update_calculations()

    def _add_action(self, action, eth_usd, quantity, date=None):
        if date is None:
            date = datetime.now()
        self.actions.append({
            'id': len(self.actions) + 1,
            'date': datetime.timestamp(date),
            'action': action,
            'eth-usd': eth_usd,
            'quantity': quantity
        })
        self._update_calculations()

    def _update_calculations(self, *args):
        self.summary['liquidation_price'] = self.summary['usd_generated'] * self.MIN_RATIO / self.summary['eth_deposited']
        self.summary['usd_value'] = self.price * self.summary['eth_deposited']
        self.summary['usd_available_to_generate'] = self.summary['usd_value'] / self.MIN_RATIO - self.summary['usd_generated']
        self.summary['eth_available_to_withdraw'] = self.summary['usd_available_to_generate'] / self.price
        if args:
            return args

    def update_price(self, price):
        self.price = price
        self._update_calculations()

    def deposit(self, eth, ignore=False, date=None):
        if ignore is False:
            self.summary['eth_on_hand'] -= eth
        self.summary['eth_deposited'] += eth
        self._add_action(action='deposit', eth_usd='ETH', quantity=eth, date=date)

    def withdraw(self, eth, date=None):
        self.summary['eth_deposited'] -= eth
        self.summary['eth_on_hand'] += eth
        self._add_action(action='withdraw', eth_usd='ETH', quantity=eth, date=date)

    # TODO: add fee calculation
    def payback(self, usd, date=None):
        self.summary['usd_generated'] -= usd
        self.summary['usd_on_hand'] -= usd
        self._add_action(action='payback', eth_usd='USD', quantity=usd, date=date)

    def generate(self, usd, date=None):
        self.summary['usd_generated'] += usd
        self.summary['usd_on_hand'] += usd
        self._add_action(action='generate', eth_usd='USD', quantity=usd, date=date)

    def trade(self, side, usd=None, eth=None, price=None, date=None):
        if price is None:
            price = self.price

        if date is None:
            date = datetime.now()

        if usd is None:
            usd = price * eth
        elif eth is None:
            eth = usd / price

        if side == 'BUY':
            self.summary['eth_on_hand'] += eth
            self.summary['usd_on_hand'] -= usd
        else: # side == 'SELL'
            self.summary['eth_on_hand'] -= eth
            self.summary['usd_on_hand'] += usd

        self.trades.append({
            'id': len(self.trades) + 1,
            'date': datetime.timestamp(date),
            'side': side,
            'usd': usd,
            'price': price,
            'eth': eth
        })
        self._update_calculations(eth)
        # return eth

    def summarize(self, price=None, save=False):
        if price:
            self.update_price(price)

        self.summary['eth_owed'] = self.summary['usd_generated'] / self.price
        self.summary['end_eth'] = self.summary['eth_deposited'] - self.summary['eth_owed']
        self.summary['pct_change_eth_price'] = (self.price - self.start_price) / self.start_price
        # self.pct_change_eth_balance = (self.summary['end_eth'] - self.start_eth_on_hand) / self.start_eth_on_hand
        if save is True:
            with open('cdp.json', 'w') as outfile:
                json.dump(self.__dict__, outfile)

        return self.summary['end_eth']
