#!/usr/bin/haserl -u 2048 -U /var/tmp
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

cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"Speicher bereinigen" en:"Clean up memory")'

%>
<h1>$(lang de:"Speicher bereinigen" en:"Clean up memory")</h1>

<% if [ -e "$WORKING_DIR/$DAEMON" ]; then %>
	<p>$(lang de:"Die angegebenen Datein werden entfernt." en:"The files specified are removed.")
	        </p>
<p><b>$(lang de:"Deinstallationsverlauf" en:"Removal progress"):</b></p>
	<p><pre><%
		if [ "$(/etc/init.d/rc.oscam status)" = "running" ]; then
			echo "$(lang de:"Der OSCam-Dienst wird gestoppt" en:"The OSCam service is about to be stopped,")"
			echo "$(lang de:"bestehende Clientverbindungen werden getrennt." en:"all client sessions will be terminated.")"
			echo ""
			/etc/init.d/rc.oscam stop
			echo ""
		fi

		echo "$(lang de:"Entbehrliche Dateien werden entfernt, um Speicherplatz freizugeben." en:"Dispensable files are removed to free up memory.")"
		echo ""

		cd $WORKING_DIR

		echo "$(lang de:"Entferne vorhandene OSCam-Binary ... " en:"Removing exisiting OSCam binary ... ")"
		rm oscam 2>/dev/null
		sleep 1
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"Entferne vorhandene SoftCam.Key ... " en:"Removing exisiting SoftCam.Key ... ")"
		rm SoftCam.Key 2>/dev/null
		sleep 1
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"Entferne vorhandene list_smargo ... " en:"Removing exisiting list_smargo ... ")"
		rm list_smargo 2>/dev/null
		sleep 1
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"Entferne vorhandene Konfigurationsbackups ... " en:"Removing exisiting configuration backups ... ")"
		rm *bak 2>/dev/null
		sleep 1
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"Entferne vorhandene Webinterface Skins ... " en:"Removing existing web interface skins ... ")"
		rm *css 2>/dev/null
		sleep 1
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"Entferne vorhandene Logdateien ... " en:"Removing exisiting log files ... ")"
		rm *log 2>/dev/null
		rm *log-prev 2>/dev/null
		cd $OSCAM_PATH/addon/watchdog
		rm watchdog.log>/dev/null
		sleep 1
		echo "$(lang de:"fertig." en:"done.")"
		echo ""

		echo "$(lang de:"Der Speicher wurde bereinigt." en:"The memory was cleaned up.")"
		echo ""
		echo "$(lang de:"Die OSCam-Binary muss neu installiert werden." en:"The OSCam binary needs to be reinstalled.")"
		echo ""
		modsave
		echo ""
	%></pre></p>
<% fi %>

<p>
    <form action="/cgi-bin/extra/oscam/oscamup"><div class="btn"><input type="submit" value="$(lang de:"OSCam installieren" en:"Install OSCam")"></div></form>
</p>

<% cgi_end %>
