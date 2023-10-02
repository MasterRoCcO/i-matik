#!/bin/sh


PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh

cgi --id=i-matik

cgi_begin "$(lang de:"Gebaut mit" en:"Built with") I-matik"
cat << EOF | sed -r 's/(.+[^>])$/\1<br>/g'
<center>

<p>
<h1>Get help here</h1>
 <ul>
        <li><a class="active" href="https://github.com/MasterRoCcO/i-matik" target="_blank">https://github.com/MasterRoCcO/i-matik</a></li>
    </ul>
 <ul>
        <li><a class="active" href="https://www.digital-eliteboard.com/threads/mein-script-i-matik-was-eine-image-automatik-ist-plus-oscam-bau.507178/" target="_blank">https://www.digital-eliteboard.com/threads/mein-script-i-matik-was-eine-image-automatik-ist-plus-oscam-bau.507178/</a></li>
    </ul>
 <ul>
        <li><a class="active" href="https://www.ip-phone-forum.de/threads/vorstellung-meines-scripts-namens-i-matik.312640/" target="_blank">https://www.ip-phone-forum.de/threads/vorstellung-meines-scripts-namens-i-matik.312640/</a></li>
    </ul>
The installed version on this device is currently xxxx
<br/>

<h1>Big thanks to</h1>
bbszx
berndy2001
hermann72pb
Loman
MC Crap FIX
nero033

<h1>TESTER by Cable devices</h1>
prisrak
</p>

</center>
EOF
cgi_end
