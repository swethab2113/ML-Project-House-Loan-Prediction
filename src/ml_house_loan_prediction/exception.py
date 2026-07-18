import sys
from ml_house_loan_prediction.logger import CustomLogger
class CustomException(Exception):
    """Creating a custom exception"""
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)                     # inherit __init__ method from parent class Exception
        _, _, exc_tb = error_details.exc_info()             # get traceback object to find file and line number where error occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename # get file name from traceback
        self.line_num = exc_tb.tb_lineno                    # get line number from traceback
        self.error_message = f"Error occured. \n Script: {self.file_name} \n Line number: {self.line_num} \n Error message: {str(error_message)}"
        
    def __str__(self):
        return self.error_message

# test exception
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         app_exc = CustomException(e, sys)
#         logger = CustomLogger().get_logger(__file__)
#         logger.error(app_exc)
#         raise app_exc