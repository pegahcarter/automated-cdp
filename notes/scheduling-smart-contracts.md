## Ethereum Alarm Clock Documentation


---

### Functions

#### schedule
- @param
  - `address _recipient`: The address we're sending our Tx to
  - `bytes callData`: The bytes used as data for the Tx
  - `uint callGas`: Amount of gas sent with Tx
  - `uint callValue`: Amount of wei sent with Tx
  - `uint8 windowSize`: Number of blocks in which the Tx can execute
  - `uint windowStart`: The first block number that the transaction will be executable.
  - `uint gasPrice`: The gas price (in wei) which must be sent by the executing party to execute the transaction.
  - `uint fee`: The fee amount (in wei) included in the transaction for protocol maintainers.
  - `uint bounty`: The payment (in wei)included in the transaction to incentivse the executing arguments
  - `uint deposit`: (optional) Required amount of ether (in wei) to be staked by executing agents





__@param__
- `address _recipient`
  - The address we're sending our Tx to
- `bytes callData`
  - The bytes used as data for the Tx
- `uint callGas`
  - Amount of gas sent with Tx
- `uint callValue`
  - Amount of wei sent with Tx
- `uint8 windowSize`
  - Number of blocks in which the Tx can execute
- `uint windowStart`
  - The first block in which the Tx can execute
- `uint gasPrice`
  - The gas price (in wei) which must be sent by the executing party to execute the transaction.
  - gas which must be sent by the
- `uint fee`
  - The fee amount (in wei) included in the transaction for protocol maintainers.
  - gwei in the Tx for protocol maintainers.
- `uint bounty`
  - The payment (in wei)included in the transaction to incentivize the executing arguments
  - gwei in the Tx to prioritize the executing arguments  
- `uint deposit`
  - (optional) Required amount of ether (in wei) to be staked by executing agents



// This function takes a total of 10 parameters
  // @param _recipient    - address to send the transaction to
  // @param
  // @param
  // @param
  // @param
  // @param
  // @param
  // @param
  // @param
  // @param
  // @param ### Retrieving Data
