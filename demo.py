from hate.logger import logging
import sys
from hate.exception import CustomException

logging.info("Welcome to our project")

try:
    a=7/"0"
except Exception as e:
    raise CustomException(e,sys) from e