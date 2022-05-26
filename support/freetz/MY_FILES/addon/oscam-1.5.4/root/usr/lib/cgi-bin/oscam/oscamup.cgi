#!/bin/sh

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
DAEMON=oscam


UPDATE=0;
UPD_INST_TXT_DE="installieren"
UPD_INST_TXT_EN="Install"
if [ -e "$WORKING_DIR/oscam" ]; then 
    UPDATE=1
    UPD_INST_TXT_DE="aktualisieren"
    UPD_INST_TXT_EN="Update"
fi

if [ -e "$WORKING_DIR" ]; then find "/usr/lib/freetz" -name libssl.so.* >$WORKING_DIR/libssl.version; fi

LIBSSL_VERSION1=$(cat $WORKING_DIR/libssl.version | grep libssl.so.1.0.0  | cut -d "/" -f5)

LIBSSL_VERSION2=$(cat $WORKING_DIR/libssl.version | grep libssl.so.1.1  | cut -d "/" -f5)

LIBSSL_VERSION3=$(cat $WORKING_DIR/libssl.version | grep libssl.so.3 | cut -d "/" -f5)


#cgi --id=cgi --id=extra:oscam:oscamup
cgi_begin 'OSCam-Setup'

if [ -e "$WORKING_DIR/" ]; then

echo '
<h1>OSCam-Dienst installieren oder aktualisieren</h1>
<p>
    Hier k&ouml;nnen Sie den OSCam-Dienst im internen oder USB Speicher Ihrer FRITZ!BOX installieren oder aktualisieren.
</p>'

if [ "$LIBSSL_VERSION1" = "libssl.so.1.0.0" ]; then
sec_begin 'Es wurde im Image <b>'$LIBSSL_VERSION1'</b> gefunden, somit wird diese OSCamversion benötigt'
    echo '
    <p>
        Hier gibt es die benötigte OSCam-Binaries:
    </p>
    <ul>
        <li><a class="active" href="https://freetz.digital-eliteboard.com/?dir=Teamserver/Freetz/OScam/OpenSSL_1_0_x" target="_blank">OSCam-Binary herunterladen</a></li>
    </ul>'
sec_end
fi
if [ "$LIBSSL_VERSION2" = "libssl.so.1.1" ]; then
sec_begin 'Es wurde im Image <b>'$LIBSSL_VERSION2'</b> gefunden, somit wird diese OSCamversion benötigt'
    echo '
    <p>
        Hier gibt es die benötigte OSCam-Binaries:
    </p>
    <ul>
        <li><a class="active" href="https://freetz.digital-eliteboard.com/?dir=Teamserver/Freetz/OScam/OpenSSL_1_1_x" target="_blank">OSCam-Binary herunterladen</a></li>
    </ul>'
sec_end
fi
if [ "$LIBSSL_VERSION3" = "libssl.so.3" ]; then
sec_begin 'Es wurde im Image <b>'$LIBSSL_VERSION3'</b> gefunden, somit wird diese OSCamversion benötigt'
    echo '
    <p>
        Hier gibt es die benötigte OSCam-Binaries:
    </p>
    <ul>
        <li><a class="active" href="https://freetz.digital-eliteboard.com/?dir=Teamserver/Freetz/OScam/OpenSSL_3_0_x" target="_blank">OSCam-Binary herunterladen</a></li>
    </ul>'
sec_end
fi


sec_begin "OSCam $UPD_INST_TXT_DE"
    if [ "$UPDATE" = "1" ]; then
        echo '
        <p>
            Eine bestehende Installation von OSCam wurde gefunden.
            Wenn Sie mit der Aktualisierung fortfahren wird eine Sicherungskopie der vorhandenen OSCam-Binary angelegt.
        </p>'
    else
        echo '
        <p>
            Es ist noch keine OSCam-Binary im Zielverzeichnis vorhanden.
            Fahren Sie fort, um eine OSCam-Binary im Zielverzeichnis zu installieren.
        </p>'
    fi

    echo '
    <p>
        Laden Sie eine passende OSCam-Binary vom Typ <b>oscam-...freetz-...</b> zur Box hoch.
        Die Datei darf <b>nicht umbenannt</b> werden.
    </p>
    <form action="'$(href extra oscam do_oscamexternal)'" method="POST" enctype="multipart/form-data">
        <p><input type="file" size="50" name="oscam" ></p>
        <p><input type="submit" value="OSCam '$UPD_INST_TXT_DE'" style="width:180px"></p>
    </form>'
