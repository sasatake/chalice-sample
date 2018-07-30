import logging
from pythonjsonlogger import jsonlogger
import datetime
import os


class JsonFormatter(jsonlogger.JsonFormatter):
    def parse(self):
        return ['timestamp', 'levelname', 'name', 'funcName']

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.datetime.now().strftime(
                os.getenv("TIME_STAMP_FORMAT"))
            log_record['timestamp'] = now


def getLogger(module_name):
    logger = logging.getLogger(module_name)
    handler = logging.StreamHandler()
    formatter = JsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
    return logger
