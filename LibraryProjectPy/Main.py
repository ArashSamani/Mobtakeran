#MAIN
from Models.Model_Book import ModelBook
from Sv.sv_Book import SvBook


_newbokk = ModelBook(NAME='c#',TITLE='asp',COUNT=4)
_service = SvBook()
_service.Insert(_newbokk)


import sqlite3 as sql

con = sql.connect('e:\PROJECT\Py-Project-Library\Mobtakeran\LibraryProjectPy\DataBase\DbLibrary.db')

cur = con.cursor()


cur.execute("select * from Books")
booklist = cur.fetchall()
print(booklist[0])

con.close()
