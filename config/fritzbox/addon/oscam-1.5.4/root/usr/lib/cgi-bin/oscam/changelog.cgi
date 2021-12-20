#!/bin/sh

PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh
. /mod/etc/conf/oscam.cfg


#cgi --id=cgi --id=extra:oscam:oscamup
cgi_begin '$(lang de:"Changelog vom DEB/NFR Freetz-Team OSCam Addon" en:"Changelog from DEB/NFR Freetz-Team OSCam Addon")'

echo '
<h1>$(lang de:"oscam-1.5.4" en:"oscam-1.5.4")</h1>
<p>$(lang de:"Anpassung wegen openssl" en:"adjustment due to openssl ")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.5.3" en:"oscam-1.5.3")</h1>
<p>$(lang de:"Es wird geprüft welche OSCamversion benötigt wird und passend zum Teamserver verlinkt" en:"It is checked which OSCam version is required and linked to the Teamserver")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.5.2" en:"oscam-1.5.2")</h1>
<p>$(lang de:"Bug behoben, Freetzsicherung kann wieder eingespielt werden" en:"Bug fixed, release fuse can be imported again")</p>
<p>$(lang de:"Bug behoben, crontab von oscamwatchdog werden wieder richtig eingetragen und gelöscht" en:"Bug fixed, crontab of oscamwatchdog are correctly entered and deleted")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.5.1" en:"oscam-1.5.1")</h1>
<p>$(lang de:"Bug behoben, OSCam-Tools/OSCam-Watchdog Einstellungen werden wieder gespeichert" en:"Bug fixed, OSCam-Tools / OSCam-Watchdog settings are saved again")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.5.0" en:"oscam-1.5.0")</h1>
<p>$(lang de:"Bug behoben, Anzeige Intern-Modus gefixt" en:"Bug fixed, display fixed internal mode")</p>
<hr />'

echo '
    <p>
        <input type="checkbox" name="expertchk" value="no" onclick='\''document.getElementById("expertchk_show").style.display=(this.checked)? "" : "none"'\''> 
        $(lang de:"Weitere" en:"More")
    </p>'

echo '<div id="expertchk_show" style="display:none;margin-left:0px;" name="expert2chk_show">'

