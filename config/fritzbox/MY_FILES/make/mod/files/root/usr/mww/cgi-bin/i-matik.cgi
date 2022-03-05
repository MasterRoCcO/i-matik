#!/bin/sh


PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh

cgi --id=i-matik

cgi_begin "$(lang de:"Gebaut mit" en:"Built with") I-matik"
cat << EOF | sed -r 's/(.+[^>])$/\1<br>/g'
<center>

<p>
<h1>Supporters</h1>
 <ul>
        <li><a class="active" href="https://github.com/MasterRoCcO/i-matik" target="_blank">https://github.com/MasterRoCcO/i-matik</a></li>
    </ul>
 <ul>
        <li><a class="active" href="https://www.ip-phone-forum.de/threads/vorstellung-meines-scripts-namens-i-matik.312640//" target="_blank">https://www.ip-phone-forum.de/threads/vorstellung-meines-scripts-namens-i-matik.312640/</a></li>
    </ul>
</p>

</center>
EOF
cgi_end
