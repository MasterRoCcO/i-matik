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
[ -n "$FORM_list_smargo" ] && DAEMON_SIZE=$(ls -l "$FORM_list_smargo"|awk '{print$5}')

UPDATE=0;
RESTART=0
[ -e "$WORKING_DIR/list_smargo" ] && UPDATE=1
[ "$(/etc/init.d/rc.oscam status)" = "running" ] && RESTART=1

cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"list_smargo aktualisieren" en:"Update list_smargo")'
%>
<h1>$(lang de:"list_smargo hochladen und aktualisieren" en:"Upload list_smargo and update")</h1>

<% if [ -n "$FORM_list_smargo_name" ] && [ -z "${FORM_list_smargo_name##list_smargo*mips-freetz*}" ] && [ ! -z "${FORM_list_smargo_name##*tar.gz}" ] && [ ! -z "${FORM_list_smargo_name##*rar}" ] && [ ! -z "${FORM_list_smargo_name##*zip}" ]; then %>
	<p>$(lang de:"Im ersten Schritt wird die Datei zur Box hochgeladen," en:"First, the file is uploaded to the box,")
	   $(lang de:"anschlie&szlig;end wird sie in das Zielverzeichnis verschoben." en:"then it is moved to the target directory.")
	</p>
	<p>$(lang de:"Sie haben gerade die Datei" en:"You just uploaded the file") <b><% echo -n $FORM_list_smargo_name %></b> $(lang de:"hochgeladen" en:"").<br>
	   $(lang de:"Die Dateigr&ouml;&szlig;e betr&auml;gt" en:"The file size is") <% cat $FORM_list_smargo | wc -c %> Bytes.<br>
	</p>
	<p><b>$(lang de:"Installationsverlauf" en:"Installation progress"):</b></p>
	<p><pre><%
		cd /var/tmp
		echo "$(lang de:"$FORM_list_smargo_name wurde im Zwischenspeicher gefunden." en:"Found $FORM_list_smargo_name in temporary memory.")"
		echo ""
		mv -f "$FORM_list_smargo" "$FORM_list_smargo_name"

		echo -n "$(lang de:"Setze Berechtigungen ... " en:"Setting permissions ... ")"
		sleep 1
		chmod 755 $FORM_list_smargo_name
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

		echo -n "$(lang de:"Verschiebe $FORM_list_smargo_name in das Zielverzeichnis ... " en:"Moving $FORM_list_smargo_name to target directory ... ")"
		cd /var/tmp
		sleep 2
		mv -f "$FORM_list_smargo_name" "$WORKING_DIR/list_smargo" 2>/dev/null

		if [ $? -ne 0 ]; then
			echo "$(lang de:"Fehler." en:"error.")"
			echo "$(lang de:"$FORM_list_smargo_name konnte nicht in das Zielverzeichnis verschoben werden." en:"$FORM_list_smargo_name could not be moved to the target directory.")"
			echo "$(lang de:"Bitte &uuml;berpr&uuml;fen Sie, ob gen&uuml;gend Speicher auf dem Medium zur Verf&uuml;gung steht." en:"Please check if sufficient memory is available on the media.")"
			[ -e "$WORKING_DIR/list_smargo" ] && rm "$WORKING_DIR/list_smargo"
		else
			echo "$(lang de:"fertig." en:"done.")"
			echo ""
			sleep 1
			echo "$(lang de:"Vorbereitungen abgeschlossen." en:"Preparations completed.")"
			echo ""
			modsave
			echo ""
			if [ "$UPDATE" = "1" ]; then
				echo "$(lang de:"Die 'list_smargo' auf Ihrer FRITZ!BOX wurde erfolgreich aktualisiert." en:"Successfully updated 'list_smargo' on your FRITZ!BOX.")"
			else
				echo "$(lang de:"Die 'list_smargo' auf Ihrer FRITZ!BOX wurde erfolgreich installiert." en:"The 'list_smargo' on your FRITZ! BOX has been successfully installed.")"
			fi
		fi
		echo ""

		if [ "$RESTART" = "1" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird jetzt neu gestartet." en:"The OSCam service is now restarted.")"
			echo ""
			/etc/init.d/rc.oscam start
		fi
	%></pre></p>
<% else %>
	<p style="color: #f7100b;" ><b>$(lang de:"Sie haben keine zu Ihrer Box passende list_smargo ausgew&auml;hlt." en:"You have not selected an appropriate list_smargo for your box.")</b></p>
	<p>$(lang de:"Laden Sie bitte ein list_smargo des Types '*-mips-freetz' zur Box." en:"Please upload an list_smargo of type '*-mips-freetz'.")<p>
	<p>$(lang de:"<b>Hinweis:</b> Es k&ouml;nnen nur <b>entpackte</b> list_smargo hochgeladen werden." en:"<b> Note: </ b> You can upload only <b>unpacked</b> list_smargo.")<p>

<% fi %>

<p>
	<form action="/cgi-bin/conf/oscam"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>
</p>

<% cgi_end %>
