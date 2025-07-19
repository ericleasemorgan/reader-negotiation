#!/usr/bin/env bash

INDEX='index.json'
HOST='http://carrels.distantreader.org'

if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi
CARREL=$1

curl $HOST/$INDEX 2>/dev/null | jq --arg CARREL $CARREL -c '.[]|select(.id|contains($CARREL))'
