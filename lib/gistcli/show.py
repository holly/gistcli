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

    GIST_API_URL = 'https://api.github.com/users/{0}/gists'
    # ex: <https://api.github.com/gists?page=4>; rel="next", <https://api.github.com/gists?page=100>; rel="last", <https://api.github.com/gists?page=1>; rel="first", <https://api.github.com/gists?page=2>; rel="prev"
    LINK_COMPILE_PETTERN = re.compile("^<(.*)>; rel=\"next\".*")

    def execute(self):

        gist = self.gist_single_from_name()
        print(self.content_from_gist(gist))

    def gist_single_from_name(self, url=None):
        # list gits
        if url is None:
            url = self.__class__.GIST_API_URL.format(self.args.user)

        next_url = None

        self.verbose_message("request url:{0}".format(url))

        res = self.make_response(url)
        headers = res.getheaders()
        body    = res.read().decode("utf-8")

        for (key, value) in headers:
            if key == 'Status' and value != "200 OK":
                self.verbose_message("body: {0}".format(body))
                raise Exception("Status: {0}".format(value))
            if key == 'Link':
                m = self.__class__.LINK_COMPILE_PETTERN.match(value)
                if m:
                    next_url = m.group(1)
                    self.verbose_message("Link header and next_url[{0}] are exists".format(next_url))

        gists = self.json_loads(body)

        for gist in gists:
            if self.args.name in gist['files']:
                return gist['files'][self.args.name]

        # recursive execution
        if next_url:
            self.verbose_message("gist_single recursive execution:{0}".format(next_url))
            time.sleep(1)
            return self.gist_single_from_name(next_url)

        # nothing
        raise Exception("user:{0} or file name:{1} is not exists".format(self.args.user, self.args.name))

    def content_from_gist(self, gist):

        raw_url = gist['raw_url']
        res = self.make_response(gist["raw_url"])
        headers = res.getheaders()
        for (key, value) in headers:
            if key == 'Status' and value != "200 OK":
                raise Exception("Status: {0}".format(value))
        return res.read().decode("utf-8")

