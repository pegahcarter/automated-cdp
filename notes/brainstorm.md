# Automate my CDP
## By: Carter Carlson

### Appendix
  1. Plan for strategy
  2. Time periods for testing
  3. Calculations
  4. Steps taken to deploy on a smart contract


### 1. Plan for strategy
- $5,000 @ day 0
- We assume an unlimited amount of $ outside of CDP
- Validate $ is above our degree of confidence
- Keep CDP ratio between 175% and 225%
  - if current ratio drops to 175%
    - Deposit more ETH to set ratio to 200%
  - if current ratio increases to 225%
    - generate more DAI to set ratio to 200%

1. Deposit a fixed amt on day 0
2. Withdraw a fixed amt on day 0
    - base withdrawal on liquidation ratio
    - do we need to display liquidation price?


### 2. Time periods for testing
1. min => max
2. max => min
3. min => max => min (a & b)


### 3. Calculations
- Liquidation Ratio
  - (eth deposited * current price) / dai generated
- Liquidation Price
  - (dai generated * 3/2) / eth deposited


### 4. Steps taken to deploy on a contract
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
