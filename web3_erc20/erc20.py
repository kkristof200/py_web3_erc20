# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3, eth as Eth
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


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Read (Cachable)

    def name(self) -> str:
        if not self.__name:
            self.__name = self.functions.name().call()

        return self.__name

    def symbol(self) -> str:
        if not self.__symbol:
            self.__symbol = self.functions.symbol().call()

        return self.__symbol

    def decimals(self) -> int:
        if not self.__decimals:
            self.__decimals = self.functions.decimals().call()

        return self.__decimals


    # Read (Non-Cachable)

    def total_supply(self) -> int:
        return self.functions.totalSupply().call()

    # alias
    totalSupply = total_supply

    def balance_of(
        self,
        address: str
    ) -> int:
        return self.functions.balanceOf(Web3.toChecksumAddress(address)).call()

    # alias
    balanceOf = balance_of

    def allowance(
        self,
        owner: str,
        spender: str
    ) -> int:
        return self.functions.allowance(
            Web3.toChecksumAddress(owner),
            Web3.toChecksumAddress(spender)
        ).call()


    # Write

    def approve(
        self,
        spender: str,
        amount: int,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.approve(
                Web3.toChecksumAddress(spender),
                amount
            ),
            account=account
        )

    def decrease_allowance(
        self,
        spender: str,
        subtracted_value: int,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.decreaseAllowance(
                Web3.toChecksumAddress(spender),
                subtracted_value
            ),
            account=account
        )

    # alias
    decreaseAllowance = decrease_allowance

    def increase_allowance(
        self,
        spender: str,
        added_value: int,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.increaseAllowance(
                Web3.toChecksumAddress(spender),
                added_value
            ),
            account=account
        )

    # alias
    increaseAllowance = increase_allowance

    def transfer(
        self,
        recipient: str,
        amount: int,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.transfer(
                recipient,
                amount
            ),
            account=account
        )

    def transfer_from(
        self,
        sender: str,
        recipient: int,
        amount: int,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.transferFrom(
                Web3.toChecksumAddress(sender),
                Web3.toChecksumAddress(recipient),
                amount
            ),
            account=account
        )
    
    # alias
    transferFrom = transfer_from

    def renounce_ownership(
        self,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.renounceOwnership(),
            account=account
        )
    
    # alias
    renounceOwnership = renounce_ownership

    def transfer_ownership(
        self,
        new_owner: str,
        account: Optional[LocalAccount] = None
    ) -> str:
        return self.send_transaction(
            function=self.functions.transferOwnership(
                Web3.toChecksumAddress(new_owner)
            ),
            account=account
        )
    
    # alias
    transferOwnership = transfer_ownership


    # Custom

    def toWei(
        self,
        amount: int
    ) -> float:
        return amount * pow(10, self.decimals()) if self.decimals() > 0 else amount

    def toEth(
        self,
        amount: int
    ) -> float:
        return amount / pow(10, self.decimals()) if self.decimals() > 0 else amount

    def marketCap(
        self,
        price_per_token: int
    ) -> int:
        return price_per_token * self.totalSupply()

    def marketCapEth(
        self,
        price_per_token: int
    ) -> int:
        return self.toEth(self.marketCap(price_per_token))

    def marketCapWei(
        self,
        price_per_token: int
    ) -> int:
        return self.toWei(self.marketCap(price_per_token))


# -------------------------------------------------------------------------------------------------------------------------------- #