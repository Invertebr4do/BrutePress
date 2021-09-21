#!/bin/bash

#Colors
greenColor="\e[0;32m\033[1m"
endColor="\033[0m\e[0m"
redColor="\e[0;31m\033[1m"
blueColor="\e[0;34m\033[1m"
yellowColor="\e[0;33m\033[1m"
purpleColor="\e[0;35m\033[1m"
turquoiseColor="\e[0;36m\033[1m"
grayColor="\e[0;37m\033[1m"

function ctrl_c(){
	echo -e "\n\n${redColor}█ Exiting...\n"
	exit 1
}

trap ctrl_c INT

url=$(echo "$1" | tr '/' ' ' | awk '{print $1 "//" $2}') > /dev/null 2>&1

status=$(curl -s -I -X GET "$url/wp-json/wp/v2/users" | grep "HTTP" | awk '{print $2}')

if [ ! "$1" ]; then
	echo -e "\n${redColor}█ Use: ${purpleColor}$0 <${grayColor}url${purpleColor}>${endColor}"
	exit 1
else
	if [ "$status" == "200" ]; then
		users=$(curl -s "$url/wp-json/wp/v2/users" | tr ',' '\n' | grep "slug" | tr -d '"' | awk '{print $2}' FS=":" | xargs | sed 's/ /, /g') > /dev/null 2>&1
		echo -ne "\n${greenColor}█${grayColor} The following users were found ${greenColor}~>${grayColor} $users"
	fi
fi
