#!/usr/bin/env python
# vim:fileencoding=utf-8

import pprint
import time
import os, sys, io
import urllib.request
import json
from configparser import ConfigParser


class Skel(object):

    CONFIG_PATH = os.path.join(os.environ["HOME"], ".gistclirc")

    def __init__(self, args):
        
        self.__args = args

    def prepare(self):

        if not os.path.isfile(self.__class__.CONFIG_PATH):
            return

        config = ConfigParser()
        config.read_string("[root]\n" + open(self.__class__.CONFIG_PATH, "r").read())

        if self.args.user is None and "user" in config["root"]:
            self.args.user = config["root"]["user"]
        if self.args.auth_token is None and "auth_token" in config["root"]:
            self.args.auth_token = config["root"]["auth_token"]

    def execute(self):
        raise NotImplementedError("You have to inherit the gistcli.skel.Skel")

    def run(self):
        self.prepare()
        self.execute()

    def json_loads(self, data):
        return json.loads(data)

    def make_response(self, url):
        req = urllib.request.Request(url=url)
        if self.args.auth_token:
            req.add_header("Authorization", "token {0}".format(self.args.auth_token))
        res = urllib.request.urlopen(req)
        return res

    def verbose_message(self, message):
        if self.args.verbose:
            print("verbose: {0}".format(message), file=sys.stderr)

    @property
    def args(self):
        return self.__args
