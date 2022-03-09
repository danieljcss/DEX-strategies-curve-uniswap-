from brownie import myUSD, StableSwapMyUSD, Strategies, accounts
import time

attacker = accounts.load("attacker")


# setting Smart Contracts for StableCoins and Swap
myusd = myUSD.at("")

swap = StableSwapMyUSD.at("")


# Setting parameters for the transaction, high gas price to skip queue

params = { 
    "from": attacker,
    "gas_price": "6 gwei"
    }

# Setting amounts to transfer
def allowAndSwap(am_myusd,token_index):
    """
    @notice Perform an exchange between myUSD and one other stablecoin of the 3pool
    @dev Index values can be found via the `underlying_coins` public getter method
    @param am_myusd Amount of myUSD being exchanged
    @param token_index Index value of the underlying stablecoin to recieve
    @return Actual amount of `token_index` received
    """
    myusd.approve(swap,am_myusd,params)

    input("Press Enter to continue...")
    swap.exchange_underlying(0,token_index,am_myusd,0,params)

def main():
    #Swap myUSD for USDC
    allowAndSwap(10000*10**6,2)
