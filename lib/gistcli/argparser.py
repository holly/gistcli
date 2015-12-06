#!/usr/bin/env python
# vim:fileencoding=utf-8

from argparse import ArgumentParser, FileType
import time
import warnings
import os, sys, io
import signal

class ArgParser(object):

    def __init__(self, description, version):

        self.__description = description
        self.__version     = version
        self.__parser      = None

        self.__initialized()

    @property
    def description(self):
        return self.__description

    @property
    def version(self):
        return self.__version

    @property
    def parser(self):
        return self.__parser

    def print_help(self):
        self.__parser.print_help()

    def args(self):
        return self.__parser.parse_args()


    def __initialized(self):

        parser = ArgumentParser(description=self.description)
        parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + self.version)

        subparsers = parser.add_subparsers(help='sub-command help', dest='subparser_name')

        list_parser = subparsers.add_parser('list', help='list help')
        list_parser.add_argument('--user', '-u', action='store', metavar='USER', help='github your account name')
        list_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token, if you want private gist')
        list_parser.add_argument('--number', '-n', action='store_true', help='number of your gists')
        list_parser.add_argument('--no-headers', action='store_true', help='print no header line at all')
        list_parser.add_argument('--verbose', action='store_true', help='verbose output')

        show_parser = subparsers.add_parser('show', help='show help')
        show_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token, if you want private gist')
        show_parser.add_argument('--id', '-I', action='store', required=True, metavar='ID', help='gist id')
        show_parser.add_argument('--verbose', action='store_true', help='verbose output')

        fetch_parser = subparsers.add_parser('fetch', help='fetch help')
        fetch_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token, if you want private gist')
        fetch_parser.add_argument('--id', '-I', action='store', required=True, metavar='ID', help='gist id')
        fetch_parser.add_argument('--download-dir', '-d', action='store', metavar='DOWNLOAD_DIR', help='download directory')
        fetch_parser.add_argument('--type', '-t', action='store', default="git", metavar='DOWNLOAD_TYPE', choices=['git', 'tarball', 'zip'], help='gistfetch download type(default:git. other type are tarball and zip)')
        fetch_parser.add_argument('--verbose', action='store_true', help='verbose output')

        post_parser = subparsers.add_parser('post', help='post help')
        post_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token')
        post_parser.add_argument('--name', '-n', action='store', metavar='FILE_NAME', help='gist file name')
        post_parser.add_argument('--description', '-d', action='store', metavar='DESCRIPTION', help='gist file description')
        post_parser.add_argument('--private', '-p', action='store_true', help='private gist')
        post_parser.add_argument('--verbose', action='store_true', help='verbose output')
        post_parser.add_argument('infile', type=FileType("r"), nargs="*", default=sys.stdin, metavar='INFILE', help='post target file or stdin data')

        update_parser = subparsers.add_parser('update', help='update help')
        update_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token')
        update_parser.add_argument('--id', '-I', action='store', required=True, metavar='ID', help='gist id')
        update_parser.add_argument('--name', '-n', action='store', metavar='FILE_NAME', help='gist file name')
        update_parser.add_argument('--description', '-d', action='store', metavar='DESCRIPTION', help='gist file description')
        update_parser.add_argument('--private', '-p', action='store_true', help='private gist')
        update_parser.add_argument('--verbose', action='store_true', help='verbose output')
        update_parser.add_argument('infile', type=FileType("r"), nargs="*", default=sys.stdin, metavar='INFILE', help='update target file or stdin data')

        delete_parser = subparsers.add_parser('delete', help='delete help')
        delete_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token')
        delete_parser.add_argument('--id', '-I', action='store', required=True, metavar='ID', help='gist id')
        delete_parser.add_argument('--verbose', action='store_true', help='verbose output')

        #show_from_name_parser = subparsers.add_parser('show_from_name', help='show_from_name help')
        #show_from_name_parser.add_argument('--user', '-u', action='store', metavar='USER', help='github your account name')
        #show_from_name_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token, if you want private gist')
        #show_from_name_parser.add_argument('--name', '-n', action='store', required=True, metavar='FILE_NAME', help='gist file name')
        #show_from_name_parser.add_argument('--verbose', action='store_true', help='verbose output')
        #
        #fetch_from_name_parser = subparsers.add_parser('fetch_from_name', help='fetch_from_name help')
        #fetch_from_name_parser.add_argument('--user', '-u', action='store', metavar='USER', help='github your account name')
        #fetch_from_name_parser.add_argument('--auth-token', '-T', action='store', metavar='AUTH_TOKEN', help='your github api access token, if you want private gist')
        #fetch_from_name_parser.add_argument('--name', '-n', action='store', required=True, metavar='FILE_NAME', help='gist file name')
        #fetch_from_name_parser.add_argument('--output', '-o', type=FileType('w'), metavar='FILE_NAME', help='write to FILE instead of stdout')
        #fetch_from_name_parser.add_argument('--remote-name', '-O', action='store_true', help='write output to a file named as the remote file')
        #fetch_from_name_parser.add_argument('--add-executable', '-x', action='store_true', help='add executable mode. enable --output or --remote-name option')
        #fetch_from_name_parser.add_argument('--verbose', action='store_true', help='verbose output')

        #args = parser.parse_args()
        self.__parser = parser

