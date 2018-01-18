class col:
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def output_color(positif_evol):
    print (col.BOLD, end='')
    if positif_evol is True:
        print (col.OKGREEN, end='')
    else:
        print (col.FAIL, end='')


def tmp_output(coin):
    """
    USED ONLY FOR DEV
    """
    print (col.UNDERLINE +
           col.YELLOW +
           coin.symbol +
           col.ENDC +
           ':  ', end='')
    print ('Rank: ' + str(coin.rank) + col.ENDC, end='')
    print ('\t->  ' + col.BOLD + str(coin.current_price) + '€' + col.ENDC)
    i = 0
    for order in coin.orders:
        i += 1
        print ('#' + str(i) + ': ', end='')
        output_color(order.positif_evol)
        print (str(round(order.value_earn, 2)) + '€' + col.ENDC, end='')
        print ('\t->\t', end='')
        output_color(order.positif_evol)
        print (str(round(order.percent_earn, 2)) + '%' + col.ENDC)

    if i > 1:
        print ('Total Value: ' + str(round(coin.total_value, 2)))
        print ('Total Earn: ' + str(round(coin.total_earn, 2)))
    print ('')

def tmp_print_total(total_earn, total_value):
    print (col.BLUE +
           col.BOLD +
           col.UNDERLINE +
           'TOTAL EARN:' +
           col.ENDC, end='')
    if total_earn > 0:
        print (col.OKGREEN, end='')
    else:
        print (col.FAIL, end='')
    print ('  ' + str(round(total_earn, 2)) + col.ENDC + '€')

    print (col.BLUE +
           col.BOLD +
           col.UNDERLINE +
           'TOTAL VALUE:' +
           col.ENDC +
           col.BOLD, end='')
    print (' ' + str(round(total_value, 2)) + col.ENDC + col.ENDC)
