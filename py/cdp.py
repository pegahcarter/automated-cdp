from py.excel import Excel

class CDP:

    slippage = 1.01

    def __init__(self, price):
        self.start_price = price
        self.price = price
        self.usd_on_hand = 0
        self.eth_on_hand = 0
        self.eth_deposited = 0
        self.usd_generated = 0
        self.usd_value = 0
        self.usd_available_to_generate = 0
        self.liquidation_price = 0
        self.actions = []

    def add_action(self, action, eth_usd, quantity):
        actions.append({
            'Date': date,
            'Action': action,
            'ETH_USD': eth_usd,
            'quantity': quantity,
            'price': self.price
        })
        self._update_calculations()

    def _update_calculations(self):
        self.liquidation_price = self.usd_generated * self.MIN_RATIO / self.eth_deposited
        self.usd_value = self.price * self.eth_deposited
        self.usd_available_to_generate = self.usd_value / self.MIN_RATIO - self.usd_generated

    def releverage(self, usd, slippage=.01, price=None):
        self.generate_usd(usd)
        if price is None:
            price = self.price
        self.trade(usd, price, side)
        self.deposit_eth(eth_purchased)

    def deposit_eth(self, eth):
        self.eth_on_hand -= eth
        self.eth_deposited += eth
        self.add_action(action='deposit', eth_usd='ETH', quantity=eth)

    def withdraw_eth(self, eth):
        self.eth_deposited -= eth
        self.eth_on_hand += eth
        self.add_action(action='withdraw', eth_usd='ETH', quantity=eth)

    def generate_usd(self, usd):
        self.usd_generated += usd
        self.usd_on_hand += usd
        self.add_action(action='generate', eth_usd='USD', quantity=usd)

    def trade(self, usd, price, side):
        eth_purchased = usd/(price * slippage)
        self.eth_on_hand += eth_purchased
        self.usd_on_hand -= usd
        self._update_calculations()

    def update_price(self, price):
        self.price = price
        self._update_calculations()

    # NOTE: this is still saved as close() in loan/personal cdp
    def summarize(self):
        self.eth_owed = self.usd_generated / price
        self.end_eth = self.eth_deposited - eth_owed
        self.pct_change_eth_price = (price - self.start_price) / self.start_price
        self.pct_change_eth_balance = (end_eth - self.start_eth_on_hand) / self.start_eth_on_hand
        actions = pd.DataFrame(self.actions)
        summary = pd.DataFrame(self.__dict__)
        actions.to_csv('data/simulations/actions.csv')
        summary.to_csv('data/simulations/summary.csv')
