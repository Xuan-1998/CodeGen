import atexit
import json
import logging.config
import logging.handlers
import os
import pathlib

working_directory = "/Users/jiangxuan/Desktop/09_CodeGen/CodeGen/codeGen"

def setup_logging():
    config_file = pathlib.Path(f"{working_directory}/utils/logger.json")

    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

    logging.basicConfig(level="INFO")

    return logging.getLogger("__name__")