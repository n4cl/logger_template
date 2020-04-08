from logzero import logger, LogFormatter, setup_default_logger


def set_logger() -> None:
    log_format = '%(color)s[%(levelname)1.1s process:%(process)d %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
    formatter = LogFormatter(fmt=log_format)
    setup_default_logger(formatter=formatter)


if __name__ == "__main__":
    set_logger()
    logger.info("Hello world")
    logger.error("Hello world")
    logger.exception("Hello world")
