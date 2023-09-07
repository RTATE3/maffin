import sqlite3

with sqlite3.connect(r'C:\Users\edgerunner\PycharmProjects\maffin\maffin.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, login TXT, password TXT);')
    cursor.execute('CREATE TABLE IF NOT EXISTS FinTransaction (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, categoria TEXT, summ INT);')