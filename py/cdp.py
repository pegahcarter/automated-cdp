class CDP(object):

    MIN_RATIO = 3.0/2.0

    def __init__(self, eth_on_hand=100, price=150):
        self.usd_on_hand = 0
        self.usd_generated = 1
        self.eth_deposited = 0.01

        self.start_eth_on_hand = eth_on_hand - self.eth_deposited
        self.eth_on_hand = eth_on_hand - self.eth_deposited
        self.start_price = price
        self.price = price

        self._update_calculations()

    def _update_calculations(self):
        self.liquidation_price = self.usd_generated * self.MIN_RATIO / self.eth_deposited
        self.usd_value = self.price * self.eth_deposited
        self.usd_available_to_generate = self.usd_value / self.MIN_RATIO - self.usd_generated

        if amt > max_amt:
            return 'Invalid request. Unable to {} {}.'.format(action, eth_usd)

        self._update_calculations()

    def deposit_eth(self, eth):
        self.eth_deposited += amt
        self.eth_on_hand -= amt

    def transfer_usd(self, usd):
        self.usd_transferred_to_carter += amt
        self.usd_on_hand -= amt

    def generate_usd(self, usd):
        self.usd_generated += amt
        self.usd_on_hand += amt

    def trade_usd_for_eth(self, usd, price):
        self.eth_on_hand += amt/price
        self.usd_on_hand -= amt

    def update_eth_price(self, price):
        print('Update ETH price:  ${} => ${}'.format(round(self.price, 2), round(price,2)))
        self.price = price
        self._update_calculations()

    def close(self, price=None):
        if price is None:
            price = self.price
        eth_owed = self.usd_generated / price
        end_eth = self.eth_deposited - eth_owed
        pct_change_eth_price = (price - self.start_price) / self.start_price
        pct_change_eth_balance = (end_eth - self.start_eth_on_hand) / self.start_eth_on_hand

    def summarize(self):
        self._update_calculations()
        print('\n\n---------------------------')
        for key, val in self.__dict__.items():
            if val > 0 and key != 'i' and 'start' not in key:
                key = key.replace('usd', 'USD').replace('eth', 'ETH').replace('_', ' ')
                print(key + ': ', round(val, 2))
        print('---------------------------\n')
