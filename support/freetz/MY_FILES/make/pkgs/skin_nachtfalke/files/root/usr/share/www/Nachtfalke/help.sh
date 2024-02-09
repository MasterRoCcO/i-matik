nachtfalke_adds() {
		TARGET_CGI=$(echo $title|awk '{print$2}'|cut -d - -f1|cut -d "&" -f1|tr [A-Z [a-z])
		case $TARGET_CGI in
			start) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/171-Nachtfalke-Reloaded-Freetzprojekt' ;;
			external_tb) _CGI_HELP='' ;;
			programme|programs) _CGI_HELP='' ;;
			configurations) _CGI_HELP='' ;;
			system) _CGI_HELP='' ;;
			design) _CGI_HELP='' ;;			
			oscam)  _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/287-oscam' ;;
			cccam) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/288-cccam' ;;
			camd3) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			mbox)  _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			sbox) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			gbox) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			scam) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			newcs) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			mgcamd) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			hypercam) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			vizcam) _CGI_HELP='http://www.nachtfalke.biz/forumdisplay.php/291-Andere-cams' ;;
			minidlna) _CGI_HELP='http://freetz.org/wiki/packages/minidlna' ;;
			fhem) _CGI_HELP='http://fhemwiki.de/wiki/FHEM' ;;
			apache) _CGI_HELP='http://freetz.org/wiki/packages/apache' ;;
			nfs) _CGI_HELP='http://freetz.org/wiki/packages/nfs-utils' ;;
			hdd) _CGI_HELP='http://freetz.org/wiki/packages/smartmontools' ;;
		esac
		[ "$(echo "$id"|grep 'tbflex:file')" ] && _CGI_HELP=''

}
