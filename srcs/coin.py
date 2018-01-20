#!/usr/bin/py3
"""
COIN OBJECT
"""

from os.path import isdir
from srcs.git_actions import repository
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

        # git variable for logs' repository
        self.logs_repo = None
        self.git_url = order.git_url
        self.logs_dir = self.get_logs_directory_path(order.git_url)
        self.now = self.init_date()

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

    def log_current_values(self):
        self.write_logs_in_file("total_value.log", str(round(self.total_value, 2)))
        self.write_logs_in_file("total_earn.log", str(round(self.total_earn, 2)))
        self.upload_logs('total_value.log', 'total_earn.log')


    def write_logs_in_file(self, filename, value):
        """
        Write value in the specify file as logs
        for future stats tools
        """
        try:
            if self.logs_repo is None:
                self.init_logs_repository()
            if self.valid_repo is False:
                return
            log_file_path = self.logs_dir + filename
            logs_file = open(log_file_path, 'a')
            log = self.now + ';' + value + '\n'
            logs_file.write(log)
            logs_file.close()

        except Exception as err:
            print (err)

    def init_logs_repository(self):
        """
        Check and Clone/ pull depot for logs
        if necessary
        """
        self.logs_repo = repository(self.git_url, self.logs_dir)
        if isdir(self.logs_dir) is False:
            self.valid_repo = self.logs_repo.clone_repository()
        else:
            self.valid_repo = self.logs_repo.init_repository()

    def init_date(self):
        """
        Format date for logs
        """
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")

    def upload_logs(self, f1, f2):
        self.logs_repo.index_file(f1)
        self.logs_repo.index_file(f2)
        self.logs_repo.commit_change('automatic logs update')
        self.logs_repo.push_commit()
