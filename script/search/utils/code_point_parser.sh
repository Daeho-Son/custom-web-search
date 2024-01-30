echo -n "$1" | od -A n -t x1 | xargs -n 1 | sed 's/ //g' | tr '[a-z]' '[A-Z]' | pbcopy
echo $(pbpaste) > ./debug/1_original_hex.txt

touch tmp
for hex in $(pbpaste)
do
	echo "obase=2; ibase=16; $hex" | bc >> tmp
done

cat tmp > ./debug/2_original_binary.txt
parsed_binary=()
temp_binary=""
for b in $(cat tmp)
do
	# echo "TEST: $b" >> ./debug/test.txt
	if [[ $b -ge "100000" ]] && [[ $b -le "1111110" ]]; then
		# echo "ASCII" >> ./debug/test.txt
		parsed_binary+="$(echo $temp_binary | awk '{print substr($1, 5, 4) substr($2, 3, 6) substr($3, 3, 6)}') "
		parsed_binary+="$b "
		temp_binary=""
		continue
	fi
	if [[ ${#temp_binary} -lt 18 ]]; then
		temp_binary+="$b "
	else
		temp_binary+="$b"
		parsed_binary+="$(echo $temp_binary | awk '{print substr($1, 5, 4) substr($2, 3, 6) substr($3, 3, 6)}') "
		temp_binary=""
	fi
done

echo ${parsed_binary[@]} > ./debug/3_parsed_binary.txt


cat /dev/null > tmp
for binary in ${parsed_binary[@]}
do
	echo "obase=10; ibase=2; $binary" | bc >> tmp
done

code_points=()
for code_point in $(cat tmp)
do
	code_points+=($code_point)
done

echo ${code_points[@]} | tee ./debug/4_code_points.txt

# Clear
echo "" | pbcopy
rm tmp
# rm -r ./debug