#!/bin/bash

# usage: ./script2_2.sh NameValute [date(dd/mm/yyyy)]

if [[ -z $1 ]]; then
	echo "Don't correct agrs"
    exit
fi

valute=$1
url="http://www.cbr.ru/scripts/XML_daily.asp?date_req="$2

tempfile=`mktemp`
wget -qO $tempfile $url
temp="`cat $tempfile`"

temp=${temp##*$valute}
if [[ "${temp:2:3}" == 'xml' ]]; then
    echo "Name valute isn't correct"
else
	temp=${temp%%</Value>*}
	temp=${temp##*<Value>}
	echo $temp
fi
