# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Union
from decimal import Decimal

# Pip
from web3 import Web3
from web3.eth import Eth
from web3.contract import ContractEvent, ContractFunction
from eth_account.signers.local import LocalAccount

from web3_wrapped_contract import WrappedContract

# Local
from ._abi import erc20_abi

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: ERC20 --------------------------------------------------------- #

class ERC20(WrappedContract):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        eth: Eth,
        address: str,
        abi: str = erc20_abi,
        account: Optional[LocalAccount] = None
    ):
        super().__init__(
            eth=eth,
            address=address,
            abi=abi,
            account=account
        )

        self.__name = None
        self.__symbol = None
        self.__decimals = None


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def approval(self) -> ContractEvent:
        return self.events.Approval()

    @property
    def transfer(self) -> ContractEvent:
        return self.events.Transfer()


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Read (Cachable)

    def name(self) -> str:
        if not self.__name:
            self.__name = self.name_method().call()

        return self.__name

    def name_method(self) -> ContractFunction:
        return self.functions.name()


    def symbol(self) -> str:
        if not self.__symbol:
            self.__symbol = self.symbol_method().call()

        return self.__symbol

    def symbol_method(self) -> ContractFunction:
        return self.functions.symbol()


    def decimals(self) -> int:
        if not self.__decimals:
            self.__decimals = self.decimals_method().call()

        return self.__decimals

    def decimals_method(self) -> ContractFunction:
        return self.functions.decimals()


    # Read (Non-Cachable)

    def total_supply(self) -> int:
        return self.total_supply_method().call()

    # alias
    totalSupply = total_supply

    def total_supply_method(self) -> ContractFunction:
        return self.functions.totalSupply()


    def balance_of(
        self,
        address: str
    ) -> int:
        return self.balance_of_method(address).call()

    # alias
    balanceOf = balance_of

    def balance_of_method(
        self,
        address: str
    ) -> ContractFunction:
        return self.functions.balanceOf(Web3.toChecksumAddress(address))


    def allowance(
        self,
        owner: str,
        spender: str
    ) -> int:
        return self.allowance_method(owner, spender).call()

    def allowance_method(
        self,
        owner: str,
        spender: str
    ) -> ContractFunction:
        return self.functions.allowance(
            Web3.toChecksumAddress(owner),
            Web3.toChecksumAddress(spender)
        )


    # Write

    def approve(
        self,
        spender: str,
        amount: int,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.approve(
                Web3.toChecksumAddress(spender),
                amount
            ),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    def decrease_allowance(
        self,
        spender: str,
        subtracted_value: int,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.decreaseAllowance(
                Web3.toChecksumAddress(spender),
                subtracted_value
            ),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    # alias
    decreaseAllowance = decrease_allowance

    def increase_allowance(
        self,
        spender: str,
        added_value: int,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.increaseAllowance(
                Web3.toChecksumAddress(spender),
                added_value
            ),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    # alias
    increaseAllowance = increase_allowance

    def transfer(
        self,
        recipient: str,
        amount: int,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.transfer(
                recipient,
                amount
            ),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    def transfer_from(
        self,
        sender: str,
        recipient: int,
        amount: int,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.transferFrom(
                Web3.toChecksumAddress(sender),
                Web3.toChecksumAddress(recipient),
                amount
            ),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    # alias
    transferFrom = transfer_from

    def renounce_ownership(
        self,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.renounceOwnership(),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    # alias
    renounceOwnership = renounce_ownership

    def transfer_ownership(
        self,
        new_owner: str,
        gas: Optional[int] = None,
        gas_price: Optional[int] = None,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.transferOwnership(
                Web3.toChecksumAddress(new_owner)
            ),
            gas=gas,
            gas_price=gas_price,
            max_fee_per_gas=max_fee_per_gas,
            max_priority_fee_per_gas=max_priority_fee_per_gas,
            account=account
        )

    # alias
    transferOwnership = transfer_ownership


    # Custom

    def toWei(
        self,
        amount: Union[int, float, Decimal]
    ) -> int:
        return int(Decimal(amount) * Decimal(pow(10, self.decimals()))) if self.decimals() > 0 else int(amount)

    def toEth(
        self,
        amount: Union[int, float, Decimal]
    ) -> Decimal:
        return Decimal(amount) / Decimal(pow(10, self.decimals())) if self.decimals() > 0 else Decimal(amount)

    def marketCap(
        self,
        price_per_token: Union[int, float, Decimal],
        total_supply: Optional[Union[int, float, Decimal]] = None
    ) -> Decimal:
        return Decimal(price_per_token) * Decimal(total_supply or self.total_supply())

    def marketCapEth(
        self,
        price_per_token: Union[int, float, Decimal]
    ) -> Decimal:
        return self.toEth(self.marketCap(price_per_token))

    def marketCapWei(
        self,
        price_per_token: Union[int, float, Decimal]
    ) -> int:
        return self.toWei(self.marketCap(price_per_token))


# -------------------------------------------------------------------------------------------------------------------------------- #