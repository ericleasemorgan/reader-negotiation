#!/usr/bin/env bash

INDEX='index.csv'
HOST='http://carrels.distantreader.org'

if [[ -z $1 ]]; then
	echo "Usage: $0 <word>" >&2
	exit
fi
WORD=$1

COUNT=$( curl $HOST/$INDEX 2>/dev/null | grep -i $WORD | wc -l | sed "s/[[:space:]]*//" )

echo -e "$WORD\t$COUNT"
exit
