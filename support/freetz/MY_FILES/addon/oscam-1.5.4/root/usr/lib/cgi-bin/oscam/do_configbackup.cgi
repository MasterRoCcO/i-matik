#!/bin/sh
# include environment variables
[ -r /var/env.cache ] && . /var/env.cache
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

fname=$(echo oscam$(date '+_%Y-%m-%d_%H%M_settings.tgz') | tr ' !' '_.')
CR=$'\r'
echo "Content-Type: application/x-gzip${CR}"
echo "Content-Disposition: attachment; filename=\"$fname\"${CR}"
echo "${CR}"

exec 3>&1 > /dev/null 2>&1

cd /var/tmp

BACKUP_DIR='addon_oscam'
rm -rf $BACKUP_DIR
mkdir $BACKUP_DIR

OSC_FILES='oscam.ac oscam.cacheex oscam.cert oscam.conf oscam.dvbapi oscam.guess oscam.ird oscam.provid oscam.server oscam.services oscam.srvid oscam.tiers oscam.user oscam.whitelist *css '

for file in $OSC_FILES; do
	DIRLIST=$(ls $WORKING_DIR/$file)
	for fpath in $DIRLIST; do
		name=${fpath##*/}
		cat $WORKING_DIR/$name > $BACKUP_DIR/$name
	done
done

tar cz $BACKUP_DIR/ >&3

rm -rf $BACKUP_DIR
