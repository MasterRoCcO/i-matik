#!/bin/sh
## NFR Freetz-Team ##

PCSCD_DIR=/usr/bin
PCSCD_CONF=/etc/pcscd.conf


start() {
    export LD_LIBRARY_PATH="/usr/lib/freetz:${LD_LIBRARY_PATH}"
    sleep 1
    ${PCSCD_DIR}/pcscd -d -f -c ${PCSCD_CONF}/reader.conf >/dev/null 2>&1   
}

stop() {
    killall -q -9 "pcscd" >/dev/null
    sleep 1
}

case "$1" in
    start)
      start
    ;;

    stop)
      stop
    ;;

    restart)
      stop
      sleep 1
      start
    ;;

esac
