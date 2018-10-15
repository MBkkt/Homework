#!/bin/bash
# ./script2.sh [-d] replace [mask]

while [[ -n $1 ]]; do
  case $1 in
    --) shift ;;
    -d) key="d"; shift;;
    *) break;;
  esac
done

sfx=$1
shift

for x; do
  if [[ -f $x ]]; then
    a=${x%.*}
    b=${x#${a}}
    y=${a}${sfx}${b}
    echo "$x -> $y"
    if [[ -z $key ]]; then mv "$x" "$y"; fi
  fi
done
