#MAIN
from Models.Model_Book import ModelBook
from Sv.sv_Book import SvBook




_serviceBook = SvBook()

for x in _serviceBook.GetAll():
    print(x)

