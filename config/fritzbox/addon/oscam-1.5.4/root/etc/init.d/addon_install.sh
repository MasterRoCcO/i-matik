#!/bin/sh
## NFR Freetz-Team ##

. /mod/etc/conf/oscam.cfg

if [ -e /var/tmp/intern ]; then
		if [ "$(mount|grep "yaffs2")" ] || [ "$(mount|grep "ubifs")" ] || [ "$(mount|grep "ext4")" ] >/dev/null; then
        OSCAM_PATH=/var/media/ftp
    else 
        OSCAM_PATH=/data
    fi
else
    if [ -z "$OSCAM_PATH" ] || [ -z "$(df|grep "$OSCAM_PATH"|grep "/dev/sd")" ]; then OSCAM_PATH="$(df|grep "/dev/sda"|awk '{print $6}'|tail -1)"; fi
fi

WORKING_DIR="$OSCAM_PATH/addon/oscam"

if [ -d "$OSCAM_PATH" ]; then
    tar -xzf /etc/addon.tar.gz -C "$OSCAM_PATH" >/dev/null
#   sleep 2
    chmod 755 "$OSCAM_PATH/addon" 2>/dev/null
    chmod 755 "$OSCAM_PATH/addon/oscam" 2>/dev/null
    chmod 755 "$OSCAM_PATH/addon/watchdog" 2>/dev/null
    chown -R root:root "$OSCAM_PATH/addon" 2>/dev/null
    if [ -e "$WORKING_DIR/oscam.conf" ]; then
        LOGFILE=$(grep -i "^logfile" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
        LOGPATH=${LOGFILE%/*}
        [ "$LOGPATH" != "syslog" ] && sed -i "/^logfile/s#$LOGPATH#$WORKING_DIR#" "$WORKING_DIR/oscam.conf"
        CSSFILE=$(grep -i "^httpcss" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
        CSSPATH=${CSSFILE%/*}
        sed -i "/^httpcss/s#$CSSPATH#$WORKING_DIR#" "$WORKING_DIR/oscam.conf"
    else
        exit 1
    fi
fi
exit 0
