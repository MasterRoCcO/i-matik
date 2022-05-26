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
DEVICE="/var/devices"

cgi --id=conf:oscam:_index
cgi_begin '$(lang de:"Serialanzeige" en:"Serialdisplay")'

echo '<h1>$(lang de:"Hier werden euch die Serial aller angeschlossenen USB-Geräte angezeigt" en:"Here you will see the series all connected USB Devices")</h1>'

if [ -e "$DEVICE" ]; then
    echo '<pre class="log full">'"$(cat "$DEVICE")"'</pre>'
fi

#echo '<p><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form></p>'
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'


cgi_end
