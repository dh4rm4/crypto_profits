#!/usr/bin/python3
"""
FETCH ALL COINS INFO FROM LOCAL FILE AND
coinmarketcap.com FOR LIVE INFOS
"""

import json
import requests
from traceback import format_exc


def fetch_coins_from_file():
    """
    Open the file coins.txt.
    It must have the hierachy:
    fullname_coin;symbol;number_possessed;purchase_price

    Ex:
    ripple;xrp;420;0.42;gitlab.loc/boid/logs_repository_url.git
    """
    try:
        coins_list = list()
        f = open('coins.txt', 'r')
        for line in f:
            coins_list.append(line)
        return sorted(coins_list)

    except Exception as err:
        print ('Error when opening coins.txt: ', err)
        print (format_exc())
        exit()


class get_live_coin_infos(object):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.coin_rank = -42
        self.current_price = float()

    def get_infos(self):
        coinmarketcap_values = coinmarketcap_infos(self.name)
        coinmarketcap_values.get_values()

        coincap_values = coincap_infos(self.name, self.symbol)
        coincap_values.get_values()
        self.get_the_average_price(coinmarketcap_values, coincap_values)

    def get_the_average_price(self, coinmarketcap, coincap_values):
        self.current_price = (coinmarketcap.current_price + coincap_values.current_price) / 2


class coinmarketcap_infos(object):
    """
    Get and store live infos from coinmarketcap.com
    """
    def __init__(self, name):
        self.name = name
        self.symbol = str()
        self.coin_rank = int()
        self.current_price = float()

    def get_values(self):
        """
        Get last infos about coin
        """
        try:
            url = 'https://api.coinmarketcap.com/v1/ticker/' + \
                  self.name + \
                  '/?convert=EUR'
            rep = requests.get(url)
            self.store_infos(rep.json()[0])

        except Exception as err:
            print ('Error when calling API: ', err)
            print (format_exc())
            exit()

    def store_infos(self, infos):
        self.symbol = infos['symbol']
        self.coin_rank = int(infos['rank'])
        self.current_price = float(infos['price_eur'])


class coincap_infos(object):
    """
    Get and store live infos from coinmarketcap.com
    """
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol.upper()
        self.current_price = float()

    def get_values(self):
        """
        Get last infos about coin
        """
        try:
            url = 'http://coincap.io/page/' + self.symbol
            rep = requests.get(url)
            self.store_infos(rep.json())

        except Exception as err:
            print ('Error when calling API: ', err)
            print (format_exc())
            exit()

    def store_infos(self, infos):
        """
        Store price infos in object from coinCap data or
        make conversion from USD to EUR
        """
        if 'price_eur' in infos:
            self.current_price = float(infos['price_eur'])
        else:
            self.current_price = self.get_usd_to_eur_conversion(infos['price_usd'])

    def get_usd_to_eur_conversion(self, price_usd):
        """
        Make the price conversion from USD to EUR
        via exchange rate from European Central Bank data
        """
        currencies_exchange_rate = requests.get('http://api.fixer.io/latest?base=USD')
        usd_to_eur_rate = currencies_exchange_rate.json()['rates']['EUR']
        return (price_usd * usd_to_eur_rate)
