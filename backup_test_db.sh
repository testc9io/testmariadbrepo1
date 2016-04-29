mysqldump -uroot -p123456 test_maria_db > test_maria_db_dump1.sql

mysql -uroot -p123456 test_maria_db < test_maria_db_dump1.sql