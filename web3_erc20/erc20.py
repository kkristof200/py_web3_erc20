# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from web3 import eth as Eth

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
        abi: str = erc20_abi
    ):
        super().__init__(
            eth=eth,
            address=address,
            abi=abi
        )

        self.__name = None
        self.__symbol = None
        self.__decimals = None


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Cachable

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


    # Non-Cachable
    
    def totalSupply(self) -> int:
        return self.functions.totalSupply().call()

    def balanceOf(
        self,
        address: str
    ) -> int:
        return self.functions.balanceOf(address).call()


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