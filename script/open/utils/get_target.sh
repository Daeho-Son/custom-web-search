DIR=$1
SH_NAME=$2
IS_NEW_WINDOW=$3

if [[ "$IS_NEW_WINDOW" == "1" ]]; then
	SH_NAME="${SH_NAME}_new_window.sh"
else
	SH_NAME="${SH_NAME}.sh"
fi

echo $DIR/$SH_NAME