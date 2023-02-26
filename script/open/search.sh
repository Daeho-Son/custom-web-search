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


# Open option
if [[ $is_new_window == "0" ]]; then
	option="-a $browser"
else
	option="-na $browser --args --new-window"
fi


# URL & Run
url=$query
if [[ $query == "" ]]; then
	open "$option"
elif [[ $query == *"https://"* ]] || [[ $query == *"http://"* ]]; then
	open "$option" "$url"
elif [[ $query == *".co"* ]]; then
	open "option" https://"$url"
else
	url=`cat $urls_json | jq ".$site.query"`
	url=${url%\"}
	url=${url#\"}

	while [[ $url == *'$query'* ]]
	do
		url=${url/'$query'/$query}
	done

	open "$option" "$url"
fi 
