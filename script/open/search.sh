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
		echo "jq 라이브러리를 설치해주세요"
		exit
	fi
fi


browser="Google Chrome"

# Error
# - $browser 로 사용하면 작동X -> "$browser"
# - $browser 를 다른 변수에 넣어서 사용하면 작동x -> 직접 사용
# # Open option
# if [[ $is_new_window == "0" ]]; then
# 	option="-a $browser"
# else
# 	option="-na $browser --args --new-window"
# fi


# URL & Run
if [[ $is_new_window == "0" ]]; then
	if [[ $query == "" ]]; then
		url=`cat $urls_json | jq ".$site.base"`
		url=${url%\"}
		url=${url#\"}
		open -a "$browser" "$url"
	elif [[ $query == *"https://"* ]] || [[ $query == *"http://"* ]]; then
		open -a "$browser" "$query"
	elif [[ $query == *".co"* ]]; then
		open -a "$browser" https://"$query"
	else
		url=`cat $urls_json | jq ".$site.query"`
		url=${url%\"}
		url=${url#\"}

		while [[ $url == *'$query'* ]]
		do
			url=${url/'$query'/$query}
		done

		open -a "$browser" "$url"
	fi 
else
	if [[ $query == "" ]]; then
		url=`cat $urls_json | jq ".$site.base"`
		open -na "$browser"
	elif [[ $query == *"https://"* ]] || [[ $query == *"http://"* ]]; then
		open -na "$browser" --args --new-window "$query"
	elif [[ $query == *".co"* ]]; then
		open -na "$browser" --args --new-window https://"$query"
	else
		url=`cat $urls_json | jq ".$site.query"`
		url=${url%\"}
		url=${url#\"}

		while [[ $url == *'$query'* ]]
		do
			url=${url/'$query'/$query}
		done

		open -na "$browser" --args --new-window "$url"
	fi 

fi
