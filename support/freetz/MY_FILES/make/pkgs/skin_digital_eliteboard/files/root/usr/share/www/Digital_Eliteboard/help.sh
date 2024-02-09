Digital_Eliteboard_adds() {
		TARGET_CGI=$(echo $title|awk '{print$2}'|cut -d - -f1|cut -d "&" -f1|tr [A-Z [a-z])
		case $TARGET_CGI in
			start) _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?2042-Fritzbox-alle-Modelle' ;;
			external_tb) _CGI_HELP='' ;;
			filesystem) _CGI_HELP='' ;;
			configurations) _CGI_HELP='' ;;
			skin) _CGI_HELP='' ;;
			system) _CGI_HELP='' ;;
      design) _CGI_HELP='' ;; 
			oscam)  _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?886-CS-Oscam' ;;
			cccam) _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?402-CS-CCcam' ;;
			camd3) _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?405-CS-Camd3' ;;
			mbox)  _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?677-CS-M-Box' ;;
			gbox) _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?403-CS-Gbox' ;;
			scam) _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?744-CS-Scam' ;;
			newcs) _CGI_HELP='http://www.digital-eliteboard.com/forumdisplay.php?404-CS-Newcs' ;;
			minidlna) _CGI_HELP='http://freetz.org/wiki/packages/minidlna' ;;
      fhem) _CGI_HELP='http://fhemwiki.de/wiki/FHEM' ;;
      apache) _CGI_HELP='http://freetz.org/wiki/packages/apache' ;;
		esac
		[ "$(echo "$id"|grep 'tbflex:file')" ] && _CGI_HELP=''

}

