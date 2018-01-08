#!/usr/bin/py3

"""
All action on a specific cryptocurrency and
the orders associate to it
"""


class col:
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class crypto_currency(object):
    """
    COIN OBJECT
    Store all infos about a coin, and the orders associate
    """
    def __init__(self, order_stats):
        self.name = order_stats.name
        self.symbol = order_stats.symbol
        self.rank = order_stats.coin_rank
        self.orders = [order_stats]
        self.total_value = order_stats.total_value
        self.total_value_earn = order_stats.value_earn
        self.curr_price = round(order_stats.curr_price, 5)

    def add_order(self, order_stats):
        self.orders.append(order_stats)
        self.total_value += order_stats.total_value
        self.total_value_earn += order_stats.value_earn

    def print_coin_stats(self):
        self.orders_print()

    def output_color(self, positif_evol):
        print (col.BOLD, end='')
        if positif_evol is True:
            print (col.OKGREEN, end='')
        else:
            print (col.FAIL, end='')

    def orders_print(self):
        """
        PRINT FUNCIONT WHEN MULTIPLE ORDERS
        FOR ONE COIN
        """
        print (col.UNDERLINE +
               col.YELLOW +
               self.symbol +
               col.ENDC +
               ':  ', end='')
        print ('Rank: ' + str(self.rank) + col.ENDC, end='')
        print ('\t->  ' + col.BOLD + str(self.curr_price) + '$' + col.ENDC)
        i = 0
        for order in self.orders:
            i += 1
            print ('#' + str(i) + ': ', end='')
            self.output_color(order.positif_evol)
            print (str(round(order.value_earn, 2)) + '$' + col.ENDC, end='')
            print ('\t->\t', end='')
            self.output_color(order.positif_evol)
            print (str(round(order.percent_earn, 2)) + '%' + col.ENDC)
        if i > 1:
            print ('Total Value: ' + str(round(self.total_value, 2)))
            print ('Total Earn: ' + str(round(self.total_value_earn, 2)))
        print ('')
