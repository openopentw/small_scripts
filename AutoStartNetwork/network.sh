in_dorm=`ipconfig | grep 140.112.247.82`
if [[ ! -z $in_dorm ]]; then
	netsh wlan start hostednetwork
fi
