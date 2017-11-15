# check if sudoed
if [ "$EUID" -ne 0 ]
  then echo "Please run as root."
  exit
fi

# upgrade system
echo "========================"
echo "=== Upgrading System ==="
echo "========================"
apt update
apt upgrade

# install my vimrc
echo "==================================="
echo "=== installing openopentw/Vimrc ==="
echo "==================================="
git clone https://github.com/openopentw/Vimrc
cp Vimrc/.vimrc ~/
cp -r Vimrc/.vim ~/
mkdir ~/tmp
vim +PlugInstall +qall

# install YouCompleteMe
echo "================================"
echo "=== installing YouCompleteMe ==="
echo "================================"
apt install build-essential cmake
apt install python3-dev
python3 ~/.vim/plugged/YouCompleteMe/install.py --clang-completer

# install gdb
echo "======================"
echo "=== installing gdb ==="
echo "======================"
apt install gdb

# install gdb peda
echo "==========================="
echo "=== installing gdb peda ==="
echo "==========================="
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
echo "DONE! debug your program with gdb and enjoy"
