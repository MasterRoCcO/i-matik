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


check "$OSCAM_CHECK_RESI" yes:check_resi

OSC_LOG=$(grep -i "^logfile" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_LOGIN=$(grep -i "^httpuser" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_PW=$(grep -i "^httppwd" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_PORT=$(grep -i "^httpport" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_MAXLOGSIZE=$(grep -i "^maxlogsize" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_HTTPALLOWED=$(grep -i "^httpallowed" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')

check "$OSCAM_CHECK_UDEV1" yes:check_udev1
check "$OSCAM_CHECK_UDEV2" yes:check_udev2
check "$OSCAM_CHECK_UDEV3" yes:check_udev3
check "$OSCAM_CHECK_UDEV4" yes:check_udev4
check "$OSCAM_CHECK_UDEV5" yes:check_udev5

DEVICE="/var/devices"
UDEV="/etc/udev"

#smartreader
SMARTREADER1=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '1p')
SMARTREADER2=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '2p')
SMARTREADER3=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '3p')
SMARTREADER4=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '4p')
SMARTREADER5=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '5p')
SMARTREADER6=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '6p')
SMARTREADER7=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '7p')
SMARTREADER8=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '8p')
SMARTREADER9=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '9p')
SMARTREADER10=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '10p')

#smartreaderplus
PRODUKT1=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '1p')
PRODUKT2=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '2p')
PRODUKT3=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '3p')
PRODUKT4=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '4p')
PRODUKT5=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '5p')
PRODUKT6=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '6p')
PRODUKT7=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '7p')
PRODUKT8=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '8p')
PRODUKT9=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '9p')
PRODUKT10=$(cat $DEVICE | grep Product= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '10p')

#easymouse
MANUFACRURER1=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '1p')
MANUFACRURER2=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '2p')
MANUFACRURER3=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '3p')
MANUFACRURER4=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '4p')
MANUFACRURER5=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '5p')
MANUFACRURER6=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '6p')
MANUFACRURER7=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '7p')
MANUFACRURER8=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '8p')
MANUFACRURER9=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '9p')
MANUFACRURER10=$(cat $DEVICE | grep Manufacturer= | cut -d "=" -f2 |cut -d " " -f1 | cut -c 1- | sed -n '10p')

#serial
READERSERIAL1=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '1p')
READERSERIAL2=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '2p')
READERSERIAL3=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '3p')
READERSERIAL4=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '4p')
READERSERIAL5=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '5p')
READERSERIAL6=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '6p')
READERSERIAL7=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '7p')
READERSERIAL8=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '8p')
READERSERIAL9=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '9p')
READERSERIAL10=$(cat $DEVICE | grep SerialNumber= | cut -d "=" -f2 | cut -c 1- | sed -n '10p')


#cgi --id=cgi --id=extra:oscam:oscamtools
cgi_begin '$(lang de:"OSCam-Tools" en:"OSCam tools")'

if [ -e "$WORKING_DIR/$DAEMON" ]; then


if [ -e "$WORKING_DIR/$DAEMON" ] && [ -e "$DEVICE" ]; then
sec_begin '$(lang de:"Serialanzeige Cardreader" en:"Serialdisplay Cardreader")'
echo '<p>$(lang de:"Hier werden euch die Serial alle angeschlossenen Cardreader angezeigt" en:"Here you will see the series all connected Cardreader")</p>'
echo '<p>$(lang de:"Für Smargo ab 1.4 Firmware, Smargo V2 und Easymouse 2" en:"For Smargo 1.4 Firmware, Smargo V2 and Easymouse 2")</p>'

