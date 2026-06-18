#MAIN
from Models.Model_Book import ModelBook
from Sv.sv_Book import SvBook


_newbokk = ModelBook(NAME='c#',TITLE='asp',COUNT=4)
_service = SvBook()
_service.Insert(_newbokk)
