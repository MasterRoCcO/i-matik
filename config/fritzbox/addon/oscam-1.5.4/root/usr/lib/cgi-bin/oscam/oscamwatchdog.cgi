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

check "$OSCAM_DYNCHK" yes:dynchk
check "$OSCAM_CHECK_CAMRUN" yes:check_camrun
check "$OSCAM_DO_CAMRUN" r:do_camrun_r "*":do_camrun_c
check "$OSCAM_SEND_CAMRUN" yes:send_camrun
check "$OSCAM_CHECK_CARDINIT" yes:check_cardinit
check "$OSCAM_DO_CARDINIT" r:do_cardinit_r "*":do_cardinit_c
check "$OSCAM_SEND_CARDINIT" yes:send_cardinit
check "$OSCAM_CHECK_BULKWRITE" yes:check_bulkwrite
check "$OSCAM_DO_BULKWRITE" r:do_bulkwrite_r "*":do_bulkwrite_c
check "$OSCAM_CHECK_CUSTOMERR" yes:check_customerr
check "$OSCAM_DO_CUSTOMERR" r:do_customerr_r "*":do_customerr_c       
check "$OSCAM_SEND_BULKWRITE" yes:send_bulkwrite
check "$OSCAM_SEND_CUSTOMERR" yes:send_customerr  
check "$OSCAM_SEND_DYNDNS" yes:send_dyndns
check "$OSCAM_SEND_REBOOT" yes:send_reboot


select "$OSCAM_DO_PROVIDER" dyndns:dyndns noip:noip dnsomatic:dnsomatic dynserv:dynserv twodns:twodns custom:custom
select "$OSCAM_CHECKING_INTERVAL" 1:val_1 2:val_2 3:val_3 4:val_4 5:val_5 10:val_10 15:val_15 20:val_20 25:val_25 30:val_30 35:val_35 40:val_40 45:val_45 50:val_50 55:val_55 60:val_60

#cgi --id=cgi --id=extra:oscam:oscamwatchdog
cgi_begin '$(lang de:"OSCam-Watchdog" en:"OSCam Watchdog")'

if [ -e "$WORKING_DIR/$DAEMON" ]; then

#echo '<form method="post" action="'$(href conf oscam)'">'
echo '<form method="post" action="'/cgi-bin/conf/oscam'">'

echo '
<h1>$(lang de:"OSCam-Watchdog einrichten" en:"OSCam Watchdog Setup")</h1>
<p>
    $(lang de:"Hier k&ouml;nnen Sie die Watchdog-Einstellungen zur &Uuml;berwachung des OSCam Dienstes anpassen." en:"Here you may adapt the watchdog settings to monitor the OSCam service.")
</p>'

