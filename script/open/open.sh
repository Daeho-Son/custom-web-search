OS=`uname`

is_new_window=$1
browser=$2
site=$3
query=$4
urls_json=$5


# Install jq
jq --version > /dev/null 2>$1
if [[ $? == "127" ]]; then
	echo "jq: command not found"
	if [[ $OS  == "Darwin" ]]; then
		brew install jq
	else
		echo "jq 라이브러리를 설치해주세요"
		exit
	fi
fi



# URL
if [[ $query == "" ]]; then
	url=`cat $urls_json | jq ".$site.base"`
else
	url=`cat $urls_json | jq ".$site.query"`
fi
url=${url%\"}
url=${url#\"}

while [[ $url == *'$query'* ]]
do
	url=${url/'$query'/$query}
done
echo $url


# Open option
if [[ $is_new_window == "0" ]]; then
	open -a "$browser" "$url"
else
	open -na "$browser" --args --new-window "$url"
fi
