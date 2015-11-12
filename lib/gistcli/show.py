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

    def execute(self):

        gist = self.gist_single()
        self.content_from_gist(gist)

    def gist_single(self, url=None):
        # list gits
        if url is None:
            url = self.__class__.GIST_API_URL.format(self.args.id)

        self.verbose_message("request url:{0}".format(url))

        res = self.make_response(url)
        headers = res.getheaders()
        body    = res.read().decode("utf-8")

        return self.json_loads(body)

    def content_from_gist(self, gist):


        for key in gist["files"]:
            filename = gist["files"][key]["filename"]
            content = gist["files"][key]["content"]

            
            print("##### {0} #####".format(filename))
            print(content)
            print()

