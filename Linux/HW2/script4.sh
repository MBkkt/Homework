#!/bin/bash

# usage: ./script4.sh "bank" sum valute

if (( $# != 3 )); then
    echo "Don't correct input"
    exit
fi

sum=$2
valute=$3

regexp1='<a target=""  href="/insurance/insurance_cases/[0-9]\+/">.*'$1'.*</a>'
regexp2='.*[0-9]\{2\}[.][0-9]\{2\}[.][0-9]\{4\}.*'

temp=$(curl 'https://www.asv.org.ru/insurance/insurance_cases/' \
       | iconv -f CP1251 -t UTF-8 \
       | grep -o "$regexp1" \
       | grep -o "[0-9]*")
       
temp=$(curl 'https://www.asv.org.ru/insurance/insurance_cases/'$temp'/' \
       | iconv -f CP1251 -t UTF-8 \
       | grep -o "$regexp2")

for x in $temp; do
    x=${x##*>}
    x=${x%:}
    x=${x//'.'/'/'}
    if [[ $x =~ ^[0-9]+/[0-9]+/[0-9]+$  ]]; then
        datee=$x
    fi
done
if [[ -z $datee ]]; then
    echo "Don't correct data"
    exit
fi
x=`./script1.sh $valute $datee`
let "x=$x*$sum"
echo $x
