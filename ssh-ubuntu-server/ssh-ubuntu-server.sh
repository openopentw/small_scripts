ubuntu_64=$(/c/Program\ Files/Oracle/VirtualBox/VBoxManage.exe list runningvms | grep ubuntu-server-64)
ubuntu_32=$(/c/Program\ Files/Oracle/VirtualBox/VBoxManage.exe list runningvms | grep ubuntu-server-32)

if [[ ! -z $ubuntu_64 ]] && [[ ! -z $ubuntu_32 ]]; then
	read -p "Please choose 64 or 32: " arch
elif [[ ! -z $ubuntu_64 ]] ; then
	arch='64'
elif [[ ! -z $ubuntu_32 ]] ; then
	arch='32'
fi

if [[ $arch == '64' ]]; then
	cmd='ssh ubuntu-server-64@192.168.56.1'
	echo $cmd
	$cmd
elif [[ $arch == '32' ]]; then
	cmd='ssh -p 23 ubuntu-server-32@192.168.56.1'
	echo $cmd
	$cmd
fi
