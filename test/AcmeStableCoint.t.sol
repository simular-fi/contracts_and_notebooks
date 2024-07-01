// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {AcmeStableCoin} from "../src/AcmeStableCoin.sol";

contract AcmeStableCoinTest is Test {
    AcmeStableCoin public coin;

    address admin = makeAddr("admin");
    address minter = makeAddr("minter");

    address bob = makeAddr("bob");
    address alice = makeAddr("alice");

    function setUp() public {
        vm.startPrank(admin);
        coin = new AcmeStableCoin();
        coin.addMinter(minter);
        vm.stopPrank();
    }

    function test_only_minter_can_mint() public {
        vm.startPrank(bob);
        vm.expectRevert();
        coin.mint(alice, 1e18);
        vm.stopPrank();

        assertEq(coin.balanceOf(alice), 0);

        vm.prank(minter);
        coin.mint(alice, 1e18);

        assertEq(coin.balanceOf(alice), 1e18);
    }

    function test_burn() public {
        vm.prank(minter);
        coin.mint(alice, 1e18);

        assertEq(coin.balanceOf(alice), 1e18);

        vm.prank(alice);
        coin.burn(1e18);

        assertEq(coin.balanceOf(alice), 0);
    }
}
