pragma solidity ^0.4.21;

// @author Carter Carlson
// @title Delaying a smart contract transaction
contract DelayedPayment {

    /* Declaring variables */
    uint lockedUntil;
    address recipient;
    address public scheduledTx

    /* Functions */

    function Schedule(
        address _recipient,
        bytes   _callData,
        uint[8] _uintArgs
    )
        public
        payable
        returns (address);


    function delayedPayment(
        address _scheduler,
        uint    numBlocks,
        address _recipient
    )
        public
        payable
    {
        scheduler = SchedulerInterface(_scheduler);
        lockedUntil = block.number + numBlocks;
        // recipient = _recipient;
        scheduledTx = scheduler.schedule.value(0.1 ether) ( // 0.1 ether pays for gas, bounty, and fee
            this,               // send to self
            "",                 // trigger fallback function
            [
                200000,         // gas to send with Tx
                0,              // wei to send with Tx
                255,            // side of the Tx execution window
                lockedUntil,    // start of the execution window
                20 gwei,        // gas price for the transaction
                20 gwei,        // fee included in the transaction
                20 gwei,        // bounty that awards the executor of the transaction
                30 gwei         // required amt of wei the claimer requires for deposit.
            ]
        );
    }

    function () public payable {
        if (msg.value > 0) { // this handles recieving remaining funds sent while scheduling (0.1 ether)
            return;
        } else if (address(this).balance > 0) {
            payout();
        } else {
            revert();
        }
    }


}
