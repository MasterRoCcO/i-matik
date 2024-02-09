Nachtfalke_old_adds() {
		TARGET_CGI=$(echo $title|awk '{print$2}'|cut -d - -f1|cut -d "&" -f1|tr [A-Z [a-z])
		case $TARGET_CGI in
			start) _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=1802' ;;
			external_tb) _CGI_HELP='' ;;
			programme|programs) _CGI_HELP='' ;;
			configurations) _CGI_HELP='' ;;
			system) _CGI_HELP='' ;;
			design) _CGI_HELP='' ;;			
			oscam)  _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=1366' ;;
			cccam) _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=606' ;;
			camd3) _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=608' ;;
			mbox)  _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=609' ;;
			sbox) _CGI_HELP='' ;;
			gbox) _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=607' ;;
			scam) _CGI_HELP='' ;;
			newcs) _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=614' ;;
			mgcamd) _CGI_HELP='http://www.sat-ulc.eu/forumdisplay.php?f=613' ;;
			hypercam) _CGI_HELP='' ;;
			vizcam) _CGI_HELP='' ;;
			minidlna) _CGI_HELP='http://freetz.org/wiki/packages/minidlna' ;;
			fhem) _CGI_HELP='http://fhemwiki.de/wiki/FHEM' ;;
			apache) _CGI_HELP='http://freetz.org/wiki/packages/apache' ;;
			nfs) _CGI_HELP='http://freetz.org/wiki/packages/nfs-utils' ;;
			hdd) _CGI_HELP='http://freetz.org/wiki/packages/smartmontools' ;;
		esac
		[ "$(echo "$id"|grep 'tbflex:file')" ] && _CGI_HELP=''

}
