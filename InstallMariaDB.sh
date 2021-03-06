sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
sudo add-apt-repository 'deb [arch=amd64,i386] http://mirror.mephi.ru/mariadb/repo/10.1/ubuntu trusty main'
sudo apt-get update
sudo apt-get install -y mariadb-server

sudo pip3 install pymysql

mysql -uroot -p123456 -e "CREATE DATABASE IF NOT EXISTS test_maria_db;"