/* 1. Establish how we want to interact with Alarm service's Scheduler contract  */

// returns the address of the newly created `TransactionRequest` contract
contract SchedulerInterface {
	// param
	// @toAddress	- The address to send the tx to
	// @callData	- The bytes used as the data for the tx
	// @windowSize	- Number of blocks after windowStart where the tx will still be executable
	// @uintArgs[0]	- callGas		- amount of gas sent with the tx
	// @uintArgs[1]	- callValue		- amount of ether(in wei) to be sent with the tx
	// @uintArgs[2]	- windowStart	- the first block number the tx will be executable
    function scheduleTransaction(address toAddress,
                                 bytes callData,
                                 uint8 windowSize,	//
                                 uint[3] uintArgs)
	    public
		returns (address);
}

/* 2. Create a contract that can use the scheduling contract */

contract DelayedPayment {
	SchedulerInterface constant scheduler = SchedulerInterface(0xTODO);

	uint lockedUntil;
	address recipient;  // This will be the smart contract associated with the CDP

	function DelayedPayment(address _recipient, uint numBlocks)
	{
		// Set the time the funds are locked up
		lockedUntil = block.number + numBlocks;
		recipient = _recipient;

		uint[3] memory uintArgs = [
			200000,			// Amount of gas sent with tx
			0,				// Amount of ether (in wei) that will be sent with the tx
			lockedUntil		// The first block number that the tx can be executed
		];
		scheduler.scheduleTransaction.value(2 ether) (
			address(this),	// Address the tx will be sent to
			"",				// Call data sent with the tx
			255,			// Number of blocks this can be executable
			uintArgs		// Arguments defined above
		);
	}

	function()
	{
		if (this.balance > 0) {
			payout();
		}
	}

	function payout()
		public
		returns(bool)
	{
		if (now < lockedUntil) return false;
		return recipient.call.value(this.balance)();
	}

}
