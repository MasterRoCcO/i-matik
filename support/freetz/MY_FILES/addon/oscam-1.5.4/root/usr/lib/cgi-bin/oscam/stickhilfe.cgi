#!/bin/sh

PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg

cgi --id=conf:oscam:_index
cgi_begin '$(lang de:"Hilfe USB-Modus" en:"USB mode help")'

cat << EOF
<h1>$(lang de:"Hilfe USB-Modus" en:"USB mode help")</h1>

<p>
	$(lang de:"Es befindet sich kein USB-Speicher an der Fritz!Box" en:"No USB memory connected to the Fritz!Box")<br>
	$(lang de:"Um OSCam zu nutzen, USB-Speicher anstecken und Fritzbox neu starten." en:"To use OSCam, connect USB memory and restart the box.")
</p>

<ul>
	<li><a class="active" href="/cgi-bin/system.cgi">$(lang de:"Fritz!Box neustarten" en:"Restart Fritz!Box")</a></li>
</ul>

<p>
	<form action="/cgi-bin/conf/oscam"><div class='btn'><input type='submit' value='$(lang de:"Zur&uuml;ck" en:"Back")'></div></form>
</p>
EOF

cgi_end

