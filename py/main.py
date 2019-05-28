import pandas as pd
from py.cdp import CDP

def main():
    df = []
    cdp_1 = CDP()
    withdrawal_1 = cdp_1.usd_available_to_generate * 0.5
    cdp_1.generate(withdrawal_1)
    cdp_1.deposit(eth=withdrawal_1/cdp_1.price)

    cdp_2 = CDP()
    cdp_2.generate(withdrawal_1)
    cdp_2.deposit(eth=withdrawal_1/cdp_2.price)
    cdp_2.generate(withdrawal_1)
    cdp_2.deposit(eth=withdrawal_1/cdp_2.price)

    cdp_3 = CDP()
    cdp_3.generate(withdrawal_1)
    cdp_3.deposit(eth=withdrawal_1/cdp_3.price)
    withdrawal_2 = cdp_3.usd_available_to_generate * .5
    cdp_3.generate(withdrawal_2)
    cdp_3.deposit(eth=withdrawal_2/cdp_3.price)

    for i in range(100, 1000):
        CDP_1 = cdp_1.close(price=i) * i
        CDP_2 = cdp_2.close(price=i) * i
        CDP_3 = cdp_3.close(price=i) * i
        df.append([i, CDP_1, CDP_2, CDP_3])

    df = pd.DataFrame(df, columns=['Price', 'CDP-1', 'CDP-2', 'CDP-3'])
    df.to_csv('data/simulations/basic_comparison.csv', index=False)

if __name__ == '__main__':
    main()
