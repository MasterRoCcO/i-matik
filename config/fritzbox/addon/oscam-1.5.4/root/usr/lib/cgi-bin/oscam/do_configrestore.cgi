#!/usr/bin/haserl -u 200 -U /var/tmp
<%
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

WORKING_DIR="$OSCAM_PATH/addon/oscam"
BACKUP_DIR="addon_oscam"
TMP_DIR="/var/tmp"

cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"OSCam-Konfiguration wiederherstellen" en:"Restore OSCam configuration")'
%>
<h1>$(lang de:"Wiederherstellung" en:"Restore")</h1>
<% if [ -n "$FORM_uploadfile_name" ] && [ -z "${FORM_uploadfile_name##oscam*tgz}" ]; then %>
	<p>$(lang de:"Sie haben gerade die Datei" en:"You just uploaded the file") <b><% echo -n $FORM_uploadfile_name %></b> hochgeladen.<br>
	   $(lang de:"Die Dateigr&ouml;&szlig;e betr&auml;gt" en:"The file size is") <% cat $FORM_uploadfile | wc -c %> Bytes.<br>
	</p>
	<p><b>$(lang de:"Installationsverlauf" en:"Installation progress"):</b></p>
	<p><pre><%
		cd /var/tmp
		echo "$(lang de:"$FORM_uploadfile_name wurde im Zwischenspeicher gefunden." en:"Found $FORM_uploadfile_name in temporary memory.")"
		echo ""
		mv -f "$FORM_uploadfile" "$FORM_uploadfile_name" 2>/dev/null

		rm -rf "$BACKUP_DIR" 2>/dev/null

		echo -n "$(lang de:"Sicherungsdateien aus Archiv extrahieren ... " en:"Extracting backup files from archive ... ")"
		tar -xzf "$FORM_uploadfile_name" -C "/var/tmp" >/dev/null &
		sleep 2
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"OSCam-Konfiguration wiederherstellen ... " en:"Restoring OSCam configuration ... ")"
		for file in $(ls "$BACKUP_DIR"); do
			echo " --- $file"
			cat "$BACKUP_DIR/$file" > "$WORKING_DIR/$file"
		done
		sleep 1
		chmod 755 "$WORKING_DIR/*" 2>/dev/null
		chown -R root:root "$OSCAM_PATH/addon" 2>/dev/null
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		if [ -e "$WORKING_DIR/oscam.conf" ] && [ "$FORM_replace" = "on" ]; then
			echo -n "$(lang de:"Passe Pfad-Einstellungen in oscam.conf an ... " en:"Adapting oscam.conf path settings ... ")"
			LOGFILE=$(grep -i "^logfile" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
			LOGPATH=${LOGFILE%/*}
			[ "$LOGPATH" != "syslog" ] && sed -i "/^logfile/s#$LOGPATH#$WORKING_DIR#" "$WORKING_DIR/oscam.conf"
			CSSFILE=$(grep -i "^httpcss" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
			CSSPATH=${CSSFILE%/*}
			sed -i "/^httpcss/s#$CSSPATH#$WORKING_DIR#" "$WORKING_DIR/oscam.conf"
			echo "$(lang de:"fertig." en:"done.")"
			echo ""
		fi

		cd /var/tmp
		echo -n "$(lang de:"Sicherungsdateien entfernen ... " en:"Removing backup files ... ")"
		rm -rf "$BACKUP_DIR" 2>/dev/null
		rm -f "$FORM_uploadfile_name" 2>/dev/null
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		modsave
		echo ""
		if [ -x "$WORKING_DIR/oscam" ] && [ "$FORM_restart" = "on" ]; then
			if pidof oscam > /dev/null; then
				echo "$(lang de:"Der OSCam-Dienst wird jetzt neu gestartet." en:"The OSCam service is restarted now.")"
				echo ""
				/etc/init.d/rc.oscam restart
			fi
		fi
	%></pre></p>
<% else %>
	<p style="color: #f7100b;" ><b>$(lang de:"Sie haben keine Sicherungs-Datei zum Hochladen ausgew&auml;hlt." en:"You have not selected a configuration archive for upload to your box.")</b></p>
	<p>$(lang de:"Die OSCam-Konfiguration wurde nicht ver&auml;ndert." en:"The OSCam configuration has not been changed.")<p>
<% fi %>

<p>
	<form action="/cgi-bin/conf/oscam"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>
</p>

<% cgi_end %>
