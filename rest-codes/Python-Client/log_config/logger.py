import logging.handlers
import logging
import sys
from pytz import timezone, utc
from datetime import datetime


def custom_time(*args):
    """
    get the customised time
    :return:
    """
    utc_dt = utc.localize(datetime.utcnow())
    my_tz = timezone("Asia/Kolkata")
    converted = utc_dt.astimezone(my_tz)
    return converted.timetuple()


def get_logger(name):
    """
    get the customised logger for the given python file
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")
    logging.Formatter.converter = custom_time
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter('%(asctime)s — %(name)s — %(levelname)s - %(process)d - %(thread)d — %(funcName)s:%(lineno)d '
                          '— %(message)s'))
    logger.addHandler(handler)
    return logger
