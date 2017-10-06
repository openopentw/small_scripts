if [ $# == 2 ] && [ $1 == 'oasis' ] && [ 0 -lt $2 ] && [ $2 -lt 4 ]; then # oasis
	echo "sftp b04902053@oasis$2.csie.ntu.edu.tw"
	sftp b04902053@oasis$2.csie.ntu.edu.tw
elif [ $# == 1 ]; then # linux or bsd1
	if [ $1 == 'bsd' ]; then # bsd
		echo "sftp b04902053@bsd1.csie.ntu.edu.tw"
		sftp b04902053@bsd1.csie.ntu.edu.tw
	elif [ 0 -lt $1 ] && [ $1 -lt 16 ]; then # linux
		echo "sftp b04902053@linux$1.csie.ntu.edu.tw"
		sftp b04902053@linux$1.csie.ntu.edu.tw
	fi
else # auto check for the best workstation
	output=`python3 /home/openopentw/git/small_scripts/csie_server/get_workstation_status_from_website.py`
	echo "sftp b04902053@$output.csie.ntu.edu.tw"
	sftp b04902053@$output.csie.ntu.edu.tw
fi
