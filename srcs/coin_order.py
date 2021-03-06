#!/usr/bin/python3
"""
COIN ORDER OBJECT
An order is all infos about a coin your purchased at
a specific time and price
"""


class coin_order(object):
    """
    Coin object to store coin infos
    """

    def __init__(self, name, git_url, symbol, purc_value, curr_price, number, rank):
        self.name = name
        self.symbol = symbol
        self.purchase_price = float(purc_value)
        self.number = float(number)
        self.coin_rank = rank
        self.git_url = git_url

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
