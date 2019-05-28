import json
from datetime import datetime

class CDP:

    MIN_RATIO = 3.0/2.0

    def __init__(self, price, start_eth_on_hand=0):
        try:
            with open(self.filename, 'r') as f:
                cdp = json.load(f)
                for key, val in cdp.items():
                    setattr(self, key, val)
        except:
            self.start_price = price
            self.start_eth_on_hand = start_eth_on_hand
            self.price = price
            self.eth_on_hand = start_eth_on_hand
            self.usd_on_hand = 0
            self.eth_deposited = 0
            self.usd_generated = 0
            self.actions = []
            self.trades = []

    def _add_action(self, action, eth_usd, quantity, date=None):
        if date is None:
            date = datetime.now()
        self.actions.append({
            'date': datetime.timestamp(date),
            'action': action,
            'eth-usd': eth_usd,
            'quantity': quantity
        })
        self._update_calculations()

    def _update_calculations(self):
        self.liquidation_price = self.usd_generated * self.MIN_RATIO / self.eth_deposited
        self.usd_value = self.price * self.eth_deposited
        self.usd_available_to_generate = self.usd_value / self.MIN_RATIO - self.usd_generated

    def update_price(self, price):
        self.price = price
        self._update_calculations()

    def deposit(self, eth, ignore=False, date=None):
        if ignore is False:
            self.eth_on_hand -= eth
        self.eth_deposited += eth
        self._add_action(action='deposit', eth_usd='ETH', quantity=eth, date=date)

    def withdraw(self, eth, date=None):
        self.eth_deposited -= eth
        self.eth_on_hand += eth
        self._add_action(action='withdraw', eth_usd='ETH', quantity=eth, date=date)

    # TODO: add fee calculation
    def payback(self, usd, date=None):
        self.usd_generated -= usd
        self.usd_on_hand -= usd
        self._add_action(action='payback', eth_usd='USD', quantity=usd, date=date)

    def generate(self, usd, date=None):
        self.usd_generated += usd
        self.usd_on_hand += usd
        self._add_action(action='generate', eth_usd='USD', quantity=usd, date=date)

    def trade(self, side, usd=None, price=None, eth=None, date=None):
        if price is None:
            price = self.price

        if date is None:
            date = datetime.now()

        if usd is None:
            usd = price * eth
        elif eth is None:
            eth = usd / price

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

    def summarize(self, price=None, save=False):
        if price is None:
            price = self.price
        else:
            self.update_price(price)

        self.eth_owed = self.usd_generated / price
        self.end_eth = self.eth_deposited - self.eth_owed
        self.pct_change_eth_price = (price - self.start_price) / self.start_price
        # self.pct_change_eth_balance = (self.end_eth - self.start_eth_on_hand) / self.start_eth_on_hand
        if save is True:
            with open('cdp.json', 'w') as outfile:
                json.dump(self.__dict__, outfile)
