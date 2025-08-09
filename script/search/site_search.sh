#!/bin/bash
export LANG=ko_KR.UTF-8


if [[ ! -e debug ]]; then
	mkdir debug
else
	rm ./debug/*
fi

is_new_window=$1
browser=$2
site=$3
query=$4
urls_json_file=$5


echo -n "is_new_windows: $1
browser: $2
site: $3
query: $4
urls_json_file: $5" > ./debug/0_input_arguments.txt


# jq 설치
jq --version > /dev/null 2>$1
if [[ $? == "127" ]]; then
	echo "jq: command not found"
	if [[ $(uname)  == "Darwin" ]]; then
		brew install jq
	else
		echo "jq 라이브러리를 설치해주세요"
		exit
	fi
fi


# URL 가져오기
if [[ $query == "" ]]; then
	url=`cat $urls_json_file | jq ".$site.base_url"`
else
	url=`cat $urls_json_file | jq ".$site.query_url"`
fi
echo "url: $url"
url=${url%\"} # url의 맨 뒤에 있는 " 자르기
url=${url#\"} # url의 맨 앞에 있는 " 자르기


# 입력 받은 query를 percent-encoding 변환
code_points=$(bash ./utils/code_point_parser.sh "$query")
echo "code_points: ${code_points}"
query=$(python3 ./utils/percent_encoding_parser.py ${code_points[@]})
echo "query: ${query}"
echo "$query" > ./debug/5_parsed_query.txt


# url에 있는 {query}를 qurl
url=$(echo $url | sed "s/{search_query}/${query}/g")
echo $url > ./debug/6_url.txt


# open 실행 옵션 설정
url=$(echo $url | sed "s/\$query/$encoded_query/g")
if [[ $is_new_window == "0" ]]; then
	open_option="-a"
else
	open_option="-na"
	window_option="--args --new-window"
fi


# Browswer 열기
echo "open $open_option $browser $window_option $url" > ./debug/z_execute_command.txt
open "$open_option" "$browser" $window_option "$url" # window_option은 double quote로 묶으면 안됨

# open을 하면 0파일 혹은 1파일이 생김
# 

if [[ -e 0 ]]; then
	rm ./0
fi

if [[ -e 1 ]]; then
	rm ./1
fi
