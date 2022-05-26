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
[ -n "$FORM_oscam" ] && DAEMON_SIZE=$(ls -l "$FORM_oscam"|awk '{print$5}')

UPDATE=0;
RESTART=0
[ -e "$WORKING_DIR/oscam" ] && UPDATE=1
[ "$(/etc/init.d/rc.oscam status)" = "running" ] && RESTART=1

cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"OSCam-Binary-Installation oder Aktualisierung" en:"OSCam binary installation or update")'
%>
<h1>$(lang de:"OSCam-Binary zur Box laden und installieren oder aktualisieren" en:"Upload OSCam binary to box and install or update")</h1>

<% if [ -n "$FORM_oscam_name" ] && [ -z "${FORM_oscam_name##oscam*freetz*}" ] && [ ! -z "${FORM_oscam_name##*tar.gz}" ] && [ ! -z "${FORM_oscam_name##*rar}" ] && [ ! -z "${FORM_oscam_name##*zip}" ]; then %>
	<p>$(lang de:"Im ersten Schritt wird die Datei zur Box hochgeladen," en:"First, the file is uploaded to the box,")
	   $(lang de:"anschlie&szlig;end wird sie in das Zielverzeichnis verschoben." en:"then it is moved to the target directory.")
	   $(lang de:"Im Falle einer vorhandenen Installation wird eine Sicherungkopie angelegt." en:"If a previous installation exists a backup copy will be created.")
	</p>
	<p>$(lang de:"Sie haben gerade die Datei" en:"You just uploaded the file") <b><% echo -n $FORM_oscam_name %></b> $(lang de:"hochgeladen" en:"").<br>
	   $(lang de:"Die Dateigr&ouml;&szlig;e betr&auml;gt" en:"The file size is") <% echo -n $DAEMON_SIZE %> Bytes.<br>
	</p>
	<p><b>$(lang de:"Installationsverlauf" en:"Installation progress"):</b></p>
	<p><pre><%
		cd /var/tmp
		echo "$(lang de:"$FORM_oscam_name wurde im Zwischenspeicher gefunden." en:"Found $FORM_oscam_name in temporary memory.")"
		echo ""
		mv -f "$FORM_oscam" "$FORM_oscam_name"

		echo -n "$(lang de:"Setze Berechtigungen ... " en:"Setting permissions ... ")"
		sleep 1
		chmod 755 $FORM_oscam_name
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

		if [ "$UPDATE" = "1" ]; then
			echo "$(lang de:"Es wurde eine bestehende OSCam installation im Zielverzeichnis gefunden." en:"A previous installation of OSCam was found in the taregt directory.")"
			echo "$(lang de:"Lege Sicherungskopie des OSCam-Dienstes unter 'oscam_old'" en:"For recovery purposes a backup named 'oscam_old'")"
			echo -n "$(lang de:"in $BKUP_PATH an ... " en:"is created in $BKUP_PATH ... ")"
			mv -f "$WORKING_DIR/oscam" "$BKUP_PATH/oscam_old"
			echo "$(lang de:"fertig." en:"done.")"
			echo ""
		fi

		echo -n "$(lang de:"Verschiebe $FORM_oscam_name in das Zielverzeichnis ... " en:"Moving $FORM_oscam_name to target directory ... ")"
		sleep 1
		cd /var/tmp
		mv -f "$FORM_oscam_name" "$WORKING_DIR/oscam" 2>/dev/null

		if [ $? -ne 0 ]; then
			echo "$(lang de:"Fehler." en:"error.")"
			echo "$(lang de:"$FORM_oscam_name konnte nicht in das Zielverzeichnis verschoben werden." en:"$FORM_oscam_name could not be moved to the target directory.")"
			echo "$(lang de:"Bitte &uuml;berpr&uuml;fen Sie, ob gen&uuml;gend Speicher auf dem Medium zur Verf&uuml;gung steht." en:"Please check if sufficient memory is available on the media.")"
			[ -e "$WORKING_DIR/oscam" ] && rm "$WORKING_DIR/oscam"
			if [ -e "$BKUP_PATH/oscam_old" ]; then
				echo ""
				echo -n "$(lang de:"Die Sicherungskopie wird zur&uuml;ckgespielt ... " en:"The previous file is restored from backup ... ")"
				mv "$BKUP_PATH/oscam_old" "$WORKING_DIR/oscam"
				if [ $? -ne 0 ]; then
					echo "$(lang de:"Fehler." en:"error.")"
					echo "$(lang de:"Auch $BKUP_PATH/oscam_old konnte nicht in das Zielverzeichnis verschoben werden." en:"Also $BKUP_PATH/oscam_old could not be moved to the target directory.")"
					echo "$(lang de:"Es wird dringend empfohlen, den verf&uuml;gbaren Speicher zu &uuml;berpr&uuml;fen und ggf. zu bereiningen." en:"It is urgently recommended to check the available memory and clean up if neccessary.")"
					[ -e "$WORKING_DIR/oscam" ] && rm "$WORKING_DIR/oscam"
	^			else
					echo "$(lang de:"fertig." en:"done.")"
				fi
			fi
		else
			echo "$(lang de:"fertig." en:"done.")"
			echo ""
			sleep 1
			echo "$(lang de:"Vorbereitungen abgeschlossen." en:"Preparations completed.")"
			echo ""
			modsave
			echo ""
			if [ "$UPDATE" = "1" ]; then
				echo "$(lang de:"Der OSCam-Dienst wurde auf Ihrer FRITZ!BOX erfolgreich aktualisiert." en:"Successfully updated the OSCam service on your FRITZ!BOX.")"
			else
				echo "$(lang de:"Der OSCam-Dienst wurde auf Ihrer FRITZ!BOX erfolgreich installiert." en:"Successfully installed the OSCam service on your FRITZ!BOX.")"
			fi
		fi
		echo ""

		if [ -x "$WORKING_DIR/oscam" ] && [ "$RESTART" = "1" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird jetzt neu gestartet." en:"The OSCam service is restarted now.")"
			echo ""
			/etc/init.d/rc.oscam start
		fi
	%></pre></p>
<% else %>
	<p style="color: #f7100b;" ><b>$(lang de:"Sie haben keine zu Ihrer Box passendes OSCam-Binary ausgew&auml;hlt." en:"You have not selected an appropriate OSCam binary for your box.")</b></p>
	<p>$(lang de:"Laden Sie bitte ein OSCam-Binary des Types '*-freetz' zur Box." en:"Please upload an OSCam binary of type '*-freetz'.")<p>
	<p>$(lang de:"<b>Hinweis:</b> Es k&ouml;nnen nur <b>entpackte</b> OSCam-Binary hochgeladen werden." en:"<b> Note: </ b> You can upload only <b>unpacked</b> OSCam binary.")<p>
<% fi %>

<p>
	<form action="/cgi-bin/conf/oscam"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>
</p>

<% cgi_end %>
