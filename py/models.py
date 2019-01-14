from web3 import HTTPProvider, Web3

from pymaker import Address
from pymaker.token import ERC20Token
from pymaker.numeric import Ray
from pymaker.sai import Tub, Tap



INITIAL_INVESTMENT = 5000


class CDP(object):
    return





'''
1. fetch current $ETH price
2. set criteria of investment in either $ETH or $USD
3. initialize "lock up" of funds
4. define liquidation price based on:
    a. $ value of locked up funds,
    b. $ value withdrew from locked funds
    c. use liquidation ratio from MakerDAO
    d. define "bite" penalty
        > if "bite" happens, convert $ETH into $USD then incur the 13% bite fee.




'''
