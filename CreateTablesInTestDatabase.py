import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='test_maria_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create table books
        sql = "CREATE TABLE IF NOT EXISTS books (BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(100) NOT NULL, SeriesID INT, AuthorID INT)"
        cursor.execute(sql)
        connection.commit()
        # Create table authors
        sql = "CREATE TABLE IF NOT EXISTS authors (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT)"
        cursor.execute(sql)
        connection.commit()
        # Create table series
        sql = "CREATE TABLE IF NOT EXISTS series (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT)"
        cursor.execute(sql)
        connection.commit()
        # Insert
        sql = "INSERT INTO books (Title,SeriesID,AuthorID) VALUES('The Fellowship of the Ring',1,1),\
              ('The Two Towers',1,1), ('The Return of the King',1,1),  ('The Sum of All Men',2,2),\
              ('Brotherhood of the Wolf',2,2), ('Wizardborn',2,2), ('The Hobbbit',0,1)"
        
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()


'''

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO 'books' ('Title', 'SeriesID', 'AuthorID') VALUES (%s, %s, %s)"
        cursor.execute(sql, ('webmaster@python.org', '7', '7'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT 'BookID', 'Title', 'SeriesID', 'AuthorID' FROM 'books'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

'''

'''

CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS books (
  BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
  Title VARCHAR(100) NOT NULL, 
  SeriesID INT, AuthorID INT);

CREATE TABLE IF NOT EXISTS authors (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);

CREATE TABLE IF NOT EXISTS series (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);

INSERT INTO books (Title,SeriesID,AuthorID) VALUES('The Fellowship of the Ring',1,1), 
 ('The Two Towers',1,1), ('The Return of the King',1,1),  ('The Sum of All Men',2,2),
 ('Brotherhood of the Wolf',2,2), ('Wizardborn',2,2), ('The Hobbbit',0,1);
 
 '''