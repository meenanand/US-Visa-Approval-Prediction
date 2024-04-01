import os 
import sys 

def error_message_detail(error , error_detail:sys):
    _,_,exc_tb = error_detail.exe_info()

    file_name =exc_tb.tb.frame.f_code.co_filename

    error_message = "Error occured python script name [{0}] line number [{1}]"    