import json
from logging import StreamHandler, Formatter, getLogger
import traceback


class FormatterJSON(Formatter):
    def format(self, record):
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        j = {
            'logLevel': record.levelname,
            'process': record.process,
            'timestamp': '%(asctime)s' % dict(asctime=record.asctime),
            'message': record.getMessage(),
            'module': record.module,
            'filename': record.filename,
            'funcName': record.funcName,
            'lineno': record.lineno,
            'traceback': [],
            'parameters': record.__dict__.get('parameters', {}),
        }
        if record.exc_info:
            exception_data = traceback.format_exc().splitlines()
            j['traceback'] = exception_data
        return json.dumps(j, ensure_ascii=False)


def get_logger(module_name, level="DEBUG"):
    logger = getLogger(module_name)
    handler = StreamHandler()
    formatter = FormatterJSON('%(asctime)s')
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False

    return logger


def test_log():
    """
    テスト
    """

    logger = get_logger(__name__)
    try:
        value = dict(a='abc', b='def', c=123)
        data = {}
        data['parameters'] = value
        logger.info('Start hello Func', extra=dict(data))

        # 例外を発生させる
        print(1 / 0)

    except ZeroDivisionError as error:
        data = {"a": "aaa"}
        logger.error(error, extra=dict(data))
        logger.exception(error, extra=dict(data))


if __name__ == "__main__":
    test_log()
