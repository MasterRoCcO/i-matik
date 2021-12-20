#!/bin/sh
## DEB/NFR Freetz-Team OSCam Addon ##

. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg


trim_string()
{
    trimmed=$1
    trimmed=${trimmed%%}
    trimmed=${trimmed##}
    echo $trimmed
}

HOST_IP=$(trim_string `hostname -i`)
VERSION="1.5.4"

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
DAEMON=oscam

TARGET_SIZE=1400
DATA_SIZE=$(df|grep "/data"|awk '{print $2}')
YAFFS2=0
UBIFS=0
JFFS2=0
EXT4=0
DATAD_SIZE=0
USB_STICK=0
USB_DIR=''
INTERN=0
INTERN_DIR=''

if cat /proc/partitions|grep "sda" >/dev/null; then
    USB_STICK=1
    if [ -z "$OSCAM_PATH" ] || [ -z "$(df|grep "$OSCAM_PATH"|grep "/dev/sd")" ]; then OSCAM_PATH="$(df|grep "/dev/sda"|awk '{print $6}'|tail -1)"; fi
    USB_DIR="$OSCAM_PATH"
fi

if mount|grep "jffs2" >/dev/null; then JFFS2=1; fi
if mount|grep "yaffs2" >/dev/null; then YAFFS2=1; fi
if mount|grep "ubifs" >/dev/null; then UBIFS=1; fi
if mount|grep "ext4" >/dev/null; then EXT4=1; fi

if [ "$JFFS2" = "1" ] && [ "$DATA_SIZE" -ge "$TARGET_SIZE" ]; then DATAD_SIZE=1; fi
if [ "$YAFFS2" = "1" ] || [ "$UBIFS" = "1" ] || [ "$EXT4" = "1" ] || [ "$DATAD_SIZE" = "1" ] ; then INTERN=1; fi

if [ "$YAFFS2" = "1" ] || [ "$UBIFS" = "1" ] || [ "$EXT4" = "1" ]; then
    INTERN_DIR=/var/media/ftp
elif [ "$JFFS2" = "1" ]; then
    INTERN_DIR=/data
fi

[ -e /var/tmp/intern ] && OSCAM_PATH="$INTERN_DIR"
WORKING_DIR="$OSCAM_PATH/addon/oscam"

WATCHDOG_LOG_PATH="$OSCAM_PATH/addon/watchdog"
MEM_USAGE=$(df|grep "$OSCAM_PATH" | awk '{ print $5}' | sed 's/%//g')

OSC_PORT=$(grep -i "^httpport" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_TMP="/var/tmp/.oscam"

check "$OSCAM_ENABLED" yes:auto "*":man
check "$OSCAM_INTERN" yes:intern "*":ustor
check "$OSCAM_COMCHK" yes:com
check "$OSCAM_DUECHK" yes:due
check "$OSCAM_RELOAD" yes:reload
check "$OSCAM_SMUSBCHK" yes:smusb
check "$OSCAM_PCSCDCHK" yes:pcscd

select "$OSCAM_COMCHK_IF" pl2303:comchk_pl2303 ftdi_sio:comchk_ftdi_sio
select "$OSCAM_SMUSBCHK_IF" 3580:smusbchk_3580 3680:smusbchk_3680 6000 smusbchk_6000
select "$OSCAM_SMMODE" phoenix:sm_phoenix smartmouse:sm_smartmouse

sec_begin '$(lang de:"Starttyp" en:"Start type")'
    echo '$(lang de:"Version" en:"Version"): '
    if [ -e "$WORKING_DIR/$DAEMON" ] && [ -e "$OSC_TMP/oscam.version" ]; then
        cat "$OSC_TMP/oscam.version"|grep "Version:"|awk '{print $NF}'|tee /var/tmp/flash/cams_version.txt
    else
        echo '$(lang de:"keine Info" en:"no info")'
    fi
       echo '<div style="float: right;"><font size="2">DEB/NFR-OSCam Addon Version: '$VERSION'</font></div>'
	echo '<p><div style="float: right;"><font size="2"><ul><li><a href="'$(href extra oscam changelog)'">$(lang de:"Changelog anzeigen" en:"View Changelog")</a></li></ul></div></p>'
       echo '<p><input id="e1" type="radio" name="ENABLED" value="yes"'$auto_chk'><label for="e1"> $(lang de:"Automatisch" en:"Automatic")</label><input id="e2" type="radio" name="ENABLED" value="no"'$man_chk'><label for="e2"> $(lang de:"Manuell" en:"Manual")</label></p>'
sec_end

if [ "$INTERN" = "0" ] && [ "$USB_STICK" = "0" ]; then
    sec_begin '$(lang de:"Interner Speicher" en:"Internal Memory")'
        echo '<p>$(lang de:"Kein oder unzureichend interner Speicher. Beachten Sie bitte auch &quot;Hilfe Intern-Modus&quot;. Alternativ dazu, USB-Speicher anstecken und neu starten." en:"No or insufficient internal memory. Please also pay attention to &quot;Internal Mode help&quot;. Alternatively, connect USB memory and restart.")</p>'
    sec_end
fi

sec_begin '$(lang de:"Startmodus (Intern oder USB)" en:"Start Mode (Internal or USB)")'
    echo '<table>'
    if [ "$INTERN" = "0" ] && [ "$JFFS2" = "1" ]; then
        echo '
            <tr height="35px">
                <td><ul><li><a href="'$(href extra oscam internhilfe)'">$(lang de:"Hilfe Intern-Modus" en:"Internal Mode help")</a></li></ul></td>
            </tr>'
    elif [ "$INTERN" = "1" ]; then
        echo '
            <tr height="35px">
                <td colspan="3"><input id="e3" type="radio" name="INTERN" value="yes"'$intern_chk'><label for="e3"> $(lang de:"Intern-Modus" en:"Internal Mode")</label></td>
            </tr>'
        if [ ! -d "$INTERN_DIR/addon/oscam" ]; then
            echo '
                <tr height="35px">
                    <td style="width: 25px"></td>
                    <td colspan="2"><font size="2">$(lang de:"Bei ausgew&auml;hltem &quot;Intern-Modus&quot; auf &quot;&Uuml;bernehmen&quot; klicken, um die OSCam Konfigurationsdateien zu installieren." en:"With &quot;Internal Mode&quot; selected click on &quot;Apply&quot; to install the OSCAM config files.")</font></td>
                </tr>
                <tr height="35px">
                    <td style="width: 25px"></td>
                    <td colspan="2"><font size="2">$(lang de:"Vorher die Anleitung runterladen, diese ist nach Aktivierung nicht mehr Verfügbar." en:"Before download the manual, this is no longer available after activation.")</font></td>
							 </tr>
               <tr height="35px">
                    <td style="width: 25px"></td>
                    <td><ul><li><a class="active" href="http://freetz.digital-eliteboard.com/Teamserver/Freetz/HowTos/Anleitung%20Intern-Modus-USB-Modus%20OScam%20mit%20oscam-1.5x.pdf" target="_blank">$(lang de:"Anleitung Intern-Modus-USB-Modus OScam mit oscam-1.5x" en:"Instructions Internal mode USB mode OScam with oscam-1.4x")</a></li></ul></td>
                </tr>'
        fi
        echo '
            <tr height="35px">
                <td style="width: 25px"></td>
                <td>$(lang de:"Intern-Pfad:" en:"Internal Path:")</td>
                <td><input type="text" name="PATH" size="50" value="'$(html "$INTERN_DIR/addon/oscam")'" disabled></td>
            </tr>'
    fi

    if [ "$USB_STICK" = "0" ]; then
        echo '
          <tr height="35px">
            <td><ul><li><a href="'$(href extra oscam stickhilfe)'">$(lang de:"Hilfe USB-Modus" en:"USB mode help")</a></li></ul></td>
          </tr>'
    elif [ "$USB_STICK" = "1" ]; then
        echo '
          <tr height="35px">
            <td colspan="3"><input id="e4" type="radio" name="INTERN" value="no"'$ustor_chk'><label for="e4"> $(lang de:"USB-Modus" en:"USB Mode")</label></td>
          </tr>'
        if [ ! -d "$USB_DIR/addon/oscam" ]; then
            echo '
              <tr height="35px">
                <td style="width: 25px"></td>
                <td colspan="2"><font size="2">$(lang de:"Bei ausgew&auml;hltem &quot;USB-Modus&quot; auf &quot;&Uuml;bernehmen&quot; klicken, um die OSCam Konfigurationsdateien zu installieren." en:"With &quot;USB Mode&quot; selected click on &quot;Apply&quot; to install the OSCAM config files.")</font></td>
              </tr>
              <tr height="35px">
                <td style="width: 25px"></td>
                <td colspan="2"><font size="2">$(lang de:"Vorher die Anleitung runterladen, diese ist nach Aktivierung nicht mehr Verfügbar." en:"Before download the manual, this is no longer available after activation.")</font></td>
							</tr>
              <tr height="35px">
                   <td style="width: 25px"></td>
              <td><ul><li><a class="active" href="http://freetz.digital-eliteboard.com/Teamserver/Freetz/HowTos/Anleitung%20Intern-Modus-USB-Modus%20OScam%20mit%20oscam-1.4x.pdf" target="_blank">$(lang de:"Anleitung Intern-Modus-USB-Modus OScam mit oscam-1.4x" en:"Instructions Internal mode USB mode OScam with oscam-1.4x")</a></li></ul></td>
                      </tr>'
        fi
        echo '
            <tr height="35px">
                <td style="width: 25px"></td>
                <td>$(lang de:"USB-Pfad:" en:"USB Path:")</td>
                <td><input type="text" name="PATH" size="50" value="'$(html "$USB_DIR/addon/oscam")'"'$([ "$OSCAM_INTERN" = "yes" ] && echo ' disabled')'"></td>
            </tr>
            <tr height="35px">
                <td style="width: 25px"></td>
                <td colspan="2"><font size="2">$(lang de:"<b>Hinweis:</b> Bei Verwendung mehrerer Speicher am USB-Anschluss der FRITZ!BOX wird empfohlen, in den Freetz-Einstellungen f&uuml;r Mountpoints das Namensschema &quot;Partitionsname&quot; auszuw&auml;hlen." en:"Note: If you connect multiple storage devices to the USB port of your FRITZ!BOX it is recommended to set &quot;partition name&quot; as naming scheme for mountpoints in Freetz settings.")</font></td>
            </tr>'
    fi
    echo '</table>'
sec_end

if [ -e "$WORKING_DIR/$DAEMON" ]; then
sec_begin '$(lang de:"OSCam-Webinterface" en:"OSCam Web Interface")'
    if [ "$(/etc/init.d/rc.oscam status)" = 'stopped' ]; then
        echo '<h2>$(lang de:"OSCam wurde nicht gestartet!" en:"OSCam is not running!")</h2>'
    else
	if [ -z "$OSC_PORT" ]; then
	    echo '<h2>$(lang de:"OSCam-Webinterface nicht aktiv!" en:"OSCam web interface not active!")</h2>'
	else
	    echo '<ul><li><a href="http://'$HOST_IP':'$OSC_PORT'/" target="_blank">$(lang de:"Aufrufen" en:"Call")</a></li></ul>'
	fi
    fi
sec_end
fi

if [ -e "$WORKING_DIR/$DAEMON" ] && [ -e /var/tmp/.oscam ]; then
    sec_begin '$(lang de:"OSCam Info-Seite " en:"OSCam Info Page")'
        echo '<ul><li><a href="'$(href extra oscam oscamversion)'">$(lang de:"OSCam-Cardserver Info-Seite" en:"OSCam card server info page")</a></li></ul>'
    sec_end
fi

if [ "$INTERN" = "1" ] || [ "$USB_STICK" = "1" ]; then
    if [ -e "$WORKING_DIR/$DAEMON" ]; then
        sec_begin '$(lang de:"OSCam-Setup - Aktualisierung" en:"OSCam Setup - Update")'
            echo '<p>$(lang de:"Es wurde eine bestehende Installation von OSCam gefunden." en:"A current installation of OSCam was found.")</p>
                  <p>$(lang de:"Falls Sie OSCam jetzt aktualisieren m&ouml;chten, folgen Sie bitte dem Link." en:"Please follow the link if you wish to update the OSCam binary now.")</p>
                  <ul><li><a href="'$(href extra oscam oscamup)'">$(lang de:"OSCam aktualisieren" en:"Update OSCam")</a></li></ul>'
        sec_end
    elif [  -d "$WORKING_DIR" ]; then
        sec_begin '$(lang de:"OSCam-Setup - Installation" en:"OSCam Setup - Installation")'
            echo '<p style="color: #f7100b;"><b>$(lang de:"Sie haben noch keine OSCam-Binary installiert. Diese ist f&uuml;r den Start erforderlich." en:"You have not yet intalled the OSCam binary. This is required before start.")</b></p>
                  <p>$(lang de:"Zur Erst-Installation der OSCam-Binary folgen Sie bitte dem Link." en:"Please follow the link to install the OSCam binary now.")</p>
                  <ul><li><a href="'$(href extra oscam oscamup)'">$(lang de:"OSCam installieren" en:"Install OSCam")</a></li></ul>'
        sec_end
    fi
fi

if [ -e "$WORKING_DIR/$DAEMON" ]; then
sec_begin '$(lang de:"USB Comport (Treiberauswahl)" en:"USB Comport (Choice of Driver)")'
    echo '
    <p>
        <input type="hidden" name="COMCHK" value="no">
        <input id="w1" type="checkbox" name="COMCHK" value="yes"'$com_chk'><label for="w1"> $(lang de:"USB Comport mit einem Treiber aktivieren" en:"Activate USB comport with driver") </label>
    </p>
    <p>
        <select name="COMCHK_IF">
            <option value="pl2303"'$comchk_pl2303_sel'>PL 2303</option>
            <option value="ftdi_sio"'$comchk_ftdi_sio_sel'>FTDI_SIO</option>
        </select> $(lang de:"Modul w&auml;hlen" en:"Select module")
    </p>
    <p>
        <input type="hidden" name="DUECHK" value="no">
        <input id="w2" type="checkbox" name="DUECHK" value="yes"'$due_chk'><label for="w2"> $(lang de:"FTDI + PL2303 Treiber gemeinsam" en:"FTDI + PL2303 drivers combined")</label>
    </p>
    <p>
        <input type="hidden" name="RELOAD" value="no">
        <input id="w3" type="checkbox" name="RELOAD" value="yes"'$reload_chk'><label for="w3"> $(lang de:"Card-Reader-Treiber neu laden" en:"Reload card reader driver")</label>
    </p>'
sec_end
fi

if [ -e "$WORKING_DIR/$DAEMON" ]; then
  if [ -x /usr/bin/smusbutil ]; then
    sec_begin '$(lang de:"WB Smartmouse USB (Smusbutil)" en:"WB smartmouse USB (Smusbutil)")'
        echo '
        <p>
            <input type="hidden" name="SMUSBCHK" value="no">
            <input id="w4" type="checkbox" name="SMUSBCHK" value="yes"'$smusb_chk'><label for="w4"> $(lang de:"USB-Smartmouse mit" en:"Use USB smartmouse with")</label>
        </p>
        <p>
            <select name="SMUSBCHK_IF">
                <option value="3580"'$smusbchk_3580_sel'>3580</option>
                <option value="3680"'$smusbchk_3680_sel'>3680</option>
                <option value="6000"'$smusbchk_6000_sel'>6000</option>
            </select> $(lang de:"Mhz benutzen" en:"Mhz")
        </p>
        <p>
            <select name="SMMODE">
                <option value="phoenix"'$sm_phoenix_sel'>Phoenix</option>
                <option value="smartmouse"'$sm_smartmouse_sel'>Smartmouse</option>
            </select> $(lang de:"Modus w&auml;hlen" en:"Select mode")
        </p>'
    sec_end
  fi
fi

if [ -e "$WORKING_DIR/$DAEMON" ]; then
  if [ -x /usr/bin/pcscd ]; then
    sec_begin '$(lang de:"PCSCD Treiber laden (CCID)" en:"Load PCSCD Driver (CCID)")'
        echo '
            <p>
                <input type="hidden" name="PCSCDCHK" value="no">
                <input id="w5" type="checkbox" name="PCSCDCHK" value="yes"'$pcscd_chk'><label for="w5"> $(lang de:"CCID Treiber laden" en:"Load CCID driver")</label>
            </p>'
    sec_end
  fi
fi

if [ -e "$WORKING_DIR/$DAEMON" ]; then
sec_begin '$(lang de:"Treiber-Status" en:"Driver Status")'
    if [ -n "$(lsmod | grep "ftdi_sio")" ]; then 
        FTDI_STATUS='$(lang de:"geladen" en:"loaded")'
        FTDI_VERSION=$(dmesg|grep 'ftdi'|grep 'Converters'|tail -1|cut -d : -f2|awk '{print$1}')
    else 
        FTDI_STATUS='$(lang de:"nicht geladen" en:"not loaded")'
    fi
    if [ -n "$(lsmod | grep "pl2303")" ]; then 
        PL2303_STATUS='$(lang de:"geladen" en:"loaded")'
    else 
        PL2303_STATUS='$(lang de:"nicht geladen" en:"not loaded")'
    fi
    echo '
    <table style="padding: 0px 0px 0px 0px;">
        <tr><th align="left" style="border-bottom: 1px solid #B4B5B0;">Treiber  </th><th align="left" style="border-bottom: 1px solid #B4B5B0;">Status</th></tr>
        <tr><td style="width:250px"><font size="2">FTDI_SIO '$FTDI_VERSION'</font></td><td><font size="2">'$FTDI_STATUS'</font></td></tr>
        <tr><td style="width:250px"><font size="2">PL2303 </font></td><td><font size="2">'$PL2303_STATUS'</font></td></tr>'
    if [ -x /usr/bin/pcscd ]; then
        if [ -n "$(find "/var/run/pcscd" -name "pcscd.pid")" ]; then 
        		/usr/bin/pcscd -dv >$OSC_TMP/pcscd.version
        		sleep 1
        		PCSCD_VERSION=$(cat $OSC_TMP/pcscd.version | grep pcsc-lite | cut -d " " -f3)
            PCSCD_STATUS='$(lang de:"geladen" en:"loaded")'
        else 
            PCSCD_STATUS='$(lang de:"nicht geladen" en:"not loaded")'
        fi
        echo '
        <tr><td style="width:250px"><font size="2">PCSCD(CCID) '$PCSCD_VERSION'</font></td><td><font size="2">'$PCSCD_STATUS'</font></td></tr>'
    fi
    echo '</table>'
sec_end
fi 

if [ -e "$WORKING_DIR/$DAEMON" ]; then
sec_begin '$(lang de:"OSCam-Tools" en:"OSCam-tools")'
    echo '<p>$(lang de:"Hier geht es zur Serialanzeige Cardreader,Udev-Regel und Fusebyte-Payload-Abfrage." en:"Here is the serial display cardreader, Udev rule and fusebyte payload query.")</p>
		<p>
        <ul><li><a href="'$(href extra oscam oscamtools)'">$(lang de:"OSCam-Tools" en:"OSCam-tools")</a></li></ul>
    </p>'
sec_end
fi

if [ -e "$WORKING_DIR/$DAEMON" ]; then
sec_begin '$(lang de:"Watchdog-Info" en:"Watchdog Info")'
    echo '
    <table>
        <tr height="35px">
            <td>$(lang de:"Externe IP-Adresse:" en:"External IP address:")</td>
            <td><input type="text" size="17" value="'$(html "$(get_ip)")'" disabled></td>
        </tr>
        <tr height="35px">
            <td>$(lang de:"Benutzter Speicher:" en:"Memory usage:")</td>
            <td><input type="text" size="4" value="'$(html "$MEM_USAGE")'%" disabled></td>
        </tr>
        <tr height="35px">
            <td>$(lang de:"Log-Verzeichnis:" en:"Log directory")</td>
            <td><input type="text" size="50" value="'$(html "$WATCHDOG_LOG_PATH")'" disabled></td>
        </tr>
    </table>
    <p>
        <ul><li><a href="'$(href extra oscam watchdoglog)'">$(lang de:"Watchdog-Log-Datei" en:"Watchdog log file")</a></li></ul>
        <ul><li><a href="'$(href extra oscam oscamwatchdog)'">$(lang de:"Watchdog-Einstellungen" en:"Watchdog settings")</a></li></ul>
    </p>'
sec_end
fi
