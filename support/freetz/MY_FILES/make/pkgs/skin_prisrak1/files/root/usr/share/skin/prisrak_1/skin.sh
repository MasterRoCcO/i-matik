skin_head() {
	local title=$1 id=$2
	local hname="$(hostname -s|html)"
	[ "$hname" != "fritz" ] && hname="&#64;${hname}&nbsp;" || hname=""
	cat << EOF
<title>Freetz&nbsp;${hname}&ndash; $title</title>
<link rel="stylesheet" type="text/css" href="/style/prisrak_1/base.css">
<link rel="stylesheet" type="text/css" href="/style/prisrak_1/colorscheme.css">
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
	if [ -n "$_CGI_HELP" ]; then
		help="&nbsp;<span class='help'>(<a href='$(html "$_CGI_HELP")' target='_blank'>Hilfe</a>)</span>"
	fi
	local hname="$(hostname -s|html)"
	[ "$hname" != "fritz" ] && hname="&#64;<a href="/cgi-bin/avm" target="_blank">${hname}</a>&nbsp;" || hname=""
	cat << EOF
<table id="edge" border="0" cellspacing="0" cellpadding="0" width="$_cgi_total_width">
<colgroup><col width="20"><col width="*"><col width="20"></colgroup>
<tr>
<td id="edge-top-left"></td>
<td id="edge-top">
<div class="version">$(html < /etc/.freetz-version)</div>
<div class="titlebar"><a href="https://freetz-ng.github.io" target="_blank" class="logo">Freetz</a>&nbsp;${hname}<a href="/cgi-bin/about.cgi" target="_blank">&ndash;</a>&nbsp;<span class="title">$title</span>$help &nbsp; &nbsp; $([ "$isauth" = 1 ] && echo "<small>Session timeout: $(date -d @$(( $MOD_HTTPD_SESSIONTIMEOUT + $(date +%s) )) +'%H:%M:%S')</small>") </div>
</td>
<td id="edge-top-right"></td>
</tr>
<tr>
<td id="edge-left"></td>
<td id="container">
EOF
	[ -n "$id" ] && _cgi_print_menu "$id"
	echo "<div id='content'>"
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
