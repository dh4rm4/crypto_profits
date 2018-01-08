#!/usr/bin/python3
"""
Main file to start the program
"""


from srcs.fetch_coins_infos import fetch_coins_from_file, coinmarket_infos
from srcs.total_stats import total_stats
from srcs.coin_order import coin_order
from srcs.coin import crypto_currency


def parse_order_infos(order_infos):
    """
    Parse infos from one line of coin.txt
    """
    try:
        name, nb, purchase_price, git_url = order_infos.replace('\n', '').split(';')
        return name, nb, purchase_price, git_url

    except ValueError:
        print ('Error: You did not format well coins.txt file')
        exit()


def collect_orders_coins_infos(orders_list):
    coin_dict = {}
    for order_infos in orders_list:
        # Parse / get local and live infos on coins
        name, number, purchase_price, git_url = parse_order_infos(order_infos)
        market_infos = coinmarket_infos(name)
        market_infos.get_value()

        # Manage orders stats
        order_stats = coin_order(name,
                                 git_url,
                                 market_infos.symbol,
                                 float(purchase_price),
                                 float(market_infos.current_price),
                                 float(number),
                                 market_infos.coin_rank)
        order_stats.profits_calc()

        # Store orders' stats in coin object
        if order_stats.name not in coin_dict:
            coin_dict[order_stats.name] = crypto_currency(order_stats)
        else:
            coin_dict[order_stats.name].add_order(order_stats)

    # PRINT
    for coin in coin_dict.items():
        coin[1].log_current_values()


def release_the_beast():
    """
    Do the dirty work
    """
    orders_list = fetch_coins_from_file()
    collect_orders_coins_infos(orders_list)