sec_begin '$(lang de:"Watchdog-Einstellungen" en:"Watchdog Settings")'
cat << EOF
  <table>
    <tr height="35px">
      <td colspan="3">
        $(lang de:"Pr&uuml;fintervall:" en:"Check interval:")
        <select name="CHECKING_INTERVAL" id="i1" size="1">
            <option value="1"$val_1_sel>1 min.</option>
            <option value="2"$val_2_sel>2 min.</option>
            <option value="3"$val_3_sel>3 min.</option>
            <option value="4"$val_4_sel>4 min.</option>
            <option value="5"$val_5_sel>5 min.</option>
            <option value="10"$val_10_sel>10 min.</option>
            <option value="15"$val_15_sel>15 min.</option>
            <option value="20"$val_20_sel>20 min.</option>
            <option value="25"$val_25_sel>25 min.</option>
            <option value="30"$val_30_sel>30 min.</option>
            <option value="35"$val_35_sel>35 min.</option>
            <option value="40"$val_40_sel>40 min.</option>
            <option value="45"$val_45_sel>45 min.</option>
            <option value="50"$val_50_sel>50 min.</option>
            <option value="55"$val_55_sel>55 min.</option>
            <option value="60"$val_60_sel>60 min.</option>
        </select>
      </td>
    </tr>
    <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_CAMRUN" value="no">
        <input id="w1" type="checkbox" name="CHECK_CAMRUN" value="yes"$check_camrun_chk><label for="w1"> $(lang de:"Softcam Aktivit&auml;t pr&uuml;fen" en:"Check softcam activity")</label>
      </td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Bei Ausfall: Neustart von" en:"On failure: restart")</td>
      <td>
        <input id="w11" type="radio" name="DO_CAMRUN" value="c"$do_camrun_c_chk><label for="w11"> Softcam</label>
        <input id="w12" type="radio" name="DO_CAMRUN" value="r"$do_camrun_r_chk><label for="w12"> Router</label>
      </td>
    </tr>
    </tr>
    <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_CARDINIT" value="no">
        <input id="w2" type="checkbox" name="CHECK_CARDINIT" value="yes"$check_cardinit_chk><label for="w2"> $(lang de:"Karten Initialisierung pr&uuml;fen" en:"Check card initialization")</label>
      </td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Bei Fehler: Neustart von" en:"On error: restart")
      <td>
        <input id="w21" type="radio" name="DO_CARDINIT" value="c"$do_cardinit_c_chk><label for="w21"> Softcam</label>
        <input id="w22" type="radio" name="DO_CARDINIT" value="r"$do_cardinit_r_chk><label for="w22"> Router</label>
      </td>
    </tr>
    <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_BULKWRITE" value="no">
        <input id="w3" type="checkbox" name="CHECK_BULKWRITE" value="yes"$check_bulkwrite_chk><label for="w3"> $(lang de:"USB (bulkwrite) pr&uuml;fen" en:"Check USB (bulk write)")</label>
      </td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Bei Fehler: Neustart von" en:"On error: restart")</td>
      <td>
        <input id="w31" type="radio" name="DO_BULKWRITE" value="c"$do_bulkwrite_c_chk><label for="w31"> Softcam</label>
        <input id="w32" type="radio" name="DO_BULKWRITE" value="r"$do_bulkwrite_r_chk><label for="w32"> Router</label>
      </td>
    </tr>
    <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="CHECK_CUSTOMERR" value="no">
        <input id="w4" type="checkbox" name="CHECK_CUSTOMERR" value="yes"$check_customerr_chk><label for="w4"> $(lang de:"Benutzerdefinierten Fehler pr&uuml;fen" en:"Check custom error")</label>
      </td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Suchtext: " en:"Search text: ")
        <input type="text" name="TEXT_CUSTOMERR" size="35" value="$(html "$OSCAM_TEXT_CUSTOMERR")">
      </td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Bei Fehler: Neustart von" en:"On error: restart")</td>
      <td>
        <input id="w41" type="radio" name="DO_CUSTOMERR" value="c"$do_customerr_c_chk><label for="w41"> Softcam</label>
        <input id="w42" type="radio" name="DO_CUSTOMERR" value="r"$do_customerr_r_chk><label for="w42"> Router</label>
      </td>
    </tr>
    <tr height="35px">
      <td colspan="3">
        <input type="hidden" name="DYNCHK" value="no">
        <input id="w5" type="checkbox" name="DYNCHK" value="yes"$dynchk_chk><label for="w5"> $(lang de:"DynDns Updatefunktion aktivieren" en:"Enable DynDNS update function") </label>
      </td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td colspan="2">
        $(lang de:"Anbieter w&auml;hlen:" en:"Select provider:")
        <select onChange="onchangeAction(this)" name="DO_PROVIDER" id="w11" size="1">
             <option value="dyndns"$dyndns_sel>DynDNS</option>
             <option value="noip"$noip_sel>No-IP</option>
             <option value="dnsomatic"$dnsomatic_sel>DNS-O-Matic</option>
             <option value="dynserv"$dynserv_sel>DynServ</option>
             <option value="twodns"$twodns_sel>Two-DNS</option>
             <option value="custom"$custom_sel>$(lang de:"Benutzerdefiniert" en:"User defined")</option>
        </select>
        <script>
            function onchangeAction(sel){
                var provider = sel.value;
                if(provider == "custom") {
                    document.getElementById("HOST_UURL").disabled=false;
                    document.getElementById("HOST_UURL_HELP").style.display='';
                    document.getElementById("HOST_UURL_INPUT").style.display='';
                } else {
                    document.getElementById("HOST_UURL").disabled=true;
                    document.getElementById("HOST_UURL_HELP").style.display='none';
                    document.getElementById("HOST_UURL_INPUT").style.display='none';
                }
            }
        </script> 
      </td>
    </tr>
    <tr height="35px" id="HOST_UURL_HELP" style="display:$([ "$OSCAM_DO_PROVIDER" != "custom" ] && echo 'none' || echo '');">
      <td style="width: 25px"></td>
      <td colspan="2"><font size="2">$(lang de:"Hier k&ouml;nnen Sie die Update-URL Ihres Dynamic-DNS-Anbieters eintragen. Verwendbare Platzhalter sind: &lt;user&gt;=Benutzer; &lt;pass&gt;=Passwort; &lt;host&gt;=Host" en:"Here you may enter the update URL of your dynamic DNS provider. Variables are: &lt;user&gt;=user; &lt;pass&gt;=password; &lt;host&gt;=host")</font></td>
    </tr>
    <tr height="35px" id="HOST_UURL_INPUT" style="display:$([ "$OSCAM_DO_PROVIDER" != "custom" ] && echo 'none' || echo '');">
      <td style="width: 25px"></td>
      <td>$(lang de:"Update-URL:" en:"Update URL:")</td>
      <td><input type="text" id="HOST_UURL" name="HOST_UURL" size="35" value="$(html "$OSCAM_HOST_UURL")"$([ "$OSCAM_DO_PROVIDER" != "custom" ] && echo ' disabled')></td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Host:" en:"Host:")</td>
      <td><input type="text" name="HOST" size="35" value="$(html "$OSCAM_HOST")"></td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Benutzer:" en:"User:")</td>
      <td><input type="text" name="HOST_USER" size="35" value="$(html "$OSCAM_HOST_USER")"></td>
    </tr>
    <tr height="35px">
      <td style="width: 25px"></td>
      <td>$(lang de:"Passwort:" en:"Password:")</td>
      <td><input type="password" name="HOST_PASS" size="35" value="$(html "$OSCAM_HOST_PASS")"></td>
    </tr>
  </table>
  <hr />
  <h1>$(lang de:"E-Mail Benachrichtigung" en:"E-Mail Notification")</h1>
  <table>
    <tr height="35px">
      <td>
        <input type="hidden" name="SEND_CAMRUN" value="no">
        <input id="s1" type="checkbox" name="SEND_CAMRUN" value="yes"$send_camrun_chk><label for="s1"> $(lang de:"Softcam Ausfall" en:"Softcam failure")</label>
      </td>
    </tr>
    <tr height="35px">
      <td>
        <input type="hidden" name="SEND_CARDINIT" value="no">
        <input id="s2" type="checkbox" name="SEND_CARDINIT" value="yes"$send_cardinit_chk><label for="s2"> $(lang de:"Karteninitialisierung" en:"Card initialization")</label>
      </td>
    </tr>
    <tr height="35px">
      <td>
        <input type="hidden" name="SEND_BULKWRITE" value="no">
        <input id="s3" type="checkbox" name="SEND_BULKWRITE" value="yes"$send_bulkwrite_chk><label for="s3"> $(lang de:"USB (bulkwrite)" en:"USB (bulkwrite)")</label>
      </td>
    </tr>
    <tr height="35px">
      <td>
        <input type="hidden" name="SEND_CUSTOMERR" value="no">
        <input id="s1" type="checkbox" name="SEND_CUSTOMERR" value="yes"$send_customerr_chk><label for="s1"> $(lang de:"Benutzerdefinierter Fehler" en:"Custom error")</label>
      </td>
    </tr>
    <tr height="35px">
      <td>
        <input type="hidden" name="SEND_REBOOT" value="no">
        <input id="s4" type="checkbox" name="SEND_REBOOT" value="yes"$send_reboot_chk><label for="s4"> $(lang de:"Router Neustart" en:"Router restart")</label>
      </td>
    </tr>
    <tr height="35px">
      <td>
        <input type="hidden" name="SEND_DYNDNS" value="no">
        <input id="s5" type="checkbox" name="SEND_DYNDNS" value="yes"$send_dyndns_chk><label for="s5"> $(lang de:"DynDns Update-Funktion" en:"DynDns update function") </label>
      </td>
    </tr>
  </table>
  <hr />
  <h1>$(lang de:"E-Mail Konfiguration" en:"E-Mail Configuration")</h1>
  <table>
      <tr height="35px">
          <td>$(lang de:"Absender E-Mail:" en:"Sender e-mail:")</td>
          <td><input id="EMAIL_FROM" type="text" name="MAIL_FROM" value="$(html "$OSCAM_MAIL_FROM")"></td>
      </tr>
      <tr height="35px">
          <td>$(lang de:"Empf&auml;nger E-Mail:" en:"Recipient e-mail:")</td>
          <td><input id="EMAIL_TO" type="text" name="MAIL_TO" value="$(html "$OSCAM_MAIL_TO")"></td>
      </tr>
      <tr height="35px">
          <td>$(lang de:"SMTP Server:" en:"SMTP server:")</td>
          <td><input id="EMAIL_SERVER" type="text" name="MAIL_SERVER" value="$(html "$OSCAM_MAIL_SERVER")"></td>
      </tr>
      <tr height="35px">
          <td>$(lang de:"SMTP Benutzername:" en:"SMTP user name:")</td>
          <td><input id="EMAIL_USER" type="text" name="MAIL_USER" value="$(html "$OSCAM_MAIL_USER")"></td>
      </tr>
      <tr height="35px">
          <td>$(lang de:"SMTP Benutzerpasswort:" en:"SMTP user password:")</td>
          <td><input id="EMAIL_PASSWORD" type="password" name="MAIL_PASSWORD" value="$(html "$OSCAM_MAIL_PASSWORD")"></td>
      </tr>
  </table>
