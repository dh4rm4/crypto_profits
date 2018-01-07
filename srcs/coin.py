#!/usr/bin/py3
"""
COIN OBJECT
"""

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

    def add_order(self, order):
        """
        Add an order in a COIN
        """
        self.orders.append(order)
        self.total_value += order.total_value
        self.total_earn += order.value_earn
        self.total_possess += order.number

    def write_logs_in_files(self, filename, value):
        """
        Write value in the specify file as logs
        for future stats tools
        """

    def print_crypto_stats(self):
        print (self.symbol + ': ' + str(self.current_price))
