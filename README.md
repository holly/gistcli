gistcli
===========

gist command line interface

# usage

## help

```shell
usage: gistcli [-h] [--version] {list,show,fetch,exec} ...

gist command line interface

positional arguments:
  {list,show,fetch,exec}
                        sub-command help
    list                list help
    show                show help
    fetch               fetch help
    exec                fetch help

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit

```


## sub-command

### list

*execute*

```shell
$ gistcli -u holly 
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

[check_drbd.sh](https://gist.github.com/holly/0b3c96d3795957bfb1f5 "check_drbd.sh")

| option     | value       |
|:-----------|:------------|
| user       | holly       |
| file name  | check_drbd.sh |

*execute*

```shell
$ gistcli show -u holly -n check_drbd.sh
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

### fetch (with add-executable)

*execute*

```shell
$ gistcli fetch -u holly -n check_drbd.sh -O -x
```

*result*
```shell
$ ls -Al check_drbd.sh
-rwxr-xr-x 1 holly holly 645 Sep 23 14:00 check_drbd.sh
```

### execute

*execute*

```shell
$ gistcli exec -u holly -n check_drbd.sh 
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

