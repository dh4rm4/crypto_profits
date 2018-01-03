#!/usr/bin/python3

from traceback import format_exc
import requests
import json


class col:
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class print_total_stats(object):
    """
    Final output of all stats
    """
    def __init__(self, total_value, total_earn):
        self.total_value = total_value
        self.earn = total_earn

    def print_total_value(self):
        print (col.BLUE +
               col.BOLD +
               col.UNDERLINE +
               'TOTAL VALUE:' +
               col.ENDC +
               col.BOLD, end='')
        print (' ' + str(round(self.total_value, 2)) + col.ENDC + col.ENDC)

    def print_total_earn(self):
        print (col.BLUE +
               col.BOLD +
               col.UNDERLINE +
               'TOTAL EARN:' +
               col.ENDC, end='')
        if self.earn > 0:
            print (col.OKGREEN, end='')
        else:
            print (col.FAIL, end='')
        print ('  ' + str(round(self.earn, 2)) + col.ENDC + '$')


class coins(object):
    """
    Coin object to store coin infos
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
        self.total_value = self.number * self.curr_price

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
        if self.positif_evol is True:
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
        print (str(round(self.value_earn, 2)) + '$', end='')
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
        try:
            url = 'https://api.coinmarketcap.com/v1/ticker/' + self.name
            rep = requests.get(url)
            self.store_infos(rep.json()[0])

        except Exception as err:
            print ('Error when calling API: ', err)
            print (format_exc())
            exit()

    def store_infos(self, infos):
        self.symbol = infos['symbol']
        self.rank = infos['rank']
        self.current_price = infos['price_usd']


def get_coins_from_files():
    """
    Open the file coins.txt.
    It must have the hierachy:
    fullname_coin;number_possessed;purchase_price

    Ex:
    ripple;420;0.42
    """
    try:
        coins_list = list()
        f = open('coins.txt', 'r')
        for line in f:
            coins_list.append(line)
        return coins_list

    except Exception as err:
        print ('Error when opening coins.txt: ', err)
        print (format_exc())
        exit()


def release_the_beast():
    """
    Do the dirty work
    """
    coins_list = get_coins_from_files()
    format_coins = ()
    total_earn = 0
    total_value = 0
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
        total_earn += coin_stats.value_earn
        total_value += coin_stats.total_value
    p = print_total_stats(total_value, total_earn)
    p.print_total_value()
    p.print_total_earn()

if __name__ in '__main__':
    release_the_beast()
