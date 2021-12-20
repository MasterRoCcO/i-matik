#!/bin/sh

PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
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

WATCHDOG_LOG_PATH="$OSCAM_PATH/addon/watchdog/"
WATCHDOG_LOG="$WATCHDOG_LOG_PATH/watchdog.log"

cgi --id=conf:oscam:_index
cgi_begin '$(lang de:"Watchdog-Log" en:"Watchdog Log")'

echo '<h1>$(lang de:"Watchdog-LOG-Datei" en:"Watchdog LOG file")</h1>'

if [ -e "$WATCHDOG_LOG" ]; then 
    echo '<pre class="log full">'"$(cat "$WATCHDOG_LOG")"'</pre>'
else
    echo '<p>$(lang de:"LOG-Datei in <b>\'$WATCHDOG_LOG_PATH\'</b> nicht verf&uuml;gbar" en:"LOG file not availbale in <b>\'$WATCHDOG_LOG_PATH\'</b>")</p>'
fi

#echo '<p><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form></p>'
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'


cgi_end
