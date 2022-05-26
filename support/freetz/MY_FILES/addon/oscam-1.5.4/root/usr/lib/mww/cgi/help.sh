_cgi_help_url() {
local path=$1

    if [ "$(echo "${path%#*}" | grep -o "oscam")" == "oscam" ]; then
	if [ "$MOD_SKIN" = "Keywelt" ]; then
	   echo "http://www.keywelt-board.com/index.php?/forum/74-freetz/"
	elif [ "$MOD_SKIN" = "Nachtfalke" ] || [ "$MOD_SKIN" = "Nachtfalke_old" ]; then
	   echo "http://www.nachtfalke.biz/forumdisplay.php/171-Nachtfalke-Reloaded-Freetzprojekt"
	else
	   echo "http://www.digital-eliteboard.com/forums/fritzbox-talk.2045/"
	fi
    else
	   echo "http://freetz.org/wiki${path}"
    fi
}  