EOF
sec_end

echo '<div class="btn"><input type="submit" value="$(lang de:"&Uuml;bernehmen" en:"Apply")"></div></form>'

#echo '</div><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'

echo '<form method="post" action="'$(href extra oscam do_testmail)'">
      	  <input type="hidden" id="from" name="from" value="from">
      	  <input type="hidden" id="to" name="to" value="to">
      	  <input type="hidden" id="server" name="server" value="server">
      	  <input type="hidden" id="user" name="user" value="user">
      	  <input type="hidden" id="password" name="password" value="password">
      	  <div class="btn"><input type="submit" value="$(lang de:"Test E-mail senden" en:"Send test e-mail")" onclick="onclickAction()"></div>
      </form>
      <script>
          function onclickAction(){
              var from=document.getElementById("EMAIL_FROM").value;
              var to=document.getElementById("EMAIL_TO").value;
              var server=document.getElementById("EMAIL_SERVER").value;
              var user=document.getElementById("EMAIL_USER").value;
              var password=document.getElementById("EMAIL_PASSWORD").value;
              document.getElementById("from").value=from;
              document.getElementById("to").value=to;
              document.getElementById("server").value=server;
              document.getElementById("user").value=user;
              document.getElementById("password").value=password;
          }
      </script>'
else
echo '
<p>$(lang de:"OSCam-Watchdog steht erst nach Installation der OSCam-Binary zur Verfügung." en:"OSCam-Watchdog are only available after installing the OSCam binary.")</p>
<hr />'
#echo '</div><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'
echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'

fi
cgi_end


