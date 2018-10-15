#!/bin/bash
# ./script4.sh size [dir]

s=$1
d=$2
if [[ -z $d ]]; then d=`pwd`; fi
args="${d}/*"

for x in $args; do
  if [[ -f $x && $s -lt `stat -c '%s' "$x"` ]]; then
    temp=${x%/*}"/"
    echo ${x#$temp}
  fi
done
