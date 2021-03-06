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


class coinmarket_infos(object):
    """
    Get and store live infos from coinmarketcap.com
    """
    def __init__(self, name):
        self.name = name
        self.symbol = str()
        self.coin_rank = int()
        self.current_price = float()

    def get_value(self):
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
        self.coin_rank = infos['rank']
        self.current_price = infos['price_eur']
