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

WORKING_DIR="$OSCAM_PATH/addon/oscam/"

LOGFILE=$(grep "^logfile" "$WORKING_DIR/oscam.conf"|cut -d "=" -f2|awk '{print $NF}')
EMMLOG_DIR=$(grep "^emmlogdir" "$WORKING_DIR/oscam.conf"|cut -d "=" -f2|awk '{print $NF}')

[ -z $EMMLOG_DIR ] && EMMLOG_DIR="$WORKING_DIR"

UNIQUEEMM_LOG=$(find "$EMMLOG_DIR" -name "*unique_emm.log")
GLOBALEMM_LOG=$(find "$EMMLOG_DIR" -name "*global_emm.log")
SHAREDEMM_LOG=$(find "$EMMLOG_DIR" -name "*shared_emm.log")
UNKNOWNEMM_LOG=$(find "$EMMLOG_DIR" -name "*unknown_emm.log")

OSC_TMP="/var/tmp/.oscam"

cgi --id=conf:oscam:_index
cgi_begin '$(lang de:"OSCam-Cardserver Info" en:"OSCam Card Server Info")'

echo '<h1>$(lang de:"OSCam-Cardserver Info-Seite" en:"OSCam card server info page")</h1>'
if [ -d "$OSC_TMP" ]; then
	echo '<pre class="log full">'"$(cat "$OSC_TMP/oscam.version")"'</pre>'
fi

echo '<h1>$(lang de:"OSCam-Cardserver LOG-File" en:"OSCam card server LOG file")</h1>'

if [ -e "$LOGFILE" ]; then
	echo '<pre class="log full">'"$(cat "$LOGFILE")"'</pre>'
	if [ -e "$WORKING_DIR/oscam.log" ]; then
	echo '<p>$(lang de:"OSCAMLOG-Datei als Archiv auf Ihrem PC sichern." en:"Backup OSCAMLOG file as archive on your PC.")</p>
	<form action="'$(href extra oscam do_oscamlogbackup)'" method="GET">
	<p><input type=submit value="$(lang de:"Sichern" en:"Backup")" style="width:180px"></p>
	</form>'
	fi
else
	echo '<p>$(lang de:"Das OSCam-Logfile ist nicht verf&uuml;gbar, Gr&uuml;nde daf&uuml;r k&ouml;nnen z.B. sein:" en:"The OSCam log file is not available. Resaons might be:")</p>
	<ol>
		<li>$(lang de:"Der OSCam-Dienst wurde noch nicht gestartet. Das Log-File wird nach dem ersten OSCam-Start angelegt." en:"OSCam service was not started. The log file will created after the first start.")</li>
		<li>$(lang de:"Bitte &uuml;berpr&uuml;fen Sie im \'oscam.conf\'-File den Pfad zum Logfile. Dieser muss nach <b>\'$WORKING_DIR\'</b> gesetzt werden." en:"Check the path to the log file in the \'oscam.conf\' file. It must be set to <b>\'$WORKING_DIR\'</b>.")</li>
	</ol>'
fi

echo '<h1>$(lang de:"OSCam-Cardserver UNIQUE-EMMLOG-File" en:"OSCam card server UNIQUE-EMMLOG file")</h1>'

if [ -e "$UNIQUEEMM_LOG" ]; then
	echo '<pre class="log full">'"$(cat "$UNIQUEEMM_LOG")"'</pre>'
	echo '<p>$(lang de:"UNIQUE-EMMLOG-Datei als Archiv auf Ihrem PC sichern." en:"Backup UNIQUE-EMMLOG file as archive on your PC.")</p>
	<form action="'$(href extra oscam do_unique_emmbackup)'" method="GET">
		<p><input type=submit value="$(lang de:"Sichern" en:"Backup")" style="width:180px"></p>
	</form>'
else
	echo '<p>$(lang de:"LOG-Datei in <b>\'$EMMLOG_DIR\'</b> nicht verf&uuml;gbar" en:"LOG file not availbale in <b>\'$EMMLOG_DIR\'</b>")</p>'
fi

#echo '<h1><p>$(lang de:"EMM-Log-Optionen:" en:"EMM log options:")<p></h1>'

echo '
	<p>
		<input type="checkbox" name="expertchk" value="no" onclick='\''document.getElementById("expertchk_show").style.display=(this.checked)? "" : "none"'\''>
		$(lang de:"Alle EMM-Logs anzeigen" en:"Show all EMM logs")
	</p>'

echo '<div id="expertchk_show" style="display:none;margin-left:0px;" name="expertchk_show">'

echo '<h1>$(lang de:"OSCam-Cardserver GLOBAL-EMMLOG-Datei" en:"OSCam card server GLOBAL-EMMLOG file")</h1>'

if [ -e "$GLOBALEMM_LOG" ]; then
	echo '<pre class="log full">'"$(cat "$GLOBALEMM_LOG")"'</pre>'
	echo '<p>$(lang de:"GLOBAL-EMMLOG-Dateien als Archiv auf Ihrem PC sichern." en:"Backup GLOBAL-EMMLOG files as archive on your PC.")</p>
	<form action="'$(href extra oscam do_global_emmbackup)'" method="GET">
		<p><input type=submit value="$(lang de:"Sichern" en:"Backup")" style="width:180px"></p>
	</form>'
else
	echo '<p>$(lang de:"LOG-Datei in <b>\'$EMMLOG_DIR\'</b> nicht verf&uuml;gbar" en:"LOG file not availbale in <b>\'$EMMLOG_DIR\'</b>")</p>'
fi

echo '<h1>$(lang de:"OSCam-Cardserver SHARED-EMMLOG-Datei" en:"OSCam card server SHARED-EMMLOG file")</h1>'

if [ -e "$SHAREDEMM_LOG" ]; then
	echo '<pre class="log full">'"$(cat "$SHAREDEMM_LOG")"'</pre>'
	echo '<p>$(lang de:"SHARED-EMMLOG-Dateien als Archiv auf Ihrem PC sichern." en:"Backup SHARED-EMMLOG files as archive on your PC.")</p>
	<form action="'$(href extra oscam do_shared_emmbackup)'" method="GET">
		<p><input type=submit value="$(lang de:"Sichern" en:"Backup")" style="width:180px"></p>
	</form>'
else
	echo '<p>$(lang de:"LOG-Datei in <b>\'$EMMLOG_DIR\'</b> nicht verf&uuml;gbar" en:"LOG file not availbale in <b>\'$EMMLOG_DIR\'</b>")</p>'
fi

echo '<h1>$(lang de:"OSCam-Cardserver UNKNOWN-EMMLOG-Datei" en:"OSCam card server UNKNOWN-EMMLOG file")</h1>'

if [ -e "$UNKNOWNEMM_LOG" ]; then
	echo '<pre class="log full">'"$(cat "$UNKNOWNEMM_LOG")"'</pre>'
	echo '<p>$(lang de:"UNKNOWN-EMMLOG-Dateien als Archiv auf Ihrem PC sichern." en:"Backup UNKNOWN-EMMLOG files as archive on your PC.")</p>
	<form action="'$(href extra oscam do_unknown_emmbackup)'" method="GET">
		<p><input type=submit value="$(lang de:"Sichern" en:"Backup")" style="width:180px"></p>
	</form>'
else
	echo '<p>$(lang de:"LOG-Datei in <b>\'$EMMLOG_DIR\'</b> nicht verf&uuml;gbar" en:"LOG file not availbale in <b>\'$EMMLOG_DIR\'</b>")</p>'
fi


echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'
#echo '</div><p><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form></p>'

cgi_end

