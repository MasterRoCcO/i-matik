Keywelt_adds() {
		TARGET_CGI=$(echo $title|awk '{print$2}'|cut -d - -f1|cut -d "&" -f1|tr [A-Z [a-z])
		case $TARGET_CGI in
			start) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/74-freetz/' ;;
			external_tb) _CGI_HELP='' ;;
			filesystem) _CGI_HELP='' ;;
			configurations) _CGI_HELP='' ;;
			system) _CGI_HELP='' ;;
      design) _CGI_HELP='' ;; 
			skin) _CGI_HELP='' ;;
			oscam)  _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/85-oscam-mpcs/' ;;
			cccam) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/77-cccam/' ;;
			camd3) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/78-camd3/' ;;
			mgcamd) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/79-mgcamd/' ;;
			gbox) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/80-gbox/' ;;
			scam) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/81-scam/' ;;
			newcs) _CGI_HELP='http://www.keywelt-board.com/index.php?/forum/82-newcamd/' ;;
			minidlna) _CGI_HELP='http://freetz.org/wiki/packages/minidlna' ;;
      fhem) _CGI_HELP='http://fhemwiki.de/wiki/FHEM' ;;
      apache) _CGI_HELP='http://freetz.org/wiki/packages/apache' ;;
		esac
		[ "$(echo "$id"|grep 'tbflex:file')" ] && _CGI_HELP=''

}

