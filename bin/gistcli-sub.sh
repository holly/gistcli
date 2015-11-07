#!/bin/sh

set -e

ORIGIN=gistcli

subcommand=$(echo "$(basename $0)" | sed -e 's/^gist//')


command="$(dirname $0)/$ORIGIN $subcommand $@"

exec $command 
