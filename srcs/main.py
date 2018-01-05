#!/usr/bin/python3
"""
Main file to start the program
"""

from srcs.fetch_coins_infos import fetch_coins_from_file, coinmarket_infos
from srcs.total_stats import total_stats
from srcs.coin_order import coin_order

def release_the_beast():
    """
    Do the dirty work
    """
    coins_list = fetch_coins_from_file()
    format_coins = ()
    total_earn = 0
    total_value = 0
    for coin_info in coins_list:
        # Parse / get local and live infos on coins
        name, number, purchase_price = coin_info.replace('\n', '').split(';')
        market_infos = coinmarket_infos(name)
        market_infos.get_value()

        # Manage stats
        order_stats = coin_order(name,
                           market_infos.symbol,
                           float(purchase_price),
                           float(market_infos.current_price),
                           float(number))
        order_stats.profits_calc()
        order_stats.print_stats()
        total_earn += order_stats.value_earn
        total_value += order_stats.total_value
    stats = total_stats(total_value, total_earn)
    stats.print_total_value()
    stats.print_total_earn()
    stats.save_logs()