echo '
<h1>$(lang de:"oscam-1.4.9" en:"oscam-1.4.9")</h1>
<p>$(lang de:"Addon angepasst, damit auf den 64xx-65xx Boxen der Intern-Modus genutzt werden kann" en:"Addon adapted so that the 64xx-65xx boxes of the internal mode can be used")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.8" en:"oscam-1.4.8")</h1>
<p>$(lang de:"Addon angepasst. Link zum neuen Teamserver eingebaut" en:"Addon customized. Link to the new team server installed")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.7" en:"oscam-1.4.7")</h1>
<p>$(lang de:"Addon angepasst, OSCam-Setup und OSCam-Tools jetzt einzeln aufrufbar" en:"Addon customized, OSCam setup and OSCam tools are now individually retrievable")</p>
<p>$(lang de:"Link Anleitung Intern-Modus-USB-Modus OScam mit oscam-1.4x mit eingebaut" en:"Link Instructions Internal mode USB OScam with oscam-1.4x with built-in")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.6" en:"oscam-1.4.6")</h1>
<p>$(lang de:"Addon angepasst, damit auf den neuen Boxen der Intern-Modus genutzt werden kann" en:"Addon adapted so that the new boxes of the internal mode can be used")</p>
<p>$(lang de:"Bug behoben, Speicherbereinigung geht wieder" en:"Bug fixed, memory recovery goes again")</p>
<p>$(lang de:"Optimierung vorgenommen. Es werden nur noch die wichtigen OSCamdateien bei Erstinstallation mit hochgeladen" en:"Optimization. Only the important OSCam files are uploaded at the initial installation")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.5" en:"oscam-1.4.5")</h1>
<p>$(lang de:"Serialanzeige. Die Serial von den angeschlossenen Cardreader wird angezeigt" en:"Serial display. The serial from the connected cardreader is displayed")</p>
<p>$(lang de:"Udev-Regel. Cardreader fest verlinken mit eigenem Namen. Wird nur angezeigt, wenn udev im Image verbaut ist" en:"Udev rule. Cardreader permanently linked with its own name. Is only displayed if udev is installed in the image")</p>
<p>$(lang de:"Versionsnummer vom PCSCD-Treiber wird angezeigt" en:"Version number of the PCSCD driver is displayed")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.4" en:"oscam-1.4.4")</h1>
<p>$(lang de:"Fusebyte-Abfrage jetzt auch über einen Receiver (Enigma2) am TV anzeigbar" en:"Fusebyte query now also be displayed on a receiver( Enigma2) on TV")</p>
<p>$(lang de:"Bugfix behoben.(Einträge in der crontab und rc_custom wurden gelöscht)" en:"Bugfix Fixed.(Entries in the crontab and rc_custom deleted)")</p>
<p>$(lang de:"Changelog eingebaut" en:"installed Changelog")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.3" en:"oscam-1.4.3")</h1>
<p>$(lang de:"Bugfix behoben (Fehler beim Wiedeherstellen einer zuvor gespeicherten OSCam-Konfiguration behoben)" en:"Bugfix Fixed. (Entries in the crontab and rc_custome deleted)")</p>
<p>$(lang de:"Fusebyte-Abfrage, SoftCam.Key, ListSmargo, OScam-Binary Install/Update/Restore: Optimierung mit Ausgabe der Zwischenschritte. " en:"Fusebyte query SoftCam.Key, List Smargo, OScam binary Install / Update / Restore: optimization with output of intermediate steps.")</p>
<p>$(lang de:"Online-Hilfe angepasst: für das OSCam Addon wird jetzt in die entsprechenden Foren (je nach Mod: NFR, DEB oder Keywelt) verwiesen. Für die Standard-Freetz-Packages wird nach Freetz.org verlinkt." en:"Online help adapted: for OSCam addon is now in the appropriate forums (depending Mod: NFR, DEB or Keywelt) referenced. For the standard Freetz package is linked to Freetz.org.")</p>
<p>$(lang de:"Auch im Intern-Modus wird jetzt der Speicherort der OSCam-Konfiguration angezeigt." en:"Also in the Internet mode the location of OSCam configuration is displayed now.")</p>
<p>$(lang de:"Alle OSCam EMM-Logs können jetzt als Archiv auf dem PC gespeichert werden." en:"All OSCam EMM logs can now be saved as an archive on the PC.")</p>
<p>$(lang de:"Watchdog integration: Das Watchdog-Addon, zur Überwaching des OSCam-Betriebs haben wir in unser Addon integriert." en:"Watchdog integration: The watchdog addon to monitor the OSCam-operation we have integrated into our Addon.")</p>
<p>$(lang de:"Eigenen DNS Updater mit eingebaut." en:"Own DNS Updater installed.")</p>
<p>$(lang de:"Zusätzlich haben wir Funktionen zum Testen der E-Mail Einstellungen, sowie DynDNS- und benutzerdefinierten Fehler Check eingebaut." en:"In addition, we have added functions to test the e-mail settings, as well as DynDNS and custom error check.")</p>
<hr />'


