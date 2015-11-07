#!/usr/bin/env python
# vim:fileencoding=utf-8

from datetime import datetime
import pprint
import time
import warnings
import os, sys, io
import subprocess
import tempfile
import gistcli.fetch

class Cli(gistcli.fetch.Cli):

    def execute(self):

        self.args.add_executable = None
        gist = self.gist_single_from_name()
        content = self.content_from_gist(gist)

        (fd, path) = tempfile.mkstemp()
        os.write(fd, content.encode("utf-8"))
        os.close(fd)
        self.verbose_message("execute command {0}".format(path))
        self.add_executable(path, force=True)
        subprocess.check_call(path)
        os.remove(path)

