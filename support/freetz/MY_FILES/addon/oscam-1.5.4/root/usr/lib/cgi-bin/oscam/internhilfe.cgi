#!/bin/sh

PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg

cgi --id=conf:oscam:_index
cgi_begin '$(lang de:"Hilfe Intern-Modus" en:"Intenal mode help")'

cat << EOF
<h1>$(lang de:"Hilfe Intern-Modus" en:"Intenal mode help")</h1>

<p>
	$(lang de:"Um den Intern-Modus zu nutzen, muss mind. 1,4MB freier Speicher auf der JFFS2-Partition vorhanden sein." en:"To use internal mode you need at least 1,4MB of available memory in the JFFS2 partition.")
</p>

<ol start="1">
	<li>$(lang de:"Image &uuml;ber das Firmware-Update flashen und die Option JFFS2 Partition l&ouml;schen aktivieren." en:"Flash the image via firmware update and activate option 'Cleanup JFFS2 partition'.")</li>
</ol>
<ul style="padding: 0px 0px 0px 25px">
	<li><a class="active" href="/cgi-bin/update/firmware.cgi">$(lang de:"Firmware-Update" en:"Firmware update")</a></li>
</ul>
<ol start="2">
	<li>$(lang de:"Ist die Option JFFS2 Partition l&ouml;schen nicht vorhanden oder sollte sich der freie Speicher nach dem erneuten Flashen nicht vergr&ouml;ssert haben, kann nur der USB-Modus verwendet werden. Dazu USB-Speicher anschliessen und Fritzbox neu starten." en:"If option 'Cleanup JFFS2 partition' is not available or the amount of available memory has not increased after reflashing, you can only use USB mode. Connect USB memory and restart.")</li>
</ol>
<ul style="padding: 0px 0px 0px 25px">
	<li><a class="active" href="/cgi-bin/system.cgi">$(lang de:"Fritz!Box neustarten" en:"Restart Fritz!Box")</a></li>
</ul>

<p>
		<form action="/cgi-bin/conf/oscam"><div class='btn'><input type='submit' value='$(lang de:"Zur&uuml;ck" en:"Back")'></div></form>
</p>
EOF

cgi_end

