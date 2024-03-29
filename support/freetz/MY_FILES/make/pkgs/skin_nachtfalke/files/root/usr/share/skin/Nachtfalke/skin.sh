
if [ "$TBFLEX_LANGUAGE_SET" = "english" ]; then helplink="help"; lang="en"; else helplink="Hilfe"; lang="de";fi
skin_head() {
	local title=$1 id=$2
	cat << EOF
<title>Freetz&nbsp;&ndash; $title</title>
<link rel="stylesheet" type="text/css" href="/style/Nachtfalke/base.css">
<link rel="stylesheet" type="text/css" href="/style/Nachtfalke/colorscheme.css">
EOF
	_cgi_print_extra_styles

	# The width of the whole cgi: There are 40px border (left+right)
	# and 225px for the menu area.
	let _cgi_total_width=_cgi_width+40+225

	# If there is no menu, we make the space available to the content.
	[ -z "$id" ] && let _cgi_width+=225
}

skin_body_begin() {
	local title=$1 id=$2
	local help=""
	[ -r /usr/share/www/Nachtfalke/help.sh ] && . /usr/share/www/Nachtfalke/help.sh && Nachtfalke_adds
	[ -n "$_CGI_HELP" ] && help="&nbsp;<span class='help'>(<a href='$(html "$_CGI_HELP")' target='_blank'>$helplink</a>)</span>"
	cat << EOF
<table id="edge" border="0" cellspacing="0" cellpadding="0" width="$_cgi_total_width">
<colgroup><col width="20"><col width="*"><col width="20"></colgroup>
<tr>
<td id="edge-top-left"></td>
<td id="edge-top">
<div class="version">$(html < /etc/.freetz-version)</div>
<div class="titlebar">
EOF
if [ "$(echo $title|grep -i -v 'TBflex')" ] && [ -n "$id" ]; then 
echo "<a href='/cgi-bin/index.cgi' class='logo'>Freetz</a>&nbsp;&ndash;</a>&nbsp;<span class='title'>$(echo $title)</span>$help</div>"
elif [ "$(echo $title|grep -i 'TBflex')" ]; then
echo "&nbsp;<span class='tb_title'><a href='/cgi-bin/extra/tbflex/overview'>$(echo $title|cut -d " " -f1)</a></span> $(echo $title|cut -d " " -f2)$help</div>"
else echo "&nbsp;<span class='tb_title'>$(echo $title)</span></div>"
fi
cat << EOF
</td>
<td id="edge-top-right"></td>
</tr>
<tr>
<td id="edge-left"></td>
<td id="container">
EOF
	set_menu() { _cgi_print_menu "$id"; }
	set_menu_tb() { 
	
	if [ -n "$(echo $id|grep '^file_tbmod')" ];then
		_conf_=$(echo $id|cut -d : -f3)
		_cgi_print_menu|sed "/Toolbox/s/^<li>/<li class='open'>/"|sed "/$_conf_/s/class='conf_file'/class='active conf_file'/"
	else _cgi_print_menu|sed "/Toolbox/s/^<li>/<li class='open'>/"
	fi 
	}
	[ "$TBFLEX_USE_TIMELINE" = "yes" -a "$(echo $id|egrep -i -v 'update|usbup|exec|install|de_installations')" -a -n "$id" ] && . /usr/share/timeline/timeline.sh && tb_timeline 2>/dev/null
	if [ -n "$id" ]; then
		if [ -n "$(echo $title|grep -i 'tbflex')" ];then
			if [ -n "$(echo $id|grep 'tbflex')" ]; then set_menu; else set_menu_tb;fi
		else set_menu;
	 	fi
	fi
echo "<div id='content' >"
}

skin_body_end() {
	cat << EOF
</div>
</td>
<td id="edge-right"></td>
</tr>
<tr>
<td id="edge-bottom-left"></td>
<td id="edge-bottom"></td>
<td id="edge-bottom-right"></td>
</tr>
</table>
<div id="footer">

<span class="datetime" title="Systemzeit des Routers">$(date +'%d.%m.%Y %H:%M')</span>&nbsp;&ndash;
<span class="uptime" title="Uptime">$(uptime | sed -r 's/.*(up.*), *load.*/\1/')</span>&nbsp;&ndash;
<span class="opt">optimiert f&uuml;r Mozilla Firefox</span>
</div>
EOF
}

skin_sec_begin() {
	# A fieldset adds a padding of 10px to the left and right, which is
	# space the content cannot utilize. By altering _cgi_width, we somehow
	# violate the rule "cgi application can use _cgi_width pixels just as
	# requested in 'cgi --width=1234'", but sec_begin is optional! If the
	# app really needs 1234px, then it should not use sec_begin() or it
	# will live with the fact that we take away some pixels.
	cgi_width_alter -20
	cat << EOF
<fieldset>
<legend>$1</legend>
EOF
}

skin_sec_end() {
	cgi_width_alter 20
	cat << EOF
</fieldset>
EOF
}

