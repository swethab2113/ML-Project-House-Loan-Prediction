import logging
import os
from datetime import datetime

class CustomLogger:
    """Creating a custom logger"""
    def __init__(self, log_dir='logs'):
        # create a "logs" directory to store log files
        self.log_dir = os.path.join(os.getcwd(), log_dir)         
        os.makedirs(self.log_dir, exist_ok=True)

        # create log file path
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path = os.path.join(self.log_dir, log_file)

        # configure python's logging system to the file
        logging.basicConfig(
            filename = log_file_path,
            level = logging.INFO,
            format = "[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s"
        )
    
    def get_logger(self, name = __file__):
        # create a logger instance using the current file name
        return logging.getLogger(os.path.basename(name))

# test logging    
# if __name__ == "__main__":
#     logger = CustomLogger()
#     logger = logger.get_logger(__file__)
#     logger.info("Logger is initialized successfully.")