echo '
<h1>$(lang de:"oscam-1.4.2" en:"oscam-1.4.2")</h1>
<p>$(lang de:"Bei OSCam Cardserver Info werden jetzt alle 4 EMMs-Logs angezeigt." en:"In OSCam CardServer info now all 4 EMMs logs are displayed.")</p>
<p>$(lang de:"Unter Treiberstatus wird angezeigt,welcher Treiber geladen ist." en:"Under Driver Status shows which driver is loaded.")</p>
<p>$(lang de:"Die Fusebyte-Payload-Abfrage wurde optimiert. Es wird die oscam.server durchsucht nach aktiven reader,caid von V13 und V14 und dem label. Wenn die passende Karte gefunden wird,wird sie als label angezeigt um die Abfrage kann gestartet." en:"The Fusebyte Payload query has been optimized. It is the oscam.server searched for active reader, caid of V13 and V14 and the label. If the matching card is found, it is a label displayed to the query can be started.")</p>
<p>$(lang de:"Zusatz-Optionen müssen jetzt aktiviert werden" en:"Additional options must be activated now")</p>
<p>$(lang de:"gepackte oscam,list_smargo und SoftCam.Key in tar.gz,rar und zip werden nicht installiert." en:"acked oscam, list_smargo and SoftCam.Key in tar.gz, rar and zip are not installed.")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.1" en:"oscam-1.4.1")</h1>
<p>$(lang de:"Fusebyte-Payload-Abfrage für NDS-Karten (V13 und V14) eingebaut." en:"built Fusebyte Payload query for NDS card (V13 and V14).")</p>
<p>$(lang de:"OSCam-Setup-Seite - Alle Funktionen zur Installation, Aktualisierung und Einrichtung von OSCam." en:"OSCam Setup page - All functions for installing, upgrading and establishment of OSCam.")</p>
<p>$(lang de:"Speicher bereinigen (u.a. Binaries, Backups und Logdateien löschen) für Boxen mit knappem internem Speicher." en:"Memory clean up (inter alia binaries, backups and log delete files) for boxes with tight internal memory.")</p>
<p>$(lang de:"OSCam-Konfiguration als Archiv sichern bzw. eine zuvor gesicherte Konfiguration wiederherstellen." en:"Save OSCam configuration as an archive or restore a previously saved configuration.")</p>
<p>$(lang de:"Optional können bei der Wiederherstellung die Pfade für Logile und Stylesheet automatisch an die aktuelle Umgebung angepasst werden, so dass keine manuelle Anpassung z.B. nach einem HW-Wechsel mehr nötig ist." en:"Optionally, the paths for Logile and stylesheet automatically adapt to the current environment in the restoration, so that no manual adjustment as after a hardware change is necessary.")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.4.0" en:"oscam-1.4.0")</h1>
<p>$(lang de:"oscam-1.3.2 und oscm-1.3.2ISP umgebaut zu einem addon" en:"oscam-1.3.2 and 1.3.2 oscam-ISP converted into a addon")</p>
<p>$(lang de:"Das Addon unterstützt nun auch Englisch als GUI-Sprache, wenn die entsprechende Einstellung beim Bau des Freetz-Images gemacht wird." en:"The addon now supports English as GUI language when the appropriate setting is made in the construction of Freetz Images.")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.3.2/oscam-1.3.2ISP" en:"oscam-1.3.2/oscam-1.3.2ISP")</h1>
<p>$(lang de:"OSCam Info-Seite" en:"OSCam Information page")</p>
<p>$(lang de:"SoftCam.Key-Erstinstallation oder Aktualisierung. " en:"SoftCam.Key initial installation or upgrade.")</p>
<p>$(lang de:"Bugfix behoben. (UStor01-Problem behoben, jetzt ist es egal wie der Stick gemountet wird)" en:"Bugfix Fixed. (uStor01 problem solved, now as the stick does not care is mounted)")</p>
<hr />'

echo '
<h1>$(lang de:"oscam-1.3.1/oscam-1.3.1ISP" en:"oscam-1.3.1/oscam-1.3.1ISP")</h1>
<p>$(lang de:"Auswahlmöglichkeit Intern-Modus oder USB-Modus" en:"Choice Intern mode or USB mode")</p>
<p>$(lang de:"Online-Update der OSCam" en:"Online update of OSCam")</p>
<p>$(lang de:"Aktuelle Hilfelinks zu ausgewählten Themen" en:"current Help Links on Selected Topics")</p>'


echo '</div><form action="'/cgi-bin/conf/oscam'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'

#echo '</div><form action="'$(href conf oscam)'"><div class="btn"><input type="submit" value="$(lang de:"Zur&uuml;ck" en:"Back")"></div></form>'

cgi_end