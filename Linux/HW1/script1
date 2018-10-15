#!/bin/bash
sfx=$1
shift
while [[ -n $1 ]]; do
  case $1 in
    --) shift ;;
    -d) key="d"; shift;;
    *) break;;
  esac
done

for x in "$@"; do
  if [[ -f $x ]]; then
    a=${x%.*}
    b=${x#${a}}
    y=${a}${sfx}${b}
    echo "$x -> $y"
    if [[ -z $key ]]; then
      mv "$x" "$y"
    fi
  else
    echo "$x no file"
  fi
done