sec_end

if [ -e "$BKUP_PATH/${DAEMON}_old" ]; then
    sec_begin 'OSCam-Dienst aus Backup wiederherstellen'
        echo '
        <p>
            Wenn das Update nicht erfolgreich war - z.B. OSCam l&auml;sst sich nach dem Update nicht mehr starten -  
            haben Sie die M&ouml;glichkeit den urspr&uuml;nglichen Zustand wieder herzustellen.
        </p>
        <p>
            <form action="'$(href extra oscam do_oscambackup)'"><div class="btn"><input type="submit" value="OSCam wiederherstellen" style="width:180px"></div></form>
        </p>'
    sec_end
fi

echo '
    <p>
        <input type="checkbox" name="expertchk" value="no" onclick='\''document.getElementById("expertchk_show").style.display=(this.checked)? "" : "none"'\''> 
        Zusatz-Optionen anzeigen
    </p>'

echo '<div id="expertchk_show" style="display:none;margin-left:0px;" name="expertchk_show">'

sec_begin 'OSCam-Konfiguration sichern oder wiederherstellen'
    echo '
    <h1>Sicherung</h1>
    <p>
        Sichern der aktuellen OSCam-Konigurationsdateien als Archiv auf Ihrem PC.
    </p>
    <form action="'$(href extra oscam do_configbackup)'" method="GET">
        <p><input type=submit value="Sichern" style="width:180px"></p>
    </form>

    <h1>Wiederherstellung</h1>
    <p>
        Wiederherstellen der OSCam-Konfiguration aus einem zuvor gesicherten Archiv.
    </p>
    <form action="'$(href extra oscam do_configrestore)'" method="POST" enctype="multipart/form-data">
        <p><input type="file" size="50" name="uploadfile"></p>
        <p><input type="checkbox" name="replace" id="replace"><label for="replace">Pfade in oscam.conf (logfile, httpcss) automatisch anpassen</label></p>
        <p><input type="checkbox" name="restart" id="restart" checked><label for="restart">OSCam-Neustart nach Wiederherstellung</label></p>
        <p><input type="submit" value="Wiederherstellen" style="width:180px"></p>
    </form>'
sec_end

sec_begin 'Speicher bereinigen'
    echo '
    <p>
        Bei (zu) geringem Speicherplatz sollten Sie vorhandene Binaries, 
        SoftCam.Key, Skins, Logdateien und Konfigurationsbackups entfernen. 
    </p>
    <form action="'$(href extra oscam do_cleanup)'" method="POST" enctype="multipart/form-data">
        <p><input type="submit" value="Bereinigen" style="width:180px"></p>
    </form>'
sec_end

if [ -e "$WORKING_DIR/$DAEMON" ]; then
    sec_begin 'list_smargo installieren/aktualisieren'
        echo '
        <p>
            <b>ACHTUNG!</b> Dieser Schritt ist optional und kann ggf. &uuml;bersprungen werden.
        </p>
        <p>
            Laden Sie eine passende <b>list_smargo-...-mips-freetz-...</b> zur Box hoch. 
            Die Datei darf <b>nicht umbenannt</b> werden.
        </p>
        <form action="'$(href extra oscam do_listexternal)'" method="POST" enctype="multipart/form-data">
            <p><input type="file" size="50" name="list_smargo"></p>
            <p><input type="submit" value="list_smargo aktualisieren" style="width:180px"></p>
        </form>'
    sec_end

    sec_begin 'SoftCam.Key installieren/aktualisieren'
        echo '
        <p>
            Laden Sie eine passende <b>SoftCam.Key</b> zur Box hoch. 
            Die Datei darf <b>nicht umbenannt</b> werden.
        </p>
        <form action="'$(href extra oscam do_softcamkeyexternal)'" method="POST" enctype="multipart/form-data">
            <p><input type="file" size="50" name="softcamkey" ></p>
            <p><input type="submit" value="SoftCam.Key aktualisieren" style="width:180px"></p>
        </form>'
    sec_end
fi  
else
echo '
<p>OSCam-Setup steht erst nach Installation der OSCam Konfigurationsdateien zur Verfügung.</p>
<hr />'  
fi

#echo '</div><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="Zur&uuml;ck"></div></form>'
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="Zur&uuml;ck"></div></form>'


cgi_end
