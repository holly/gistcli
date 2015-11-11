#!/usr/bin/env python
# vim:fileencoding=utf-8

from datetime import datetime
import pprint
import time
import warnings
import os, sys, io
import re
import subprocess
import gistcli.show 

class Cli(gistcli.show.Cli):

    GIT_CMD = '/usr/bin/git'

    def content_from_gist(self, gist):

        cmd = [ self.__class__.GIT_CMD, "clone", gist["git_pull_url"]]
        if self.args.download_dir:
            cmd.append(self.args.download_dir)
        subprocess.check_call(cmd)

