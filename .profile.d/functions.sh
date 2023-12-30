#functions
#rename files replacing spaces
rmspace() {
     find . -depth -name '* *' \
| while IFS= read -r f ; do mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)" ; done
}

#change volume
vol() {
   doas  mixerctl outputs.master=$1 > /dev/null
}

#search privately
ddg() {
    lynx https://duckduckgo.com/lite/search?q="$1"
    }

yad() {
    cadaver https://webdav.yandex.ru
    }

m2t() {
    man $* | col -b > $*.txt
    }

#extract - extract most common compression types
extract () {
     if [ -f $1 ] ; then
              case $1 in
                   *.tar.bz2)   tar xjf $1        ;;
	           *.tar.gz)    tar xzf $1     ;;
                   *.bz2)       bunzip2 $1       ;;
                   *.rar)       7z x $1     ;;
                   *.gz)        gunzip $1     ;;
                   *.tar)       tar xf $1        ;;
                   *.tbz2)      tar xjf $1      ;;
                   *.tgz)       tar xzf $1       ;;
                   *.zip)       unzip $1     ;;
                   *.Z)         uncompress $1  ;;
                   *.7z)        7z x $1    ;;
                   *)           echo "'$1' cannot be extracted via extract()" ;;
              esac
      else
         echo "'$1' is not a valid file"
     fi
}


#backup made easy
bu ()
{
    if [ "`dirname $1`" == "." ]; then
            mkdir -p ~/.backup/`pwd`;
	    cp -r $1 ~/.backup/`pwd`/$1-`date +%Y%m%d%H%M`.backup
    else
            mkdir -p ~/.backup/`dirname $1`;
            cp -r $1 ~/.backup/$1-`date +%Y%m%d%H%M`.backup;
    fi
}


yaput() {
W_DIR="PRIVATE"
[ $# != 1  ] && echo "usage: yad [file]" && exit 1
send=${1}
cadaver <<EOF
open https://webdav.yandex.ru
cd $W_DIR
put $send
EOF
}
