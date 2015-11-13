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

    GIST_API_URL         = 'https://api.github.com/gists'
    HTTP_REQUEST_HEADERS = { "Accept": "application/json", "Content-Type": "application/json" }
    INVALID_MESSAGE      = "invalid-email-address"

    def execute(self):

        id = self.gist_post()
        print(id)

    def gist_post(self):

        public = True
        url    = self.__class__.GIST_API_URL
        self.verbose_message("request url:{0}".format(url))

        if self.args.private:
            public = False

        # make payload
        payload = { "public": public }

        if isinstance(self.args.infile, list):
            # from file list
            files= {}
            for f in self.args.infile:
                files[os.path.basename(f.name)] = { "content": f.read() }
            payload["files"] = files
        else:
            # from stdin
            if not self.args.name :
                raise Exception("error: the following arguments are required: --name/-n")
            payload["files"] = { self.args.name: { "content": self.args.infile.read() }}

        if self.args.description:
            payload["description"] = self.args.description

        json_data = self.json_dumps(payload)
        self.verbose_message(json_data)

        res = self.make_response(url, headers=self.__class__.HTTP_REQUEST_HEADERS, data=json_data)
        headers = res.getheaders()
        body    = res.read().decode("utf-8")

        data = self.json_loads(body)

        history_login = data["history"][0]["user"]["login"]

        if history_login == self.__class__.INVALID_MESSAGE:
            raise Exception("history message:{0}. auth_token is invalid".format(history_login))

        return data["id"]
