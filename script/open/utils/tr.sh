TR="$1"
# TR=`echo "$TR" | tr '&' ','`
TR=`echo "$TR" | sed 's/ ,/,/g'`
TR=`echo "$TR" | sed 's/+/%2B/g'`

echo $TR
