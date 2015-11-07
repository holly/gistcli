#!/usr/bin/env python
# vim:fileencoding=utf-8

from datetime import datetime
import pprint
import time
import warnings
import os, sys, io
import re
from gistcli.skel import Skel

class Cli(Skel):

    GIST_API_URL         = 'https://api.github.com/gists/{0}'
    INVALID_MESSAGE      = "invalid-email-address"

    def execute(self):

        self.gist_delete()

    def gist_delete(self):

        url    = self.__class__.GIST_API_URL.format(self.args.id)
        self.verbose_message("request url:{0}".format(url))

        res = self.make_response(url, method="DELETE")
        #headers = res.getheaders()
        #body    = res.read().decode("utf-8")
