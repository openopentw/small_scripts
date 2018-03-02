echo -n "Waiting for computer to completely boot "
for((i = 0; i < 10; ++i)); do
    sleep 3
    echo -n .
done

echo ""
sleep 20
in_dorm=`ipconfig | grep 140.112.247.82`
if [[ ! -z $in_dorm ]]; then
    netsh wlan start hostednetwork
fi
