#!/usr/bin/env bash

INDEX='index.csv'
HOST='http://carrels.distantreader.org'

if [[ -z $1 ]]; then
	echo "Usage: $0 <word>" >&2
	exit
fi
WORD=$1

curl $HOST/$INDEX 2>/dev/null | grep -i $WORD | csvcut -c 3,1,17 | sed "s/^/  * /" | sed "s/,/ \(/" | sed "s/,/\) - /"