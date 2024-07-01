// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.13;

import {ERC20} from "solmate/tokens/ERC20.sol";

/// Simple fictitious stablecoin
contract AcmeStableCoin is ERC20 {
    /// manage minters
    address public admin;
    /// map of allowed minters
    mapping(address => bool) minters;

    constructor() ERC20("Acme", "A", 18) {
        admin = msg.sender;
    }

    /// Add a minter
    function addMinter(address minter) external {
        require(msg.sender == admin, "Not the Admin!");
        minters[minter] = true;
    }

    /// Mint 'to'. Caller must be a authorized minter
    function mint(address to, uint256 amount) external {
        require(minters[msg.sender], "Not a minter");
        _mint(to, amount);
    }

    /// You can only burn your tokens
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
