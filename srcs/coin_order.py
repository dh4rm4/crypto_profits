#!/usr/bin/python3
"""
COIN ORDER OBJECT
An order is all infos about a coin your purchased at
a specific time and price
"""


class col:
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class coin_order(object):
    """
    Coin object to store coin infos
    """

    def __init__(self, name, symbol, purc_value, curr_price, number, rank):
        self.name = name
        self.symbol = symbol
        self.purchase_price = float(purc_value)
        self.number = int(number)
        self.coin_rank = rank

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
        self.percent_earn = (self.curr_price / self.purchase_price) * 100 - 100
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
