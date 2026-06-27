from Models.Model_Book import ModelBook
import sqlite3 as sql

class SvBook:

    def __init__(self):
        self.con = sql.connect(r'e:\PROJECT\Py-Project-Library\Mobtakeran\LibraryProjectPy\DataBase\DbLibrary.db')
        self.cur = self.con.cursor()
    
    def Insert(self ,book:ModelBook):
        #Save to dataBase
        print("Save to DataBase")
        
    
    def Search(ID):
        #search books by id 
        pass

    def GetAll(self):
        #Get All Books 
       
       self.cur.execute("select * from Books")
       booklist = self.cur.fetchall()
       self.con.close()
       return booklist
    