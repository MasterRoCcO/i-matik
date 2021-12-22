#!/bin/sh


PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh

cgi --id=i-matik

cgi_begin "$(lang de:"Gebaut mit" en:"Built with") I-matik"
cat << EOF | sed -r 's/(.+[^>])$/\1<br>/g'
<center>

<p>
<h1>Supporters</h1>
https://github.com/MasterRoCcO/i-matik

https://www.digital-eliteboard.com/threads/mein-script-i-matik-was-eine-image-automatik-ist-plus-oscam-bau.507178/
</p>

</center>
EOF
cgi_end
