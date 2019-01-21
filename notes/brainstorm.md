### Plan for strategy
- $5,000 @ day 0
- We assume an unlimited amount of $ outside of CDP
- Validate $ is above our degree of confidence

1. Deposit a fixed amt on day 0
2. Withdraw a fixed amt on day 0
    - base withdrawal on liquidation price
    - liquidation price will be $20 below current prices
    - that would be dangerous if ETH was $1,000/ETH, because $20 is only 2% of $1,000
    - Let's base it on standard deviation
        - What's the degree of confidence?

---

- We start at price X, with a liquidation price of ?
- After the price is ? standard deviations away from X, we adjust our liquidation price
- Let's say we always want to stay at least X standard deviations away from price X
  - % chance within 1 sdev.:    68.2%
  - % chance within 2 sdev.:    95.45%
  - % chance within 3 sdev.:    99.73%      - once every 370 days
  - % chance within 4 sdev.:    99.99994%   - once every 1,666,667 days / 4,566 years
    - 0.02% chance in one year

---

### Time periods to use for testing
1. min => max
2. max => min
3. min => max => min (a & b)


---

### Steps to deploy on a contract
1. open/close/deposit a CDP using ganache-cli
2. use contract/oracle to fetch current ETH price
3. deploy test smart contract on mainnet
4. deploy smart contract for CDP
  - Criteria
    - Daily frequency
    - Withdraw to set liq. price @ 5 standard deviations away from avg. volatility
    - If price drops and liq. price @ 4 sdevs, lower liq. price @ 5 sdevs
    - If price raises and liq. price is @ 6 sdevs, raise liq. price @ 5 sdevs
5. Analysis of risk
  - risk of hitting our liq. price w/in 24 hours
  - factoring in liq. fees
    - Is there an optimal liq. price that includes liq. fees?
    - If so, what's the performance relative to a CDP w/out factoring liq. fees?
