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

OSC_LOG=$(grep -i "^logfile" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_LOGIN=$(grep -i "^httpuser" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_PW=$(grep -i "^httppwd" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_PORT=$(grep -i "^httpport" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_MAXLOGSIZE=$(grep -i "^maxlogsize" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_HTTPALLOWED=$(grep -i "^httpallowed" "$WORKING_DIR/oscam.conf" | cut -d "=" -f2 | sed 's/^ //')
OSC_LABEL=$(echo $FORM_card_label | cut -d " " -f1)
OSC_CAID=$(echo $FORM_card_label | cut -d " " -f2)
OSC_TEMP="/tmp/tempfile"
SEP_LINE="##############################################"

OSC_IP="127.0.0.1"


cgi --id=extra:oscam:oscamtools
cgi_begin '$(lang de:"Fusebyte-Payload-Abfrage" en:"Fusebyte Payload Query")'
%>
<p><b>$(lang de:"Fusebyte-Payload-Abfrage" en:"Fusebyte Payload Query"):</b></p>
	<p>
	<p>$(lang de:"Die Abfrage f&uuml;r Karte <b><% echo -n $OSC_LABEL %></b> wird gestartet. Dauer: ca. 20 Sek." en:"The query for card <b><% echo -n $OSC_LABEL %></b> is started. Duration: about 20 sec.")</p>
	<p><pre><%
		echo "$SEP_LINE"
		curl -s --digest -o - -u $OSC_LOGIN:$OSC_PW "http://$OSC_IP:$OSC_PORT/status.html?debug=65535" >/dev/null 2>&1
		echo "## $(lang de:"Setze Debug-Level auf 65535 ..." en:"Setting debug level to 65535 ...")"
		echo "$SEP_LINE"

		curl -s --digest -o - -u $OSC_LOGIN:$OSC_PW "http://$OSC_IP:$OSC_PORT/readers.html?label=$OSC_LABEL&action=disable" >/dev/null 2>&1
		echo "## $(lang de:"$OSC_LABEL ausgeschaltet. Warte 1 Sekunde ..." en:"$OSC_LABEL disabled ... waiting 1 second ...")"

		sleep 1

		curl -s --digest -o - -u $OSC_LOGIN:$OSC_PW "http://$OSC_IP:$OSC_PORT/readers.html?label=$OSC_LABEL&action=enable"  >/dev/null 2>&1
		echo "## $(lang de:"$OSC_LABEL eingeschaltet. Warte 15 Sekunden ..." en:"$OSC_LABEL enabled. Waiting 15 seconds ...")"

		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
		curl -s -u "$OSCAM_RESI_USER:$OSCAM_RESI_PASSWORD" -d "text=Fusebyte%20und%20Payload%20Abfrage%20wurde%20gestartet\n\nStarte%20den%20Smartcard-Reader%20neu!&type=1&timeout=10" "http://$OSCAM_RESI_IP:$OSCAM_RESI_PORT/web/message" > $OSC_TEMP
		rm -f $OSC_TEMP
		fi

		sleep 15

		echo "$SEP_LINE"
		echo "## $(lang de:"Pr&uuml;fe Fusebyte ..." en:"Checking Fusebyte ...")"
		grep -A 2 -B 1 "15 48 " $OSC_LOG | grep -A 1 "Answer from cardreader" | grep -A 1 "$OSC_LABEL " | tail -n 1 | tail -c 49 > $OSC_TEMP
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
		fusebyte=$(cut -c 7-8 $OSC_TEMP | tail -n 2)
		fi

		if  [ -s $OSC_TEMP ]; then
			cat $OSC_TEMP | tail -n 2
			echo "$SEP_LINE"

			MATCH=$(cat $OSC_TEMP | grep -o "15 48 ..")
			echo "$(lang de:"Gefunden: " en:"Found: ")"$MATCH
			case $MATCH in
				"15 48 00") echo "=> Virgin" ;;
				"15 48 05") echo "=> Active" ;;
				"15 48 25") echo "=> Married/Activated" ;;
			esac
			rm -f $OSC_TEMP
		else
			echo "$SEP_LINE"
			echo "$(lang de:"Keine Fusebyte-Info gefunden." en:"No fusebyte info found.")"
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
		fusebyte="Keine Fusebyte-Info gefunden."
		fi
		fi

		echo "$SEP_LINE"
		if  [ "$OSC_CAID" = "09C4" ]; then
			echo "## $(lang de:"Pr&uuml;fe Payload V13 ..." en:"Checking payload V13 ...")"
			cat $OSC_LOG | grep -A 0 -B 3 "00 0F 04 " | grep Dec | tail -n 1 | tail -c 18 >> $OSC_TEMP
			cat $OSC_LOG | grep -A 0 -B 3 "00 0F 04 " | tail -n 1 | tail -c 31 >> $OSC_TEMP
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
			payload=$(cat $OSC_TEMP | tail -n 2)
		fi

			if  [ -s $OSC_TEMP ]; then
				cat $OSC_TEMP | tail -n 2
				echo "$SEP_LINE"

				MATCH=$(cat $OSC_TEMP | grep -o "0F 04 .. .. ..")
				echo "$(lang de:"Gefunden: " en:"Found: ")"$MATCH
				case $MATCH in
					"0F 04 02 30 20") echo "=> $(lang de:"Vor dem Aktivieren der Karte" en:"Before card activation")" ;;
					"0F 04 00 10 20") echo "=> $(lang de:"Karte aktiviert (1. EMM geschrieben) aber noch ohne Entitlements (2. EMM fehlt)" en:"Card activated (1.EMM written) but without entitlements (2. EMM missing)")" ;;
					"0F 04 00 00 00") echo "=> $(lang de:"Karte aktiviert und mit Entitlements versorgt" en:"Card activated und provisioned with entitlements")" ;;
					"0F 04 00 10 00") echo "=> $(lang de:"Karte gepairt" en:"Card paired")" ;;
					"0F 04 00 00 20") echo "=> $(lang de:"Karte mit falschem/verf&auml;lschtem EMM zerst&ouml;rt /ODER/ Karte deaktiviert/gesperrt" en:"Card destroyed with wrong/forged EMM /OR/ card deactivated/blocked")" ;;
					"0F 04 02 00 00") echo "=> $(lang de:"Schreibe Tiers..." en:"Writing tiers...")" ;;
				esac
				rm -f $OSC_TEMP
			else
				echo "$SEP_LINE"
				echo "$(lang de:"Keine Payload-Info gefunden." en:"No payload info found.")"
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
			payload="Keine Payload-Info gefunden."
		fi
			fi
		elif [ "$OSC_CAID" = "098C" ]; then
			echo "## $(lang de:"Pr&uuml;fe Payload V14 ..." en:"Checking payload V14 ...")"
			cat $OSC_LOG | grep -A 0 -B 3 "00 0F 06 " | grep Dec | tail -n 1 | tail -c 18 >> $OSC_TEMP
			cat $OSC_LOG | grep -A 0 -B 3 "00 0F 06 " | tail -n 1 | tail -c 31 >> $OSC_TEMP
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
		payload=$(cat $OSC_TEMP | tail -n 2)
		fi

			if  [ -s $OSC_TEMP ]; then
				cat $OSC_TEMP | tail -n 2
				echo "$SEP_LINE"

				MATCH=$(cat $OSC_TEMP | grep -o "0F 06 .. .. ..")
				echo "$(lang de:"Gefunden: " en:"Found: ")"$MATCH
				case $MATCH in
					"0F 06 02 30 20") echo "=> $(lang de:"Vor dem Aktivieren der Karte" en:"Before card activation")" ;;
					"0F 06 00 10 20") echo "=> $(lang de:"Karte aktiviert (1. EMM geschrieben) aber noch ohne Entitlements (2. EMM fehlt)" en:"Card activated (1.EMM written) but without entitlements (2. EMM missing)")" ;;
					"0F 06 00 00 00") echo "=> $(lang de:"Karte aktiviert und mit Entitlements versorgt" en:"Card activated und provisioned with entitlements")" ;;
					"0F 06 00 10 00") echo "=> $(lang de:"Karte gepairt" en:"Card paired")" ;;
					"0F 06 00 00 20") echo "=> $(lang de:"Karte mit falschem/verf&auml;lschtem EMM zerst&ouml;rt /ODER/ Karte deaktiviert/gesperrt" en:"Card destroyed with wrong/forged EMM /OR/ card deactivated/blocked")" ;;
					"0F 06 02 00 00") echo "=> $(lang de:"Schreibe Tiers..." en:"Writing tiers...")"
					;;
				esac
				rm -f $OSC_TEMP
			else
				echo "$SEP_LINE"
				echo "$(lang de:"Keine Payload-Info gefunden." en:"No payload info found.")"
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
			payload="Keine Payload-Info gefunden."
		fi
			fi
		fi

		echo "$SEP_LINE"
		curl -s --digest -o - -u $OSC_LOGIN:$OSC_PW "http://$OSC_IP:$OSC_PORT/status.html?debug=0" >/dev/null 2>&1
		echo "## $(lang de:"Setze Debug-Level auf 0 ... " en:"Setting debug level to 0 ...")"
		echo "$SEP_LINE"
		echo "$(lang de:"Fertig." en:"Done.")"
		if [ "$OSCAM_CHECK_RESI" = "yes" ]; then
		curl -s -u "$OSCAM_RESI_USER:$OSCAM_RESI_PASSWORD" -d "text=FuseByte\n$fusebyte\n\n$payload&type=1&timeout=20" "http://$OSCAM_RESI_IP:$OSCAM_RESI_PORT/web/message" > $OSC_TEMP
		rm -f $OSC_TEMP
		fi

	%></pre></p>


<p>$(lang de:"Sollte mal keine Fusebyte/Payload-Infos gefunden werden: Vorraussetzungen pr&uuml;fen." en:"In case no fusebyte/payload info is found: check prerequisites.")</p>
<p>$(lang de:"Danach die Abfrage wiederholen." en:"Then repeat the query.")</p>

<p>
	<form action="/cgi-bin/extra/oscam/oscamtools"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>
</p>

<% cgi_end %>
