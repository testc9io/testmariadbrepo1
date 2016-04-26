В терминале выполнить команду чтобы узнать версию линукса на котором сейчас работаем
lsb_release -a

На сайте mariadb в разделе downloads:
https://downloads.mariadb.org/mariadb/repositories/#mirror=mephi
Выбрать нужный версию линукса и любое зеркало

Подготовленный сайтом список команд записать в sh-файл InstallMariaDB.sh
Т.е. записать в этот файл примерно следующие строки:
sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
sudo add-apt-repository 'deb [arch=amd64,i386] http://mirror.mephi.ru/mariadb/repo/10.1/ubuntu trusty main'
sudo apt-get update
sudo apt-get install mariadb-server

Чтобы исполнить этот файл в терминале нужно набрать:
sudo sh InstallMariaDB.sh
(Регистр значение имеет)