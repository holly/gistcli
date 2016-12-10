#!/usr/bin/env python
# vim:fileencoding=utf-8

import pprint
import time
import warnings
import os, sys, io
import re
from gistcli.skel import Skel

class Cli(Skel):

    GIST_API_URL = 'https://api.github.com/users/%s/gists'
    # ex: <https://api.github.com/gists?page=4>; rel="next", <https://api.github.com/gists?page=100>; rel="last", <https://api.github.com/gists?page=1>; rel="first", <https://api.github.com/gists?page=2>; rel="prev"
    LINK_COMPILE_PETTERN = re.compile("^<(.*)>; rel=\"next\".*")
    LINE_FORMAT = "{id:<36}{name:<36}{status:<10}{language:12}{created:<24}{updated}"

    def execute(self):
        
        stack = self.gist_stack()
        stack_header = {"id": "ID", "name": "NAME", "status": "STATUS", "language": "LANGUAGE", "created": "CREATED", "updated": "UPDATED"}

        if self.args.number:
            print(len(stack))
            return

        if not self.args.no_headers:
            print(self.__class__.LINE_FORMAT.format(**stack_header))

        for gist in stack:
            print(self.__class__.LINE_FORMAT.format(**gist))


    def gist_stack(self, url=None):

        # list gits
        if url is None:
            url = self.__class__.GIST_API_URL % self.args.user

        stack = []

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
                    # recursive execution
                    next_url = m.group(1)
                    self.verbose_message("gist_list recursive execution:{0}".format(next_url))
                    time.sleep(1)
                    stack.extend(self.gist_stack(url=next_url))

        gists = self.json_loads(body)
        for gist in gists:
            for key in gist['files']:
                status = "Public" if gist['public'] is True else "Private"
                language = gist['files'][key]['language'] if gist['files'][key]['language'] is not None else "Text"
                gist_info = {
                        'id'       : gist['id'],
                        'name'     : gist['files'][key]['filename'],
                        'status'   : status,
                        'language' : language,
                        'created'  : gist['created_at'],
                        'updated'  : gist['updated_at'],
                    }
                stack.append(gist_info)
        return stack

