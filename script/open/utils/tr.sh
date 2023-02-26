TR=`echo "$1" | tr '&' ','`
TR=`echo "$TR" | sed 's/ ,/,/g'`
TR=`echo "$TR" | sed 's/+/%2B/g'`
TR=`echo "$TR" | tr ' ' '+'`

echo $TR
