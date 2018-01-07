#!/usr/bin/python3
"""
Main file to start the program
"""


from srcs.fetch_coins_infos import fetch_coins_from_file, coinmarket_infos
from srcs.total_stats import total_stats
from srcs.coin_order import coin_order
from srcs.coin import crypto_currency


def collect_orders_coins_infos(orders_list):
    coin_dict = {}
    for order_infos in orders_list:
        # Parse / get local and live infos on coins
        name, number, purchase_price = order_infos.replace('\n', '').split(';')
        market_infos = coinmarket_infos(name)
        market_infos.get_value()

        # Manage stats
        order_stats = coin_order(name,
                                 market_infos.symbol,
                                 float(purchase_price),
                                 float(market_infos.current_price),
                                 float(number),
                                 market_infos.coin_rank)
        order_stats.profits_calc()
        if order_stats.name not in coin_dict:
            coin_dict[order_stats.name] = crypto_currency(order_stats)
        else:
            coin_dict[order_stats.name].add_order(order_stats)

    # PRINT
    for coin in coin_dict.items():
        coin[1].print_crypto_stats()
#        coin_dict[coin].print_coin_stats()


def release_the_beast():
    """
    Do the dirty work
    """
    orders_list = fetch_coins_from_file()
    collect_orders_coins_infos(orders_list)
