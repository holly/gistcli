gistcli
===========

gist command line interface

# usage

## help

```shell
usage: gistcli [-h] [--version]
               {list,show,fetch,show_from_name,fetch_from_name,post,update,delete}
               ...

gist command line interface

positional arguments:
  {list,show,fetch,show_from_name,fetch_from_name,post,update,delete}
                        sub-command help
    list                list help
    show                show help
    fetch               fetch help
    show_from_name      show_from_name help
    fetch_from_name     fetch_from_name help
    post                post help
    update              update help
    delete              delete help

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit

```


## sub-command

### list

```shell
usage: gistcli list [-h] [--user USER] [--auth-token AUTH_TOKEN] [--number]
                    [--no-headers] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  github your account name
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token, if you want private gist
  --number, -n          number of your gists
  --no-headers          print no header line at all
  --verbose             verbose output
```

*execute*

```shell
$ gistcli list -u holly 
```

*result*

```shell
ID                      NAME                                STATUS    LANGUAGE    CREATED                 UPDATED
e3ef09ae9551d425eb77    virus-alert.sh                      Public    Shell       2015-09-26T13:22:20Z    2015-09-26T13:24:11Z
0b3c96d3795957bfb1f5    save_drbd_status.sh                 Public    Shell       2015-06-28T13:27:35Z    2015-08-29T14:23:52Z
0b3c96d3795957bfb1f5    ctrl_drbd.sh                        Public    Shell       2015-06-28T13:27:35Z    2015-08-29T14:23:52Z
0b3c96d3795957bfb1f5    check_drbd.sh                       Public    Shell       2015-06-28T13:27:35Z    2015-08-29T14:23:52Z
2ab5b1763c5563debd5e    make-cert.pl                        Public    Perl        2015-04-19T03:36:04Z    2015-08-29T14:19:28Z
aa18fd518be1205f2753    Check server                        Public    Text        2015-03-09T04:06:15Z    2015-08-29T14:16:48Z
6c53b06a5fcae36b4edd    getswap.sh                          Public    Shell       2014-12-03T03:34:57Z    2015-08-29T14:10:42Z
42ecbce38f0a7c07daa6    redis-sentinel-failover.sh          Public    Shell       2014-11-30T14:15:10Z    2015-08-29T14:10:33Z
53f39016625c18498c26    arch-chroot-script.sh               Public    Shell       2014-10-19T15:24:29Z    2015-08-29T14:07:52Z
8094562                 tumblr-recent-posts.js              Public    JavaScript  2013-12-23T10:14:41Z    2015-08-29T13:54:40Z
6977416                 pgpool_follow_master.sh             Public    Shell       2013-10-14T15:25:15Z    2015-08-29T13:52:39Z
6958260                 pgpool_remote_start                 Public    Shell       2013-10-13T04:40:16Z    2015-08-29T13:52:38Z

... and more ...
```

### show

```shell
usage: gistcli show [-h] [--auth-token AUTH_TOKEN] --id ID [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token, if you want private gist
  --id ID, -I ID        gist id
  --verbose             verbose output
```

