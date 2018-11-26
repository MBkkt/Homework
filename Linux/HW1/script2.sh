#!/bin/bash
# ./script2.sh [-d] replace ['mask'] [directory]

while [[ -n $1 ]]; do
  case $1 in
    --) shift ;;
    -d) key="d"; shift;;
    *) break;;
  esac
done

if [[ -z $1 ]]; then
  echo "Missing required arguments"
  exit
fi

sfx=$1
shift

argv="$@"

t=${!#}
if [[ ! -d $t ]]; then t=`pwd`; fi
cd $t

for x in $argv; do
  if [[ -f $x ]]; then
    a=${x%.*}
    b=${x#${a}}
    y=${a}${sfx}${b}
    echo "$x -> $y"
    if [[ -z $key ]]; then mv "$x" "$y"; fi
  fi
done
