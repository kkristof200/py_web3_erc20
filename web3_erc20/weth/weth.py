# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, List

# Pip
from web3.eth import Eth
from web3.contract import ContractEvent
from eth_account.signers.local import LocalAccount

# Local
from web3_erc20.erc20 import ERC20
from ._abi import weth_abi

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: ERC20 --------------------------------------------------------- #

class Weth(ERC20):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        eth: Eth,
        address: str,
        abi: List[dict] = weth_abi,
        account: Optional[LocalAccount] = None
    ):
        super().__init__(
            eth=eth,
            address=address,
            abi=abi,
            account=account
        )


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def deposit_event(self) -> ContractEvent:
        return self.events.Deposit()


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Write

    @property
    def deposit(
        self,
        wei: int,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.deposit(wei),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )


# -------------------------------------------------------------------------------------------------------------------------------- #