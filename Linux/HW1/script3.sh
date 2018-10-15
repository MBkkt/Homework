#!/bin/bash
# ./script.sh [user] [file]

f='/etc/passwd'
user=$USER

while [[ -n $1 ]]; do
    case $1 in
        -f) f=$2; shift 2;;
        -*) shift;;
        *) user=$1; break;;
    esac
done

echo $(grep "^$user:" < $f | cut -d ':' -f 6)
