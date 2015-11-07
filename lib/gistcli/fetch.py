#!/usr/bin/env python
# vim:fileencoding=utf-8

from datetime import datetime
import pprint
import time
import warnings
import os, sys, io
import stat
import re
import gistcli.show 

class Cli(gistcli.show.Cli):

    def execute(self):

        gist = self.gist_single_from_name()
        content = self.content_from_gist(gist)

        path = None
        if self.args.remote_name:
            path = gist['filename']
            with open(path, 'w') as f:
                f.write(content)
        elif self.args.output:
            path = self.args.output.name
            self.args.output.write(content)
            self.args.output.close()
        else:
            raise Exception("must be specified the option -O( --remote-name) or -o( --output=)FILE_NAME")

        self.add_executable(path)

    def add_executable(self, path, force=False):

        if self.args.add_executable or force is True:
            st = os.stat(path)
            # see http://docs.python.jp/3.4/library/stat.html
            #os.chmod(path, st.st_mode|stat.S_IEXEC)
            os.chmod(path, st.st_mode|stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH)