if [ "$SMARTREADER1" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL1")'" disabled></p>'
else
if [ "$MANUFACRURER1" = "FTDI" ] && [ "$PRODUKT1" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL1")'" disabled></p>'
else
if [ "$MANUFACRURER1" = "Argolis" ] && [ "$PRODUKT1" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL1")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER2" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL2")'" disabled></p>'
else
if [ "$MANUFACRURER2" = "FTDI" ] && [ "$PRODUKT2" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL2")'" disabled></p>'
else
if [ "$MANUFACRURER2" = "Argolis" ] && [ "$PRODUKT2" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL2")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER3" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL3")'" disabled></p>'
else
if [ "$MANUFACRURER3" = "FTDI" ] && [ "$PRODUKT3" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL3")'" disabled></p>'
else
if [ "$MANUFACRURER3" = "Argolis" ] && [ "$PRODUKT3" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL3")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER4" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL4")'" disabled></p>'
else
if [ "$MANUFACRURER4" = "FTDI" ] && [ "$PRODUKT4" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL4")'" disabled></p>'
else
if [ "$MANUFACRURER4" = "Argolis" ] && [ "$PRODUKT4" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL4")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER5" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL5")'" disabled></p>'
else
if [ "$MANUFACRURER5" = "FTDI" ] && [ "$PRODUKT5" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL5")'" disabled></p>'
else
if [ "$MANUFACRURER5" = "Argolis" ] && [ "$PRODUKT5" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL5")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER6" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL6")'" disabled></p>'
else
if [ "$MANUFACRURER6" = "FTDI" ] && [ "$PRODUKT6" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL6")'" disabled></p>'
else
if [ "$MANUFACRURER6" = "Argolis" ] && [ "$PRODUKT6" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL6")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER7" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL7")'" disabled></p>'
else
if [ "$MANUFACRURER7" = "FTDI" ] && [ "$PRODUKT7" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL7")'" disabled></p>'
else
if [ "$MANUFACRURER7" = "Argolis" ] && [ "$PRODUKT7" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL7")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER8" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL8")'" disabled></p>'
else
if [ "$MANUFACRURER8" = "FTDI" ] && [ "$PRODUKT8" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL8")'" disabled></p>'
else
if [ "$MANUFACRURER8" = "Argolis" ] && [ "$PRODUKT8" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL8")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER9" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL9")'" disabled></p>'
else
if [ "$MANUFACRURER9" = "FTDI" ] && [ "$PRODUKT9" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL9")'" disabled></p>'
else
if [ "$MANUFACRURER9" = "Argolis" ] && [ "$PRODUKT9" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL9")'" disabled></p>'
fi
fi
fi

if [ "$SMARTREADER10" = "Reader" ]; then
echo '<p>$(lang de:"Die Smartreader-Serial lautet:" en:"The Smartreader-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL10")'" disabled></p>'
else
if [ "$MANUFACRURER10" = "FTDI" ] && [ "$PRODUKT10" = "FT232R" ]; then
echo '<p>$(lang de:"Die Easymouse-Serial lautet:" en:"The Easymouse-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL10")'" disabled></p>'
else
if [ "$MANUFACRURER10" = "Argolis" ] && [ "$PRODUKT10" = "Smartreader" ]; then
echo '<p>$(lang de:"Die Smartreaderplus-Serial lautet:" en:"The Smartreaderplus-Serial is:") <input type="text" name="DEVICE" size="20" value="'$(html "$READERSERIAL10")'" disabled></p>'
fi
fi
fi
echo '<p> <ul><li><a href="'$(href extra oscam devices)'">$(lang de:"Serial aller angeschlossenen USB-Geräte" en:"Serial all connected USB devices")</a></li></ul></p>'
sec_end 
fi

if [ "$(/etc/init.d/rc.oscam status)" = 'stopped' ]; then
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'
fi

#echo '<form method="post" action="'$(href conf oscam)'">'
echo '<form method="post" action="'/cgi-bin/conf/oscam'">'
if [ -e "$WORKING_DIR/$DAEMON" ] && [ -e "$UDEV" ]  && [ "$(/etc/init.d/rc.oscam status)" = 'running' ]; then
sec_begin '$(lang de:"Udev-Regel (udev_final)" en:"Udev-Rule (udev_final)")'
echo '<p>$(lang de:"Hier könnt ihr die angeschlossenen Cardreader mit udev_final fest verlinken. Für Smargo ab 1.4 Firmware, Smargo V2 und Easymouse 2." en:"Here you can link the connected cardreader with udev_final. For Smargo 1.4 Firmware, Smargo V2 and Easymouse 2.")</p>'
echo '<p>$(lang de:"In das erste Feld gehört die Serial des Readers. In dem zweitem Feld gebt ihr dem Reader einen Namen." en:"The serial number of the reader belongs to the first field. In the second field you give the reader a name.")</p>'
echo '<p>$(lang de:"Hacken rein bei Udev-Regel aktivieren und Übernehmen. Danach <u>muss</u> die Fritzbox neu gestartet werden." en:"Check the check box for Udev rule and apply. After that the Fritzbox <u>must</u> be restarted.")</p>'
cat << EOF
    <table>
    <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_UDEV1" value="no">
        <input id="w7" type="checkbox" name="CHECK_UDEV1" value="yes"$check_udev1_chk><label for="w7"> $(lang de:"Udev-Regel aktivieren" en:"Udev rule")</label>
      </td>
    </tr>
        <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Serial Reader1: " en:"Reader1:")
        <input type="text" name="TEXT_UDEVREADER1" size="25" value="$(html "$OSCAM_TEXT_UDEVREADER1")">$(lang de:"Bezeichnung: " en:"designation:")<input type="text" name="TEXT_UDEV1" size="25" value="$(html "$OSCAM_TEXT_UDEV1")">
      </td>
    </tr>
        <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_UDEV2" value="no">
        <input id="w7" type="checkbox" name="CHECK_UDEV2" value="yes"$check_udev2_chk><label for="w7"> $(lang de:"Udev-Regel aktivieren" en:"Udev rule")</label>
      </td>
    </tr>
        <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Serial Reader2: " en:"Reader2:")
        <input type="text" name="TEXT_UDEVREADER2" size="25" value="$(html "$OSCAM_TEXT_UDEVREADER2")">$(lang de:"Bezeichnung: " en:"designation:")<input type="text" name="TEXT_UDEV2" size="25" value="$(html "$OSCAM_TEXT_UDEV2")">
      </td>
    </tr>
     <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_UDEV3" value="no">
        <input id="w7" type="checkbox" name="CHECK_UDEV3" value="yes"$check_udev3_chk><label for="w7"> $(lang de:"Udev-Regel aktivieren" en:"Udev rule")</label>
      </td>
    </tr>
        <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Serial Reader3: " en:"Reader3:")
        <input type="text" name="TEXT_UDEVREADER3" size="25" value="$(html "$OSCAM_TEXT_UDEVREADER3")">$(lang de:"Bezeichnung: " en:"designation:")<input type="text" name="TEXT_UDEV3" size="25" value="$(html "$OSCAM_TEXT_UDEV3")">
      </td>
    </tr>
     <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_UDEV4" value="no">
        <input id="w7" type="checkbox" name="CHECK_UDEV4" value="yes"$check_udev4_chk><label for="w7"> $(lang de:"Udev-Regel aktivieren" en:"Udev rule")</label>
      </td>
    </tr>
        <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Serial Reader4: " en:"Reader4:")
        <input type="text" name="TEXT_UDEVREADER4" size="25" value="$(html "$OSCAM_TEXT_UDEVREADER4")">$(lang de:"Bezeichnung: " en:"designation:")<input type="text" name="TEXT_UDEV4" size="25" value="$(html "$OSCAM_TEXT_UDEV4")">
      </td>
    </tr>   
     <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_UDEV5" value="no">
        <input id="w7" type="checkbox" name="CHECK_UDEV5" value="yes"$check_udev5_chk><label for="w7"> $(lang de:"Udev-Regel aktivieren" en:"Udev rule")</label>
      </td>
    </tr>
        <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Serial Reader5: " en:"Reader5:")
        <input type="text" name="TEXT_UDEVREADER5" size="25" value="$(html "$OSCAM_TEXT_UDEVREADER5")">$(lang de:"Bezeichnung: " en:"designation:")<input type="text" name="TEXT_UDEV5" size="25" value="$(html "$OSCAM_TEXT_UDEV5")">
      </td>
    </tr>
      </table>
EOF
echo '<div class="btn"><input type="submit" value="$(lang de:"&Uuml;bernehmen" en:"Apply")"></div></form>'
else
echo '
<p>$(lang de:"Hinweis: Die Udev-Regel steht erst nach Start der OSCam-Binary zur Verfügung." en:"Note: The Udev rule is only available after starting the OSCam binary.")</p>
<hr />'
sec_end 
fi

#echo '<form method="post" action="'$(href conf oscam)'">'
echo '<form method="post" action="'/cgi-bin/conf/oscam'">'
if [ ! "$(/etc/init.d/rc.oscam status)" = 'stopped' ]; then
sec_begin '$(lang de:"Ergebniss der Fusebyte-Payload-Abfrage über ein Receiver (Enigma2) am TV anzeigen lassen" en:"Let the result Fusebyte-payload Show request a Receiver (Enigma2) on TV")'
cat << EOF
  <table>
    <tr height="35px">
    <td colspan="3">
        <input type="hidden" name="CHECK_RESI" value="no">
        <input id="w3" type="checkbox" name="CHECK_RESI" value="yes"$check_resi_chk><label for="w3"> $(lang de:"Dazu den Hacken setzen, die Daten eintragen und auf Übernehmen klicken. Danach Abfrage starten" en:"These set the hook, submit it and click Apply. Then start search")</label></td>
    <tr height="35px">
        <td>$(lang de:"Receiver-IP:" en:"Receiver-IP:")</td>
        <td><input id="RESI_IP" type="text" name="RESI_IP" value="$(html "$OSCAM_RESI_IP")"></td>
        </tr>
    <tr height="35px">
        <td>$(lang de:"Receiver-Webif-Port:" en:"Receiver-Port:")</td>
        <td><input id="RESI_PORT" type="text" name="RESI_PORT" value="$(html "$OSCAM_RESI_PORT")"></td>
        </tr>
    <tr height="35px">
        <td>$(lang de:"Receiver-Webif-User:" en:"Receiver-User:")</td>
        <td><input id="RESI_USER" type="text" name="RESI_USER" value="$(html "$OSCAM_RESI_USER")"></td>
        </tr>
    <tr height="35px">
        <td>$(lang de:"Receiver-Webif-Passwort:" en:"Receiver Password:")</td>
        <td><input id="RESI_PASSWORD" type="password" name="RESI_PASSWORD" value="$(html "$OSCAM_RESI_PASSWORD")"></td>
        </tr>
  </table>
EOF
echo '<div class="btn"><input type="submit" value="$(lang de:"&Uuml;bernehmen" en:"Apply")"></div></form>'
sec_end
fi

if [ ! "$(/etc/init.d/rc.oscam status)" = 'stopped' ]; then 
    sec_begin '$(lang de:"Fusebyte-Payload-Abfrage" en:"Fusebyte Payload Query")'
        echo '
        <p>$(lang de:"Hier besteht die M&ouml;glichkeit sich Fusebyte und Payload seiner NDS-Karte (V13 oder V14) anzeigen zu lassen. Die Zugangsdaten werden aus oscam.conf gelesen." en:"Here you can display the fusebyte and payload of your NDS card. The access data will be read from oscam.conf.")</p>
        <p style="padding: 0px 0px 0px 25px"><font size="2">$(lang de:"<b>Hinweis:</b> Die Log-Gr&ouml;sse der oscam.log sollte mindestens 4 MB betragen. Der Parameter <b>httpallowed</b> muss auf \"127.0.0.1\" oder \"0.0.0.0-255.255.255.255\" gesetzt sein. Den Receiver auf einen Skysender schalten und unten auf \"Abfrage starten\" klicken." en:"<b> Note: </ b> The log size of oscam.log should be at least 4 MB. Parameter <b>httpallowed</b> must be set to \"127.0.0.1\" or \"0.0.0.0-255.255.255.255\". Switch the receiver to a Sky channel and click on \"Start Query\" below.")</font></p>

        <p>
            <b>$(lang de:"Aktuelle Einstellungen:" en:"Current Settings")</b>
            <table style="padding: 0px 0px 0px 25px">
                <tr><td style="width:100px">httpuser:   </td><td>'$OSC_LOGIN'        </td></tr>
                <tr><td style="width:100px">httppwd:    </td><td>'$OSC_PW'           </td></tr>
                <tr><td style="width:100px">httpport:   </td><td>'$OSC_PORT'         </td></tr>
                <tr><td style="width:100px">httpallowed:</td><td>'$OSC_HTTPALLOWED'  </td></tr>
                <tr></tr>
                <tr><td style="width:100px">$(lang de:"Log-Pfad:" en:"Log Path:") </td><td>'$OSC_LOG' </td></tr>
                <tr><td style="width:100px">$(lang de:"Log-Gr&ouml;sse :" en:"Log Size")</td><td>'$OSC_MAXLOGSIZE' kB </td></tr>
            </table>
        <ul><li><a href="'$(href file oscam oscamconf)'">$(lang de:"Einstellungen &auml;ndern" en:"Change settings")</a></li></ul>'

        IFS=$'='
        readers=0

        while read param value; do
            case $param in
                \[reader\]) let readers++ ;;	
                label*)     eval reader_${readers}_label=\${value} ;;
                enable*)    eval reader_${readers}_enable=\${value} ;;
                caid*)      eval reader_${readers}_caid=\${value} ;;
            esac
        done < "$WORKING_DIR/oscam.server"

        unset IFS

        echo '
        <form action="'$(href extra oscam do_fusebyte_payload)'" method="POST" enctype="multipart/form-data">
            <p>
                $(lang de:"Karte w&auml;hlen: " en:"Select card: ")
                <select name="card_label">'
                    i=1; while [[ $i -le $readers ]]; do
                        eval enable=\$reader_${i}_enable
                        enable=$(echo $enable | sed -e 's/^[[:space:]]*//g' -e 's/[[:space:]]*\$//g')
                        if [ "$enable" != "0" ]; then
                            eval caid=\$reader_${i}_caid
                            caid=$(echo $caid | sed -e 's/^[[:space:]]*//g' -e 's/[[:space:]]*\$//g' | tr "[a-z]" "[A-Z]")
                            if [ "$caid" = "098C" ] || [ "$caid" = "09C4" ]; then
                                eval label=\$reader_${i}_label
                                label=$(echo $label | sed -e 's/^[[:space:]]*//g' -e 's/[[:space:]]*\$//g')
                                echo '<option value="'$label' '$caid'">'$label'</option>'
                            fi
                        fi
                        let i++
                    done 

        echo '        </select>
            </p>
            <p><input type="submit" value="$(lang de:"Abfrage starten" en:"Start Query")" style="width:180px"></p>
        </form>'
    sec_end    
fi
else
echo '
<p>$(lang de:"OSCam-Tools steht erst nach Installation der OSCam-Binary zur Verfügung." en:"OSCam-Tools are only available after installing the OSCam binary.")</p>
<hr />'
fi

if [ "$(/etc/init.d/rc.oscam status)" = 'running' ]; then
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'
fi

#echo '</div><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'


cgi_end

