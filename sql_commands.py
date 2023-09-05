import sqlite3

with sqlite3.connect('maffin') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY,
    cursor.execute('CREATE TABLE Transaction (id INT AUTO_INCREMENT PRIMARY KEY, date TEXT, categoria TEXT, summ INT