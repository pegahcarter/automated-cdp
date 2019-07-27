import pandas as pd
from py.cdp import CDP

cdp = CDP(price=225, eth_deposited=85.722)
withdrawal_1 = cdp.summary['usd_available_to_generate'] * 0.
cdp.generate(withdrawal_1)
eth_purchased = cdp.trade(side='BUY', usd=withdrawal_1, price=228)
cdp.deposit(eth=cdp.summary['eth_on_hand'])
cdp.summarize(price=350, save=True)







if __name__ == '__main__':
    main()
