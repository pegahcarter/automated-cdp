from cdp import CDP


starting_eth = 100
dai_generated = 5000


# Create CDP
cdp = CDP(price=200, start_eth_on_hand=starting_eth)

# Deposit starting eth on hand
cdp.deposit(eth=starting_eth)

# Generate USD
cdp.generate(dai_generated)

# Trade USD for ETH and assume we pay a 1% premium on ETH
eth_purchased = cdp.trade(side='BUY', dai=dai_generated, price=cdp.price*1.01)

# Deposit ETH purchased into CDP
cdp.deposit(eth=eth_purchased)

# Summarize CDP performance when ETH price hits $300
cdp.summarize(price=300, save=True)
