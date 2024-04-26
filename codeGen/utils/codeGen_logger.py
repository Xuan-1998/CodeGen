import atexit
import json
import logging.config
import logging.handlers
import os
import pathlib

import logging

# Dictionary to store handlers by name
handlers = {}

def setup_logging():
    # Create logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    # Store the handler with a name
    handlers['console_handler'] = ch

    return logger

def getHandlerByName(name):
    return handlers.get(name, None)

# Setup logging
logger = setup_logging()

# Retrieve a handler by name
queue_handler = getHandlerByName('console_handler')
if queue_handler:
    logger.info('Handler retrieved successfully')
else:
    logger.error('Handler not found')


working_directory = r"/Users/yibozhao/Documents/01 Johns Hopkins/02 LLM Code Generation/CodeGen/codeGen"

def setup_logging():
    config_file = pathlib.Path(f"{working_directory}/utils/logger.json")

    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

    logging.basicConfig(level="INFO")

    return logging.getLogger("__name__")