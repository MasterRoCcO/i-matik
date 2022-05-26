#!/usr/bin/haserl -u 2048 -U /var/tmp
<%
PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg

SUBJECT='$(lang de:"OSCam Watchdog Testmail" en:"OSCam watchdog test mail")'

cgi --id=extra:oscam:oscamwatchdog
cgi_begin '$(lang de:"Testmail" en:"Test mail")'
%>
<h1>$(lang de:"Testmail senden" en:"Send test mail")</h1>

<% if [ -n "$FORM_from" ] && [ -n "$FORM_to" ] && [ -n "$FORM_server" ] && [ -n "$FORM_user" ] && [ -n "$FORM_password" ]; then %>
	<p>$(lang de:"Es wird eine Testmail mit den eingestellten Parametern versendet." en:"A test mail is sent with the configured settings.")
	</p>
	<p><b>$(lang de:"Verlauf" en:"Progress"):</b></p>
	<p><pre><%
		echo '$(lang de:"Parameter:" en:"Settings:")'
		echo ' --- $(lang de:"Absender E-Mail:" en:"Sender e-mail:")' "$FORM_from"
		echo ' --- $(lang de:"Empf&auml;nger E-Mail:" en:"Recipient e-mail:")' "$FORM_to"
		echo ' --- $(lang de:"SMTP Server:" en:"SMTP server:")' "$FORM_server"
		echo ' --- $(lang de:"SMTP Benutzername:" en:"SMTP user name:")' "$FORM_user"
		echo ' --- $(lang de:"SMTP Benutzerpasswort:" en:"SMTP user password:")' "$FORM_password"
		echo ' --- $(lang de:"Betreff:" en:"Subject:")' "$SUBJECT"
		echo ''

		echo -n '$(lang de:"Testmail wird gesendet ... " en:"Sending test mail ...")'

		mailer -s "$SUBJECT" -f $FORM_from -t $FORM_to -m $FORM_server -a $FORM_user -w $FORM_password &

		echo '$(lang de:"fertig." en:"done.")'
		echo ''

		echo '$(lang de:"Die Testmail wurde versendet. &Uuml;berpr&uuml;fen Sie den Posteingang." en:"The test mail was sent. Check the inbox.")'
	%></pre></p>
<% else %>
	<p>$(lang de:"Einstellungen unvollst&auml;ndig. Bitte geben Sie alle Parameter an." en:"Insufficient data. Please specify all settings.")<p>
<% fi %>

<p>
	<font size="2">
	$(lang de:"&quot;Zur&uuml;ck&quot; bringt Sie zur&uuml;ck zur OSCam-Watchdog Seite. Ungesicherte &Auml;nderungen gehen dabei verloren."
	       en:"&quot;Back&quot; takes you back to the OSCam watchdog page. Unsaved changes will be lost.")<br>
	$(lang de:"Mit &quot;&Uuml;bernehmen&quot; (nur bei ungesicherten &Auml;nderungen sichtbar) werden die Watchdog-E-Mail-Parameter gesichert und es geht zur&uuml;ck zur Hauptseite."
	       en:"&quot;Apply&quot; (visible only in case of unsaved changes) will save the watchdog e-mail settings and return to the main page.")
	</font>
</p>
<p>
	<form action="/cgi-bin/extra/oscam/oscamwatchdog">
        	<div class="btn">
            		<input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")">
        	</div>
        </form>
<% if [ "$FORM_from" != "$OSCAM_MAIL_FROM" ] || [ "$FORM_to" != "$OSCAM_MAIL_TO" ] || [ "$FORM_server" != "$OSCAM_MAIL_SERVER" ] || [ "$FORM_user" != "$OSCAM_MAIL_USER" ] || [ "$FORM_password" != "$OSCAM_MAIL_PASSWORD" ]; then %>
	<form method="post" action="/cgi-bin/conf/oscam">
      		<input type="hidden" name="MAIL_FROM" value="<% echo "$FORM_from" %>">
      		<input type="hidden" name="MAIL_TO" value="<% echo "$FORM_to" %>">
      		<input type="hidden" name="MAIL_SERVER" value="<% echo "$FORM_server" %>">
      		<input type="hidden" name="MAIL_USER" value="<% echo "$FORM_user" %>">
      		<input type="hidden" name="MAIL_PASSWORD" value="<% echo "$FORM_password" %>">
		<div class="btn">
			<input type="submit" value="$(lang de:"&Uuml;bernehmen" en:"Apply")">
		</div>
	</form>
<% fi %>
</p>

<% cgi_end %>
