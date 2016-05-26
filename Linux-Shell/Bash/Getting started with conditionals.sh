read response
response=${response,,}
if [[ $response =~ ^(yes|y)$ ]]; then
	echo "YES"
else 
	echo "NO"
fi