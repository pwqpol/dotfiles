export TERM=xterm-256color
export HISTFILE=~/.history

. ~/.profile.d/aliases.sh
. ~/.profile.d/functions.sh

LYNX_CFG=~/.lynx.cfg; export LYNX_CFG  
#PS1='[\u@\h \W]\$ '  # To leave the default one
#DO NOT USE RAW ESCAPES, USE TPUT
reset=$(tput sgr0)
red=$(tput setaf 1)
blue=$(tput setaf 4)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
PS1='\[$green\]\h\[$reset\]@ \[$yellow\]\w\[$reset\] \[$red\]\$ \[$reset\]'


#autostart apps
if [ -z `pgrep -n emacs` ]
    then emacs --daemon
fi

trap '. ~/.profile.d/ksh_logout' exit 0

clear
date "+DATE: %d-%m-%Y%nTIME: %H:%M"
METRIC=1 #Should be 0 or 1; 0 for F, 1 for C
curl -s http://rss.accuweather.com/rss/liveweather_rss.asp\?metric\=${METRIC}\&locCode\="EN|UA|Simferopol" | perl -ne 'if (/Currently/) {chomp;/\<title\>Currently: (.*)?\<\/title\>/; print "$1"; }' && echo









