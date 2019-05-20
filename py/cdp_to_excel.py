'''
Brainstorming to document CDP actions to CSV

Columns
    - Date
    - Action
    - ETH_USD
    - Quantity

How do we account for tx fees?

Is there a way to apply _update_calculations() to formulas without constantly
calling it?
'''


class CDP:

    def __init__(self, price):
        self.start_price = price
        self.price = price
        self.eth_on_hand = 0
        self.eth_deposited = 0
        self.usd_generated = 0
        self.usd_value = 0
        self.usd_available_to_generate = 0
        self.liquidation_price = 0

    def _update_calculations(self):
        # self.liquidation_price = self.usd_generated * self.MIN_RATIO / self.eth_deposited
        self.usd_value = self.price * self.eth_deposited
        self.usd_available_to_generate = self.usd_value / self.MIN_RATIO - self.usd_generated

    def deposit_eth(self, eth):
        self.eth_deposited += eth
        # self.eth_on_hand -= eth
        self._update_calculations()

    def transfer_usd(self, usd):
        self.usd_transferred_to_carter += usd
        self.usd_on_hand -= usd
        self._update_calculations()

    def generate_usd(self, usd):
        self.usd_generated += usd
        self.usd_on_hand += usd
        self._update_calculations()

    def trade_usd_for_eth(self, usd, price):
        self.eth_on_hand += usd/price
        self.usd_on_hand -= usd
        self._update_calculations()

    def update_eth_price(self, price):
        self.price = price
        self._update_calculations()
