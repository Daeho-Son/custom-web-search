#!/bin/bash

if [[ ! -e debug ]]; then
	mkdir debug
else
	rm ./debug/*
fi

is_new_window=$1
browser=$2
site=$3
query=$4
urls_json=$5

echo "is_new_window: $1
browswer: $2
site: $3
query: $4
urls_json: $5
" > ./debug/0_input_arguments.txt

jq --version > /dev/null 2>$1
if [[ "$?" == "127" ]]; then
	echo "jq: command not found"
	if [[ "$OS"  == "Darwin" ]]; then
		brew install jq
	else
		echo "Exit: jq 라이브러리를 설치해주세요"
		exit
	fi
fi

open_option="-na"
window_option="--args"
if [[ $is_new_window == "1" ]]; then
	window_option="$window_option --new-window"
fi

if [[ "$query" =~ (https:\/\/|http:\/\/)?([a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})? ]]; then
	echo "[DEBUG] URI를 매개변수로 입력"
	url="$query"
else
	echo "[DEBUG] 검색어를 매개변수로 입력"
	url=`cat $urls_json | jq ".$site.query"`
	url=${url%\"}
	url=${url#\"}
	url=$(echo -n $url | sed "s/{query}/$query/g")
fi

rm -f 0
rm -f 1

echo $open_option "$browser" $window_option "$url" > ./debug/z_execute_command.txt
open "$open_option" "$browser" $window_option "$url"
