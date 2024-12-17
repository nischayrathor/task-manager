"""
    module to keep common utilities (logger)
"""
import logging
import sys

def logger_config():
    """
        Log configuration function
    """
    # define the format of the log entries
    logging.basicConfig(stream=sys.stdout, format='%(levelname)s:     %(asctime)s  -  %(message)s')
    logger = logging.getLogger("task-manager")
    logger.setLevel(logging.DEBUG)
    return logger