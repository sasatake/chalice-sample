import logging
from pythonjsonlogger import jsonlogger
import datetime


class JsonFormatter(jsonlogger.JsonFormatter):
    def parse(self):
        return ['timestamp', 'level', 'name', 'funcName']

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # https://qiita.com/yoppe/items/4260cf4ddde69287a632
            now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


def getLogger(module_name):
    logger = logging.getLogger(module_name)
    handler = logging.StreamHandler()
    formatter = JsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
