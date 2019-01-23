pragma solidity >=0.4.22 <0.6.0;

contract SimpleWallet {

    // State variables
    address public owner;
    mapping (address => uint) internal balances;
    mapping (address => bool) public enrolled;

    // Events
    event logEnroll(address accountAddress);
    event logDeposit(address accountAddress, uint amount);
    event logWithdrawal(address accountAddress, uint amount, uint newBalance);

    // Constructor
    constructor()
        public
    {
        owner = msg.sender;
    }

    // Views
    function balance()
        public
        view
        returns (uint)
    {
        return balances[msg.sender];
    }

    // Functions
    function enroll()
        public
    {
        emit logEnroll(msg.sender);
        enrolled[msg.sender] = true;
        balances[msg.sender] = 0;
    }

    function deposit(uint amount)
        public
        payable
        returns (uint)
    {
        require(enrolled[msg.sender] == true);
        emit logDeposit(msg.sender, amount);
        balances[msg.sender] += msg.value;
        return balances[msg.sender];
    }

    function withdraw(uint amount)
        public
        returns (uint)
    {
        require(enrolled[msg.sender] == true);
        require(balances[msg.sender] >= amount);
        balances[msg.sender] -= amount;
        emit logWithdrawal(msg.sender, amount, balances[msg.sender]);
        msg.sender.transfer(amount);
        return balances[msg.sender];
    }

    function end()
        public
    {
        require(msg.sender == owner);
        selfdestruct(owner);
    }
    
}
