#!/usr/bin/haserl
<%
PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg

RESTART=0

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

cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"OSCam-Dienst wiederherstellen" en:"Restore OSCam service")'
%>
<h1>$(lang de:"OSCam-Dienst wiederherstellen" en:"Restore OSCam service")</h1>
<% if [ -e "$BKUP_PATH/oscam_old" ]; then %>
	<p>$(lang de:"Es wurde die Sicherungskopie eines vormals installierten OSCam-Dienstes gefunden." en:"A backup copy of a previously installed OSCam service was found.")<br>
	   $(lang de:"Das Backup wird nun in den Speicher Ihrer FRITZ!BOX zur&uuml;ck gespielt." en:"The backup is now restored to your FRITZ!BOX memory.")<br>
	   $(lang de:"Eventuell bestehende Client-Verbindungen werden dabei getrennt." en:"Current client sessions will be terminated. ")<br>
	   $(lang de:"Bitte haben Sie einen Moment Geduld ... " en:"Please be patient ... ")
	</p>
	<p><b>$(lang de:"Wiederherstellungsverlauf" en:"Restoration progress"):</b></p>
	<p><pre><%
		echo "$(lang de:"Die Sicherungskopie des OSCam-Dienstes" en:"The OSCam service is restored from a backup copy")"
		echo "$(lang de:"wird zur&uuml;ck gespielt." en:"of the previous OSCam binary.")"
		echo ""

		sleep 2
		if [ "$(/etc/init.d/rc.oscam status)" = "running" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird jetzt gestoppt," en:"OSCam service is about to be stopped,")"
			echo "$(lang de:"bestehende Clientverbindungen werden getrennt." en:"all client sessions are terminated.")"
			echo ""
			/etc/init.d/rc.oscam stop
			sleep 5
			echo ""
			RESTART=1
		fi

		echo -n "$(lang de:"Sicherungskopie des OSCam-Dienstes wird wiederhergestellt ... " en:"Restoring OSCam service from backup ... ")"
		sleep 1
		cd /var/tmp
		mv -f "$BKUP_PATH/oscam_old" "$WORKING_DIR/oscam"

		if [ $? -ne 0 ]; then
			echo "$(lang de:"Fehler." en:"error.")"
			echo "$(lang de:"$BKUP_PATH/oscam_old konnte nicht in das Zielverzeichnis verschoben werden." en:"$BKUP_PATH/oscam_old could not be moved to the target directory.")"
			echo "$(lang de:"Bitte &Uuml;berpr&uuml;fen Sie, ob gen&uuml;gend Speicher auf dem Medium zur Verf&uuml;gung steht." en:"Please check if sufficient memory is available on the media.")"
			[ -e "$WORKING_DIR/oscam" ] && rm "$WORKING_DIR/oscam"
		else
			echo "$(lang de:"fertig." en:"done.")"
			echo ""
			sleep 1
			modsave
			echo ""
			echo "$(lang de:"Der OSCam-Dienst wurde auf Ihrer FRITZ!BOX erfolgreich wiederhergestellt." en:"Successfully restored OSCam service on your FRITZ!BOX.")"
		fi
		echo ""

		if [ -x "$WORKING_DIR/oscam" ] && [ "$RESTART" = "1" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird jetzt neu gestartet." en:"The OSCam service is restarted now.")"
			echo ""
			/etc/init.d/rc.oscam start
		fi
	%></pre></p>
<% else %>
	<p style="color: #f7100b;" ><b>$(lang de:"Es wurden keine Sicherungsdaten f&uuml;r eine Wiederherstellung gefunden!" en:"No backup data was found for restoration!")</b></p>
	<p>$(lang de:"Versuchen Sie ggf. eine andere OScam-Version &uuml;ber 'OSCam-Update' zu installieren." en:"You may try to install a different OSCam release via 'OSCam Update'.")</p>
<% fi %>

<p>
	<form action="/cgi-bin/conf/oscam"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>
</p>

<% cgi_end %>
