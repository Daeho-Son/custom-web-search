is_new_window=$1
browser=$2
site=$3
query=$4
urls_json=$5

echo "is_new_window: $1"
echo "browswer: $2"
echo "site: $3"
echo "query: $4"
echo "urls_json: $5"

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

# Error
# - $browser 로 사용하면 작동X -> "$browser"
# - $browser 를 다른 변수에 넣어서 사용하면 작동x -> 직접 사용

window_option=""
open_option="-a"
if [[ $is_new_window == "1" ]]; then
	window_option="--args --new-window"
	open_option="-na"
fi

if [[ $query == "" ]]; then
	echo "1"
	echo $open_option "$browser" $window_option "https://google.com"
	open $open_option "$browser" $window_option "https://google.com"
elif [[ $query == "https://"* ]] || [[ $query == "http://"* ]]; then
	echo "2"
	echo $open_option "$browser" $window_option "$query"
	open $open_option "$browser" $window_option "$query"
elif [[ $query == *".co"* ]] || [[ $query == *".net"* ]] || [[ $query == *".kr"* ]]; then
	echo "3"
	echo $open_option "$browser" $window_option https://"$query"
	open $open_option "$browser" $window_option https://"$query"
else
	echo "4"
	url=`cat $urls_json | jq ".$site.query"`
	url=${url%\"}
	url=${url#\"}

	while [[ $url == *'$query'* ]]
	do
		url=${url/'$query'/$query}
	done
	echo $open_option "$browser" $window_option "$url"
	open $open_option "$browser" $window_option "$url"
fi 