[check_drbd.sh](https://gist.github.com/holly/0b3c96d3795957bfb1f5 "check_drbd.sh")

| option     | value       |
|:-----------|:------------|
| id         | 0b3c96d3795957bfb1f5 |
| file name  | check_drbd.sh        |

*execute*

```shell
$ gistcli show --id 0b3c96d3795957bfb1f5
```

*result*

```shell
##### check_drbd.sh #####
#!/bin/bash

EXIT_CODE=0

STATUS_FILE=/tmp/drbd.status

STATUS=$(sed -e 's/.* state:\(.*\)$/\1/' $STATUS_FILE)
if [ "${STATUS}" != "MASTER" ]; then
        echo "current status is ${STATUS}. skip"
        exit
fi

DRBD_ROLE_STATUS=$(/sbin/drbdadm role r0 | cut -d '/' -f1)
DRBD_DSTATE_STATUS=$(/sbin/drbdadm dstate r0 | cut -d '/' -f1)
DRBD_CSTATE_STATUS=$(/sbin/drbdadm cstate r0)

[ "${DRBD_ROLE_STATUS}" != "Primary" ] && EXIT_CODE=1
#[ "${DRBD_DSTATE_STATUS}" != "UpToDate" ] && EXIT_CODE=2
#[ "${DRBD_CSTATE_STATUS}" != "Connected" ] && EXIT_CODE=3

echo "$(date +'%Y/%m/%d %H:%M:%S') check_drbd role:${DRBD_ROLE_STATUS} dstate:${DRBD_DSTATE_STATUS} cstate:${DRBD_CSTATE_STATUS} exit:${EXIT_CODE}" >> /tmp/check_drbd.log

exit $EXIT_CODE
```

### fetch

```shell
usage: gistcli fetch [-h] [--auth-token AUTH_TOKEN] --id ID
                     [--download-dir DOWNLOAD_DIR] [--type DOWNLOAD_TYPE]
                     [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token, if you want private gist
  --id ID, -I ID        gist id
  --download-dir DOWNLOAD_DIR, -d DOWNLOAD_DIR
                        download directory
  --type DOWNLOAD_TYPE, -t DOWNLOAD_TYPE
                        gistfetch download type(default:git. other type are
                        tarball and zip)
  --verbose             verbose output
```

*execute*

```shell
$ gistcli fetch --id 0b3c96d3795957bfb1f5
```

*result*

```shell
$ ls -Al 0b3c96d3795957bfb1f5/
total 12
drwxrwxr-x 8 holly holly 152 Nov 12 17:05 .git
-rw-rw-r-- 1 holly holly 743 Nov 12 17:05 check_drbd.sh
-rw-rw-r-- 1 holly holly 614 Nov 12 17:05 ctrl_drbd.sh
-rw-rw-r-- 1 holly holly 270 Nov 12 17:05 save_drbd_status.sh
```

*execute(type is tarball)*

```shell
$ gistcli fetch --id 0b3c96d3795957bfb1f5 -t tarball
```

*result*

```shell
$ ls -Al 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24.tar.gz
-rw-rw-r-- 1 holly holly 995 Nov 12 17:06 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24.tar.gz

$ tar tvfz 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24.tar.gz
drwxrwxr-x root/root         0 2015-06-28 22:27 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24/
-rw-rw-r-- root/root       743 2015-06-28 22:27 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24/check_drbd.sh
-rw-rw-r-- root/root       614 2015-06-28 22:27 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24/ctrl_drbd.sh
-rw-rw-r-- root/root       270 2015-06-28 22:27 0b3c96d3795957bfb1f5-bb8ef3979efab34ab9ed44d2edfa57944a7c9c24/save_drbd_status.sh
```

### show_from_name

```shell
usage: gistcli show_from_name [-h] [--user USER] [--auth-token AUTH_TOKEN]
                    [--no-headers] --name FILE_NAME [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  github your account name
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token, if you want private gist
  --no-headers          print no header line at all
  --name FILE_NAME, -n FILE_NAME
                        gist file name
  --verbose             verbose output
```


[check_drbd.sh](https://gist.github.com/holly/0b3c96d3795957bfb1f5 "check_drbd.sh")

| option     | value       |
|:-----------|:------------|
| user       | holly       |
| file name  | check_drbd.sh |

*execute*

```shell
$ gistcli show_from_name -u holly -n check_drbd.sh
```

*result*

```shell
#!/bin/bash

EXIT_CODE=0

STATUS_FILE=/tmp/drbd.status

STATUS=$(sed -e 's/.* state:\(.*\)$/\1/' $STATUS_FILE)
if [ "${STATUS}" != "MASTER" ]; then
        echo "current status is ${STATUS}. skip"
        exit
fi

DRBD_ROLE_STATUS=$(/sbin/drbdadm role r0 | cut -d '/' -f1)
DRBD_DSTATE_STATUS=$(/sbin/drbdadm dstate r0 | cut -d '/' -f1)
DRBD_CSTATE_STATUS=$(/sbin/drbdadm cstate r0)

[ "${DRBD_ROLE_STATUS}" != "Primary" ] && EXIT_CODE=1
#[ "${DRBD_DSTATE_STATUS}" != "UpToDate" ] && EXIT_CODE=2
#[ "${DRBD_CSTATE_STATUS}" != "Connected" ] && EXIT_CODE=3

echo "$(date +'%Y/%m/%d %H:%M:%S') check_drbd role:${DRBD_ROLE_STATUS} dstate:${DRBD_DSTATE_STATUS} cstate:${DRBD_CSTATE_STATUS} exit:${EXIT_CODE}" >> /tmp/check_drbd.log

exit $EXIT_CODE
```

### fetch_from_name

```shell
usage: gistcli fetch_from_name [-h] [--user USER] [--auth-token AUTH_TOKEN] --name
                     FILE_NAME [--output FILE_NAME] [--remote-name]
                     [--add-executable] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  github your account name
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token, if you want private gist
  --name FILE_NAME, -n FILE_NAME
                        gist file name
  --output FILE_NAME, -o FILE_NAME
                        write to FILE instead of stdout
  --remote-name, -O     write output to a file named as the remote file
  --add-executable, -x  add executable mode. enable --output or --remote-name
                        option
  --verbose             verbose output
```

*execute*

```shell
$ gistcli fetch -u holly -n check_drbd.sh -O 
```

*result*
```shell
$ ls -Al check_drbd.sh
-rwxr-xr-x 1 holly holly 645 Sep 23 14:00 check_drbd.sh
```

### execute

```shell
usage: gistcli exec [-h] [--user USER] [--auth-token AUTH_TOKEN] --name
                    FILE_NAME [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  github your account name
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token, if you want private gist
  --name FILE_NAME, -n FILE_NAME
                        gist file name
  --verbose             verbose output
```

*execute*

```shell
$ gistcli exec -u holly -n check_drbd.sh 
# display check_drbd.sh execute result
```

### post

```shell
usage: gistcli post [-h] [--user USER] [--auth-token AUTH_TOKEN] --name
                    FILE_NAME [--description DESCRIPTION] [--private]
                    [--verbose]
                    [INFILE]

positional arguments:
  INFILE                post target file or stdin data

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  github your account name
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token
  --name FILE_NAME, -n FILE_NAME
                        gist file name
  --description DESCRIPTION, -d DESCRIPTION
                        gist file description
  --private, -p         private gist
  --verbose             verbose output
```

*execute*

```shell
# from stdin
$ gistcli post -u holly -n test.txt <test.txt
# or from file
$ gistcli post -u holly -n test.txt test.txt
```

*result*
```shell
# unique id
0b436445dbc534beca38
```

### update

```shell
usage: gistcli update [-h] [--auth-token AUTH_TOKEN] --id ID
                      [--name FILE_NAME] [--description DESCRIPTION]
                      [--private] [--verbose]
                      [INFILE [INFILE ...]]

positional arguments:
  INFILE                update target file or stdin data

optional arguments:
  -h, --help            show this help message and exit
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token
  --id ID, -I ID        gist id
  --name FILE_NAME, -n FILE_NAME
                        gist file name
  --description DESCRIPTION, -d DESCRIPTION
                        gist file description
  --private, -p         private gist
  --verbose             verbose output
```

*execute*

```shell
# from stdin
$ gistcli update -u holly -n test.txt <test.txt
# or from file
$ gistcli update -u holly -n test.txt test.txt
```

*result*
```shell
# unique id
0b436445dbc534beca38
```

### delete

```shell
usage: gistcli delete [-h] [--user USER] [--auth-token AUTH_TOKEN] --id ID
                      [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  github your account name
  --auth-token AUTH_TOKEN, -T AUTH_TOKEN
                        your github api access token
  --id ID, -I ID        gist id
  --verbose             verbose output
```

*execute*

```shell
$ gistcli delete -u holly --id 0b436445dbc534beca38
```

# install

## pip install

```python
$ pip install gistcli
```

## setup.py option

### build

```
$ python setup.py build
```

### cleanup

```
$ python setup.py clean --all
```

# License

MIT.

