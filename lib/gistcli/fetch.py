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

    GIT_CMD              = '/usr/bin/git'
    GIST_ANOTHERTYPE_URL = 'https://gist.github.com/{user}/{id}/archive/{version}.{ext}'
    EXT_TYPES            = { "zip": "zip", "tarball": "tar.gz" }

    def content_from_gist(self, gist):

        if self.args.type == "git":
            cmd = [ self.__class__.GIT_CMD, "clone", gist["git_pull_url"]]
            if self.args.download_dir:
                cmd.append(self.args.download_dir)
            self.verbose_message("execute command: {0}".format(" ".join(cmd)))
            subprocess.check_call(cmd)
        else:

            version = gist["history"][0]["version"]
            ext     = self.__class__.EXT_TYPES[self.args.type]
            filename = self.args.id + "-" + version + "." + ext

            download_fmt = { 
                        "user"    : gist["owner"]["login"],
                        "id"      : self.args.id,
                        "version" : version,
                        "ext"     : ext
                    }
            download_url = self.__class__.GIST_ANOTHERTYPE_URL.format(**download_fmt)

            self.verbose_message("download archive: {0}".format(download_url))
            res = self.make_response(download_url)

            self.verbose_message("write file: {0}".format(filename))
            with open(filename, "wb") as f:
                while True:
                    buffer = res.read(4096)
                    if not buffer: break
                    f.write(buffer)

