from logging import getLogger, StreamHandler, DEBUG
from pythonjsonlogger import jsonlogger
from datetime import datetime, timezone, timedelta


class JsonFormatter(jsonlogger.JsonFormatter):

    def parse(self):
        return [
            'level',
            'process',
            'timestamp',
            'filename'
            'funcName',
            'lineno',
            'message',
        ]

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            JST = timezone(timedelta(hours=+9), 'JST')
            now = datetime.now(JST).strftime('%Y-%m-%d %H:%M:%S')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


def get_logger(module_name, level='DEBUG'):
    logger = getLogger(module_name)
    handler = StreamHandler()
    formatter = JsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)

    return logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Hello world.")
    try:
        0/0
    except Exception as e:
        import traceback
        logger.error("Hello world.", extra={"traceback": traceback.format_exc().splitlines()})

    logger = get_logger("test", "ERROR")
    logger.info("Hello world.")
