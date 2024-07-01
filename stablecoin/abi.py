from pathlib import Path
from simular import contract_from_raw_abi, create_account, contract_from_abi_bytecode

PATH = Path(__file__).parent


# Fixed wallet addresses
ADMIN = "0x0c7ccc4f1f495a1c2fe661ae4b6ae83309cd06b2"
MINTER = "0xa47d88347e06922641b1fdc9ad527a221787b95a"

ABI = """[{"type":"constructor","inputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"DOMAIN_SEPARATOR","inputs":[],"outputs":[{"name":"","type":"bytes32","internalType":"bytes32"}],"stateMutability":"view"},{"type":"function","name":"addMinter","inputs":[{"name":"minter","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"admin","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"allowance","inputs":[{"name":"","type":"address","internalType":"address"},{"name":"","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"approve","inputs":[{"name":"spender","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"balanceOf","inputs":[{"name":"","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"burn","inputs":[{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"decimals","inputs":[],"outputs":[{"name":"","type":"uint8","internalType":"uint8"}],"stateMutability":"view"},{"type":"function","name":"mint","inputs":[{"name":"to","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"name","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"nonces","inputs":[{"name":"","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"permit","inputs":[{"name":"owner","type":"address","internalType":"address"},{"name":"spender","type":"address","internalType":"address"},{"name":"value","type":"uint256","internalType":"uint256"},{"name":"deadline","type":"uint256","internalType":"uint256"},{"name":"v","type":"uint8","internalType":"uint8"},{"name":"r","type":"bytes32","internalType":"bytes32"},{"name":"s","type":"bytes32","internalType":"bytes32"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"symbol","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"totalSupply","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"transfer","inputs":[{"name":"to","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"transferFrom","inputs":[{"name":"from","type":"address","internalType":"address"},{"name":"to","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"event","name":"Approval","inputs":[{"name":"owner","type":"address","indexed":true,"internalType":"address"},{"name":"spender","type":"address","indexed":true,"internalType":"address"},{"name":"amount","type":"uint256","indexed":false,"internalType":"uint256"}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"name":"from","type":"address","indexed":true,"internalType":"address"},{"name":"to","type":"address","indexed":true,"internalType":"address"},{"name":"amount","type":"uint256","indexed":false,"internalType":"uint256"}],"anonymous":false}]"""
BITS = "60e06040523480156200001157600080fd5b506040518060400160405280600481526020016341636d6560e01b815250604051806040016040528060018152602001604160f81b815250601282600090816200005c9190620001e0565b5060016200006b8382620001e0565b5060ff81166080524660a052620000816200009f565b60c0525050600680546001600160a01b03191633179055506200032a565b60007f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f6000604051620000d39190620002ac565b6040805191829003822060208301939093528101919091527fc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc660608201524660808201523060a082015260c00160405160208183030381529060405280519060200120905090565b634e487b7160e01b600052604160045260246000fd5b600181811c908216806200016657607f821691505b6020821081036200018757634e487b7160e01b600052602260045260246000fd5b50919050565b601f821115620001db57600081815260208120601f850160051c81016020861015620001b65750805b601f850160051c820191505b81811015620001d757828155600101620001c2565b5050505b505050565b81516001600160401b03811115620001fc57620001fc6200013b565b62000214816200020d845462000151565b846200018d565b602080601f8311600181146200024c5760008415620002335750858301515b600019600386901b1c1916600185901b178555620001d7565b600085815260208120601f198616915b828110156200027d578886015182559484019460019091019084016200025c565b50858210156200029c5787850151600019600388901b60f8161c191681555b5050505050600190811b01905550565b6000808354620002bc8162000151565b60018281168015620002d75760018114620002ed576200031e565b60ff19841687528215158302870194506200031e565b8760005260208060002060005b85811015620003155781548a820152908401908201620002fa565b50505082870194505b50929695505050505050565b60805160a05160c051610cec6200035a60003960006104c40152600061048f015260006101750152610cec6000f3fe608060405234801561001057600080fd5b50600436106101005760003560e01c806370a0823111610097578063a9059cbb11610066578063a9059cbb14610234578063d505accf14610247578063dd62ed3e1461025a578063f851a4401461028557600080fd5b806370a08231146101d95780637ecebe00146101f957806395d89b4114610219578063983b2d561461022157600080fd5b8063313ce567116100d3578063313ce567146101705780633644e515146101a957806340c10f19146101b157806342966c68146101c657600080fd5b806306fdde0314610105578063095ea7b31461012357806318160ddd1461014657806323b872dd1461015d575b600080fd5b61010d6102b0565b60405161011a91906109d0565b60405180910390f35b610136610131366004610a3a565b61033e565b604051901515815260200161011a565b61014f60025481565b60405190815260200161011a565b61013661016b366004610a64565b6103ab565b6101977f000000000000000000000000000000000000000000000000000000000000000081565b60405160ff909116815260200161011a565b61014f61048b565b6101c46101bf366004610a3a565b6104e6565b005b6101c46101d4366004610aa0565b610547565b61014f6101e7366004610ab9565b60036020526000908152604090205481565b61014f610207366004610ab9565b60056020526000908152604090205481565b61010d610554565b6101c461022f366004610ab9565b610561565b610136610242366004610a3a565b6105d0565b6101c4610255366004610adb565b610636565b61014f610268366004610b4e565b600460209081526000928352604080842090915290825290205481565b600654610298906001600160a01b031681565b6040516001600160a01b03909116815260200161011a565b600080546102bd90610b81565b80601f01602080910402602001604051908101604052809291908181526020018280546102e990610b81565b80156103365780601f1061030b57610100808354040283529160200191610336565b820191906000526020600020905b81548152906001019060200180831161031957829003601f168201915b505050505081565b3360008181526004602090815260408083206001600160a01b038716808552925280832085905551919290917f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925906103999086815260200190565b60405180910390a35060015b92915050565b6001600160a01b03831660009081526004602090815260408083203384529091528120546000198114610407576103e28382610bd1565b6001600160a01b03861660009081526004602090815260408083203384529091529020555b6001600160a01b0385166000908152600360205260408120805485929061042f908490610bd1565b90915550506001600160a01b0380851660008181526003602052604090819020805487019055519091871690600080516020610c97833981519152906104789087815260200190565b60405180910390a3506001949350505050565b60007f000000000000000000000000000000000000000000000000000000000000000046146104c1576104bc61087a565b905090565b507f000000000000000000000000000000000000000000000000000000000000000090565b3360009081526007602052604090205460ff166105395760405162461bcd60e51b815260206004820152600c60248201526b2737ba10309036b4b73a32b960a11b60448201526064015b60405180910390fd5b6105438282610914565b5050565b610551338261096e565b50565b600180546102bd90610b81565b6006546001600160a01b031633146105ac5760405162461bcd60e51b815260206004820152600e60248201526d4e6f74207468652041646d696e2160901b6044820152606401610530565b6001600160a01b03166000908152600760205260409020805460ff19166001179055565b336000908152600360205260408120805483919083906105f1908490610bd1565b90915550506001600160a01b03831660008181526003602052604090819020805485019055513390600080516020610c97833981519152906103999086815260200190565b428410156106865760405162461bcd60e51b815260206004820152601760248201527f5045524d49545f444541444c494e455f455850495245440000000000000000006044820152606401610530565b6000600161069261048b565b6001600160a01b038a811660008181526005602090815260409182902080546001810190915582517f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c98184015280840194909452938d166060840152608083018c905260a083019390935260c08083018b90528151808403909101815260e08301909152805192019190912061190160f01b6101008301526101028201929092526101228101919091526101420160408051601f198184030181528282528051602091820120600084529083018083525260ff871690820152606081018590526080810184905260a0016020604051602081039080840390855afa15801561079e573d6000803e3d6000fd5b5050604051601f1901519150506001600160a01b038116158015906107d45750876001600160a01b0316816001600160a01b0316145b6108115760405162461bcd60e51b815260206004820152600e60248201526d24a72b20a624a22fa9a4a3a722a960911b6044820152606401610530565b6001600160a01b0390811660009081526004602090815260408083208a8516808552908352928190208990555188815291928a16917f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925910160405180910390a350505050505050565b60007f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f60006040516108ac9190610be4565b6040805191829003822060208301939093528101919091527fc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc660608201524660808201523060a082015260c00160405160208183030381529060405280519060200120905090565b80600260008282546109269190610c83565b90915550506001600160a01b038216600081815260036020908152604080832080548601905551848152600080516020610c9783398151915291015b60405180910390a35050565b6001600160a01b03821660009081526003602052604081208054839290610996908490610bd1565b90915550506002805482900390556040518181526000906001600160a01b03841690600080516020610c9783398151915290602001610962565b600060208083528351808285015260005b818110156109fd578581018301518582016040015282016109e1565b506000604082860101526040601f19601f8301168501019250505092915050565b80356001600160a01b0381168114610a3557600080fd5b919050565b60008060408385031215610a4d57600080fd5b610a5683610a1e565b946020939093013593505050565b600080600060608486031215610a7957600080fd5b610a8284610a1e565b9250610a9060208501610a1e565b9150604084013590509250925092565b600060208284031215610ab257600080fd5b5035919050565b600060208284031215610acb57600080fd5b610ad482610a1e565b9392505050565b600080600080600080600060e0888a031215610af657600080fd5b610aff88610a1e565b9650610b0d60208901610a1e565b95506040880135945060608801359350608088013560ff81168114610b3157600080fd5b9699959850939692959460a0840135945060c09093013592915050565b60008060408385031215610b6157600080fd5b610b6a83610a1e565b9150610b7860208401610a1e565b90509250929050565b600181811c90821680610b9557607f821691505b602082108103610bb557634e487b7160e01b600052602260045260246000fd5b50919050565b634e487b7160e01b600052601160045260246000fd5b818103818111156103a5576103a5610bbb565b600080835481600182811c915080831680610c0057607f831692505b60208084108203610c1f57634e487b7160e01b86526022600452602486fd5b818015610c335760018114610c4857610c75565b60ff1986168952841515850289019650610c75565b60008a81526020902060005b86811015610c6d5781548b820152908501908301610c54565b505084890196505b509498975050505050505050565b808201808211156103a5576103a5610bbb56feddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3efa2646970667358221220ab24352f39bebbd95e8ff2b84233b6b4adf1c226f505d428dec7180654fb644f64736f6c63430008150033"


def stablecoin_contract(evm):
    """
    Load the contract based on the ABI and bytecode
    TODO: REMOVE Move this json out to another location.  The 'out' directory
    doesn't exist in github
    """
    # with open(f"{PATH}/../out/AcmeStableCoin.sol/AcmeStableCoin.json") as f:
    #    full = f.read()
    # return contract_from_raw_abi(evm, full)
    return contract_from_abi_bytecode(evm, ABI, bytes.fromhex(BITS))


def deploy_and_loan_contract(evm):
    """
    Deploy and load the stablecoin contract using the pre-generated addresses.
    Add a single authorized minter.

    Returns the contract
    """
    # setup accounts
    create_account(evm, address=ADMIN)
    create_account(evm, address=MINTER)

    # deploy the contract
    # coin = stablecoin_contract(evm)
    coin = contract_from_abi_bytecode(evm, ABI, bytes.fromhex(BITS))
    coin.deploy(caller=ADMIN)

    # add the minter
    coin.addMinter.transact(MINTER, caller=ADMIN)

    return coin
