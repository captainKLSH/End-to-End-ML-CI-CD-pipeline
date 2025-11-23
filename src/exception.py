import sys
from src.logger import logging

def errorMessage(error,errorDetail:sys):
    _,_,excTm=errorDetail.exc_info()
    file_name=excTm.tb_frame.f_code.co_filename
    errorMess="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,excTm.tb_lineno,str(error)
    )

    return errorMess

class customException(Exception):
    def __init__(self, errorMess,errorDetail:sys):
        super().__init__(errorMess)
        self.errorMess=errorMessage(errorMess,errorDetail=errorDetail)
    def __str__(self):
        return self.errorMess