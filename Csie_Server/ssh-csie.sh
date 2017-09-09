if [ $# == 2 ] && [ $1 == 'oasis' ] && [ 0 -lt $2 ] && [ $2 -lt 4 ]; then # oasis
	echo "ssh b04902053@oasis$2.csie.org"
	ssh b04902053@oasis$2.csie.org
elif [ $# == 1 ]; then # linux or bsd1
	if [ $1 == 'bsd' ]; then # bsd
		echo "ssh b04902053@bsd1.csie.org"
		ssh b04902053@bsd1.csie.org
	elif [ 0 -lt $1 ] && [ $1 -lt 16 ]; then # linux
		echo "ssh b04902053@linux$1.csie.org"
		ssh b04902053@linux$1.csie.org
	fi
else # auto check for the best workstation
	output=`python3 /home/openopentw/git/small_scripts/Csie_Server/get_server_status_from_website.py`
	echo "ssh b04902053@$output.csie.org"
	ssh b04902053@$output.csie.org
fi
