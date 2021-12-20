#!/usr/bin/haserl -u 2048 -U /var/tmp
<%
PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg

if [ -e /var/tmp/intern ]; then
		if [ "$(mount|grep "yaffs2")" ] || [ "$(mount|grep "ubifs")" ] || [ "$(mount|grep "ext4")" ] >/dev/null; then
        OSCAM_PATH=/var/media/ftp
        BKUP_PATH=/var/media/ftp/addon/oscam
    else
        OSCAM_PATH=/data
        BKUP_PATH=/var/tmp
    fi
else
    if [ -z "$OSCAM_PATH" ] || [ -z "$(df|grep "$OSCAM_PATH"|grep "/dev/sd")" ]; then OSCAM_PATH="$(df|grep "/dev/sda"|awk '{print $6}'|tail -1)"; fi
    BKUP_PATH="$OSCAM_PATH/addon/oscam"
fi

WORKING_DIR="$OSCAM_PATH/addon/oscam"

DAEMON_SIZE=0
[ -n "$FORM_softcamkey" ] && DAEMON_SIZE=$(ls -l "$FORM_softcamkey"|awk '{print$5}')

UPDATE=0;
RESTART=0
[ -e "$WORKING_DIR/SoftCam.Key" ] && UPDATE=1
[ "$(/etc/init.d/rc.oscam status)" = "running" ] && RESTART=1

cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"SoftCam.Key-Installation oder Aktualisierung" en:"SoftCam.Key installation or update")'
%>
<h1>$(lang de:"SoftCam.Key zur Box laden und installieren oder aktualisieren" en:"Upload SoftCam.Key and install or update")</h1>

<% if [ -n "$FORM_softcamkey_name" ] && [ -z "${FORM_softcamkey_name##[sS]oft[cC]am*}" ]  && [ ! -z "${FORM_softcamkey_name##*tar.gz}" ] && [ ! -z "${FORM_softcamkey_name##*rar}" ] && [ ! -z "${FORM_softcamkey_name##*zip}" ]; then %>
	<p>$(lang de:"Im ersten Schritt wird die Datei zur Box hochgeladen," en:"First, the file is uploaded to the box,")
	   $(lang de:"anschlie&szlig;end wird sie in das Zielverzeichnis verschoben." en:"then it is moved to the target directory.")
	</p>
	<p>$(lang de:"Sie haben gerade die Datei" en:"You just uploaded the file") <b><% echo -n $FORM_softcamkey_name %></b> $(lang de:"hochgeladen" en:"").<br>
	   $(lang de:"Die Dateigr&ouml;&szlig;e betr&auml;gt" en:"The file size is") <% echo -n $DAEMON_SIZE %> Bytes.<br>
	</p>
	<p><b>$(lang de:"Installationsverlauf" en:"Installation progress"):</b></p>
	<p><pre><%
		cd /var/tmp
		echo "$(lang de:"$FORM_softcamkey_name wurde im Zwischenspeicher gefunden." en:"Found $FORM_softcamkey_name in temporary memory.")"
		echo ""
		mv -f "$FORM_softcamkey" "$FORM_softcamkey_name" 2>/dev/null

		echo -n "$(lang de:"Setze Berechtigungen ... " en:"Setting permissions ... ")"
    sleep 1
		chmod 755 $FORM_softcamkey_name
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		if [ "$RESTART" = "1" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird jetzt gestoppt" en:"The OSCam service is about to be stopped,")"
			echo "$(lang de:"bestehende Clientverbindungen werden getrennt." en:"all client sessions are terminated.")"
			echo ""
			/etc/init.d/rc.oscam stop
			sleep 5
      echo ""
		fi

		echo -n "$(lang de:"Verschiebe $FORM_softcamkey_name in das Zielverzeichnis ... " en:"Moving $FORM_softcamkey_name to target directory ... ")"
		cd /var/tmp
		sleep 2
		mv -f "$FORM_softcamkey_name" "$WORKING_DIR/SoftCam.Key" 2>/dev/null

		if [ $? -ne 0 ]; then
			echo "$(lang de:"Fehler." en:"error.")"
			echo "$(lang de:"$FORM_softcamkey_name konnte nicht in das Zielverzeichnis verschoben werden." en:"$FORM_softcamkey_name could not be moved to the target directory.")"
			echo "$(lang de:"Bitte &uuml;berpr&uuml;fen Sie, ob gen&uuml;gend Speicher auf dem Medium zur Verf&uuml;gung steht." en:"Please check if sufficient memory is available on the media.")"
			[ -e "$WORKING_DIR/SoftCam.Key" ] && rm "$WORKING_DIR/SoftCam.Key"
		else
			echo "$(lang de:"fertig." en:"done.")"
			echo ""
			sleep 1
			echo "$(lang de:"Vorbereitungen abgeschlossen." en:"Preparations completed.")"
			echo ""
			modsave
			echo ""
			if [ "$UPDATE" = "1" ]; then
				echo "$(lang de:"Die 'SoftCam.Key' auf Ihrer FRITZ!BOX wurde erfolgreich aktualisiert." en:"Successfully updated 'SoftCam.Key' on your FRITZ!BOX.")"
			else
				echo "$(lang de:"Die 'SoftCam.Key' auf Ihrer FRITZ!BOX wurde erfolgreich installiert." en:"Successfully installed 'SoftCam.Key' on your FRITZ!BOX.")"
			fi
		fi
		echo ""

		if [ "$RESTART" = "1" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird jetzt neu gestartet." en:"The OSCam service is restarted now.")"
			echo ""
			/etc/init.d/rc.oscam start
		fi
	%></pre></p>
<% else %>
	<p style="color: #f7100b;" ><b>$(lang de:"Sie haben keine zu Ihrer Box passendes SoftCam.Key ausgew&auml;hlt." en:"You have not selected an appropriate SoftCam.Key for your box.")</b></p>
	<p>$(lang de:"<b>Hinweis:</b> Es k&ouml;nnen nur <b>entpackte</b> SoftCam.Key hochgeladen werden." en:"<b> Note: </ b> You can upload only <b>unpacked</b> SoftCam.Key.")<p>

<% fi %>

<p>
	<form action="/cgi-bin/conf/oscam"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>
</p>

<% cgi_end %>
