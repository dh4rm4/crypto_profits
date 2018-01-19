#!/usr/bin/python3
"""
Every Actions on git repository
"""

from git import Repo, remote
from traceback import format_exc

class repository(object):
    def __init__(self, repo_url, repo_path):
        self.repo_url = repo_url
        self.repo_path = repo_path
        self.origin = None

    def clone_repository(self):
        """
        Clone the remote repo
        """
        try:
            self.repo_obj = Repo.clone_from(self.repo_url, self.repo_path)
            return True

        except Exception as err:
            print ("[-] Something happen when cloning repo.")
            print ("\tCheck URL: " + self.repo_url)
            print ("\tLogs for this coin will be ignore", end="\n\n")
            return False

    def init_repository(self):
        """
        Create the repo object
        """
        try:
            self.repo_obj = Repo(self.repo_path)
            if self.pull_repository() == True:
                return True
            return False

        except Exception as err:
            print (err)
            return False

    def index_file(self, filename):
        """
        Index filename for next commit
        """
        try:
            self.repo_obj.index.add([filename])
        except Exception as err:
            print (err)

    def commit_change(self, msg):
        """
        Set message for current commit
        """
        try:
            self.repo_obj.index.commit(msg)
        except Exception as err:
            print (err)

    def init_origin(self):
        """
        Init remote repo's origin
        """
        try:
            self.origin = self.repo_obj.remote(name='origin')
            if self.origin.exists() is False:
                self.origin = self.repo_obj.create_remote(name='origin',
                                                          url=self.repo_url)
        except Exception as err:
            print (err)

    def pull_repository(self):
        try:
            if self.origin is None:
                self.init_origin()
                self.origin.pull()
            return True

        except Exception as err:
            print ("[-] Something happen when pulling repo. Check your git conf. ")
            return False

    def push_commit(self):
        try:
            if self.origin is None:
                self.init_origin()
            self.origin.push()
        except Exception as err:
            print (err)
