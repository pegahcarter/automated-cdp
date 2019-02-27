# Automate my CDP
## By: Carter Carlson

### Appendix
  1. Plan for strategy
  2. Time periods for testing
  3. Variables of interest
  4. Variables needed for automation
  5. Standard deviation metrics
  6. Steps to deploy on a smart contract


### 1. Plan for strategy
- $5,000 @ day 0
- We assume an unlimited amount of $ outside of CDP
- Validate $ is above our degree of confidence
- Keep CDP ratio between 175% and 225%
  - if current ratio drops to 175%
    - Deposit more ETH to set ratio to 200%
  - if current ratio increases to 225%
    - generate more DAI to set ratio to 200%


### 2. Time periods for testing
1. Interval
  - Check price at each row in prices.csv
  - 1 row = 1 day
  - Todo: Set interval of price check w/ more robust dataset
2. Start price of simulation => End price of simulation
  - min => max
  - max => min
  - price does not fluctuate the entire time


### 3. Variables of interest
- Liquidation Ratio
  - (eth deposited * current price) / dai generated
- Liquidation Price
  - (dai generated * 3/2) / eth deposited
- Time interval for CDP adjustments
  - static or dynamic?
    - fixed interval
          - calculate risk by avg. volatility over the interval
      - this number should be quantifiable
    - dynamic interval
      - all risk could be eliminated
- Probability of liquidation
  - Relates to CDP adjustment interval


### 4. Stored variables needed for automation
- ETH locked (updated from CDP actions)
- DAI minted (updated from CDP actions)
- Price points to trigger CDP action (updated from CDP actions)
- Current ETH price (update every price check)
- Liquidation Ratio (update every price check)


### 5. Standard deviation metrics
- After the price is 1 unit of sdev away from X, we adjust our liquidation price
- Let's say we always want to stay at least X standard deviations away from the price
  - % chance within 1 sdev.:    68.2%
  - % chance within 2 sdev.:    95.45%
  - % chance within 3 sdev.:    99.73%      - once every 370 days
  - % chance within 4 sdev.:    99.99994%   - once every 1,666,667 days / 4,566 years
    - 0.02% chance in one year



### 6. Steps to deploy on a contract
1. open/close/deposit a CDP using ganache-cli
2. find reliable source to fetch current ETH price
3. deploy test smart contract on mainnet
4. deploy smart contract for CDP
  - Criteria
    - Daily frequency
    - Withdraw to set liq. price @ X standard deviations away from avg. volatility
    - If price drops and liq. price @ X-1 sdevs, lower liq. price @ X sdevs
    - If price raises and liq. price is @ X + 1 sdevs, raise liq. price @ X sdevs
5. Analysis of risk
  - risk of hitting our liq. price w/in 24 hours
  - factoring in liq. risk and fees
    - Is there an optimal liq. price calculatino that incorporates liq. fees?
    - If so, what's the performance relative to a CDP w/out factoring liq. fees?
