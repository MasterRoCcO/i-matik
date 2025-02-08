#!/bin/sh


PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh

cgi --id=i-matik

cgi_begin "Gebaut mit I-matik"
cat << EOF | sed -r 's/(.+[^>])$/\1<br>/g'
<center>

<p>
<h1>Get help here</h1>
	<a class="active" href="https://github.com/MasterRoCcO/i-matik" target="_blank">GitHub Side</a>
<br/>
	<a class="active" href="https://www.digital-eliteboard.com/threads/mein-script-i-matik-was-eine-image-automatik-ist-plus-oscam-bau.507178/" target="_blank">Digital Eliteboard Side</a>
<br/>
	<a class="active" href="https://www.ip-phone-forum.de/threads/vorstellung-meines-scripts-namens-i-matik.312640/" target="_blank">IP Phone Forum Side</a>
<br/>
<br/>
The installed version on this device is currently xxxx
<br/>
<h1>Donate Page for i-matik</h1>
<br/>
	<a class="active" href="https://www.spendenseite.de/i-matik/-67603" target="_blank">Spenden Side</a>
<br/>
<br/>
<h1>Donate Page for freetz-ng</h1>
	<a class="active" href="https://github.com/sponsors/fda77" target="_blank"> <img src="https://img.shields.io/static/v1?label=GitHub&message=fda77&logo=GitHub&color=%230e8e86" alt="GitHub Side"></a>
<br/>
	or
	<a class="active" href="https://camo.githubusercontent.com/1bbcdb4d5113e485a0fee48c81e68b3e1900189377a5d75b7beea9922a09a51e/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d426974636f696e266d6573736167653d6664613737266c6f676f3d426974636f696e26636f6c6f723d253233306538653836" target="_blank">
    <img src="https://img.shields.io/static/v1?label=Bitcoin&message=fda77&logo=Bitcoin&color=%230e8e86" alt="Bitcoin Side"></a>	
<br/>
<br/>
<h1>Big thanks to</h1>
bbszx (Tested on 4060 and 7530AX)
berndy2001
hermann72pb
Humpty Dumpty
Hookdr
Loman
MC Crap FIX (Tested on Fiber 5590 and 5690Pro)
nero033
prisrak (Tested on Cabel 6660 and 6690)
sestarus
TickTack (Tested on 4050 and 7690)
</p>

</center>
EOF
cgi_end
