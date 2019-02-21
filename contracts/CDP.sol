pragma solidity ^0.4.20;

contract CDP {

    /* DECLARING VARIABLES */
    address public owner;


    /* MAPPING */


    /* EVENTS */
    event logDeposit (uint id);


    /* MODIFIERS */
    // validate the CDP id exists
    modifier CDPExists(uint _id) { require( oraclize()     ) }


    /* STRUCTS */


    /* CONSTRUCTUR */
    cunstructor() public {
        owner = msg.sender;
    }


    /* VIEWS */


    /* METHODS */
    function addCDP(uint _id)
        public
    {
        // 1. validate id requested is less than total id's available
        // 2. validate that for the id requested, the message sender is the same
        //      as the CDP owner address.

    }

}
