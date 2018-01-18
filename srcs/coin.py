#!/usr/bin/py3
"""
COIN OBJECT
"""

from os.path import isdir
from datetime import datetime

class crypto_currency(object):
    """
    Store all infos on specific coin
    based on orders
    """

    def __init__(self, order):
        self.name = order.name
        self.symbol = order.symbol
        self.rank = order.coin_rank

        self.orders = [order]
        self.current_price = order.curr_price
        self.total_value = order.total_value
        self.total_earn = order.value_earn
        self.total_possess = order.number

    def get_logs_directory_path(self, git_url):
        path = './stats/'
        path += git_url.split('/')[-1].replace('.git', '')
        path += '/'
        return path

    def add_order(self, order):
        """
        Add an order in a COIN
        """
        self.orders.append(order)
        self.total_value += order.total_value
        self.total_earn += order.value_earn
        self.total_possess += order.number
