// Solidity code for NeuroToken (ERC-20)
pragma solidity ^0.8.0;

contract NeuroToken {
    string public name = "NeuroToken";
    string public symbol = "NTK";
    uint256 public totalSupply;
    mapping(address => uint256) public balances;

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
    }

    function transfer(address recipient, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
    }
}
