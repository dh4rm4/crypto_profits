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
        self.repo_obj = Repo.clone_from(self.repo_url, self.repo_path)

    def init_repository(self):
        """
        Create the repo object
        """
        self.repo_obj = Repo(self.repo_path)
        self.pull_repository()

    def index_file(self, filename):
        """
        Index filename for next commit
        """
        self.repo_obj.index([filename])

    def commit_change(self, msg):
        """
        Set message for current commit
        """
        self.repo_obj.index.commit(msg)

    def init_origin(self):
        """
        Init remote repo's origin
        """
        self.origin = self.repo_obj.remote(name='origin')

    def pull_repository(self):
        if self.origin is None:
            self.init_origin()
        self.origin.pull()

    def push_commit(self):
        if self.origin is None:
            self.init_origin()
        self.origin.push()
