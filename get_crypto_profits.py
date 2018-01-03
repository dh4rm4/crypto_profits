#!/usr/bin/python3

from traceback import format_exc
import requests
import json


class col:
    LOWRED      = '\033[94m'
    OKGREEN     = '\033[92m'
    YELLOW      = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'


class coins(object):
    """
    Coin object to store coin info
    """

    def __init__(self, name, symbol, purc_value, curr_price, number):
        self.name = name
        self.symbol = symbol
        self.purchase_price = float(purc_value)
        self.number = int(number)

        self.curr_price = float(curr_price)
        self.value_earn = float(0)
        self.percent_earn = 0
        self.positif_evol = False

    def profits_calc(self):
        """
        Fill object with profits values
        """
        price_diff = self.curr_price - self.purchase_price
        self.percent_earn = (self.curr_price / self.purchase_price) * 100
        if price_diff > 0:
            self.positif_evol = True
        self.value_earn = price_diff * self.number

    def output_color(self):
        print (col.BOLD, end='')
        if self.positif_evol == True:
            print (col.OKGREEN, end='')
        else:
            print (col.FAIL, end='')

    def end_color(self):
        print (col.ENDC, end='')

    def print_stats(self):
        print (col.UNDERLINE +
               col.YELLOW +
               self.symbol +
               col.ENDC +
               ':  ', end='')
        self.output_color()
        print (round(self.value_earn, 2), end='')
        self.end_color()
        print ('\t->\t', end='')
        self.output_color()
        print (str(round(self.percent_earn, 2)) + '%')
        self.end_color()

class coinmarket_infos(object):
    """
    Get and store infos from coinmarketcap.com
    """
    def __init__(self, name):
        self.name = name
        self.symbol = str()
        self.rank = int()
        self.current_price = float()

    def get_value(self):
        """
        Get last infos about coin
        """
        url = 'https://api.coinmarketcap.com/v1/ticker/' + self.name
        rep = requests.get(url)
        self.store_infos(rep.json()[0])

    def store_infos(self, infos):
        self.symbol = infos['symbol']
        self.rank = infos['rank']
        self.current_price = infos['price_usd']


def get_coins_from_files():
    """
    Open the file my_coins.txt.
    It must have the hierachy:
    fullname_coin;number_possessed;purchase_price

    Ex:
    ripple;420;0.42
    """
    try:
        coins_list = list()
        f = open('my_coins.txt', 'r')
        for line in f:
            coins_list.append(line)
        return coins_list

    except Exception as err:
        print ('Error when opening my_coins.txt: ', err)
        print (format_exc())
        exit()

def release_the_beast():
    """
    Do the dirty work
    """
    coins_list = get_coins_from_files()
    format_coins = ()
    for coin_info in coins_list:
        # Parse / get local and live infos on coin
        name, number, purchase_price = coin_info.replace('\n', '').split(';')
        market_infos = coinmarket_infos(name)
        market_infos.get_value()

        # Manage stats
        coin_stats = coins(name,
                           market_infos.symbol,
                           float(purchase_price),
                           float(market_infos.current_price),
                           float(number))
        coin_stats.profits_calc()
        coin_stats.print_stats()


if __name__ in '__main__':
    release_the_beast()
