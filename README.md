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
В процессе установки нужно будет нажать "Y" и "Enter" чтобы продолжить установку, затем будет предложено ввести парль для пользователя СУБД root

Переключаемся на python3 (cloud9 preferences python version)
Чтобы работать с MariaDB из Python нужно установить модуль python-mysqldb:
sudo pip3 install pymysql
Пример работы
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM books"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

Создать базу в скрипте баш
mysql -uroot -p123456 -e "create database myololodatabase;"

git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/testc9io/testmariadbrepo1.git
git push -u origin master