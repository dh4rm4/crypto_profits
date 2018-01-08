#!/usr/bin/python3

from traceback import format_exc
import json
import datetime


class col:
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class total_stats(object):
    """
    Final output of all stats
    """
    def __init__(self, total_value, total_earn):
        self.total_value = total_value
        self.earn = total_earn

    def print_total_value(self):
        print (col.BLUE +
               col.BOLD +
               col.UNDERLINE +
               'TOTAL VALUE:' +
               col.ENDC +
               col.BOLD, end='')
        print (' ' + str(round(self.total_value, 2)) + col.ENDC + col.ENDC)

    def print_total_earn(self):
        print (col.BLUE +
               col.BOLD +
               col.UNDERLINE +
               'TOTAL EARN:' +
               col.ENDC, end='')
        if self.earn > 0:
            print (col.OKGREEN, end='')
        else:
            print (col.FAIL, end='')
        print ('  ' + str(round(self.earn, 2)) + col.ENDC + '$')
