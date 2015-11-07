#!/usr/bin/env python
# vim:fileencoding=utf-8

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

def find_scripts(scripts_path):
    base_path = os.path.abspath(scripts_path)
    return list(map(lambda path: os.path.join(scripts_path, path), 
           filter(lambda file_name: os.path.isfile(
             os.path.join(base_path, file_name)), os.listdir(base_path)
         )))

import os, sys

bindir = "bin"
libdir = "lib"

import info
import version

setup_options = info.INFO
setup_options["version"] = version.VERSION
setup_options.update(dict(
#  install_requires = open('requirements.txt').read().splitlines(),
  scripts          = find_scripts(bindir),
  packages         = find_packages(libdir),
  package_dir      = { "": libdir },
))

setup(**setup_options)
