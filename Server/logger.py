# -*- coding: utf-8 -*-
# @File       : logger.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/19 11:19
# @Description:

import logging
import os
import time
import coloredlogs
from Server.settings import LOGGING_CONSOLE_FLAG,LOGGING_FILE_LOG,LOGGING_CURRENT_LEVEL

# -----------------------------------------------------------------------------
# Create or get a logger
# -----------------------------------------------------------------------------
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Set the format of logger
# -----------------------------------------------------------------------------
fmt = '%(asctime)s - [%(name)s] - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s'
formatter = logging.Formatter(fmt)

# -----------------------------------------------------------------------------
# Create Handler, output log to console and file
# -----------------------------------------------------------------------------
# FileHandler
basedir = os.path.abspath(os.path.dirname(__file__))
log_dest = os.path.join(basedir, 'Log')  # directory
if not os.path.isdir(log_dest):
    os.mkdir(log_dest)
filename = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'  # name of the log: current time




# -----------------------------------------------------------------------------
# add handler to Logger
# -----------------------------------------------------------------------------
if(LOGGING_FILE_LOG):
    file_handler = logging.FileHandler(os.path.join(log_dest, filename), encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
if(LOGGING_CONSOLE_FLAG):
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# -----------------------------------------------------------------------------
# Set logger level
# -----------------------------------------------------------------------------
logger.setLevel(logging.DEBUG)

# -----------------------------------------------------------------------------
# Logger with color
# -----------------------------------------------------------------------------
coloredlogs.DEFAULT_FIELD_STYLES = dict(
    asctime=dict(color='green'),
    name=dict(color='blue'),
    filename=dict(color='magenta'),
    lineno=dict(color='cyan'),
    levelname=dict(color='black', bold=True),
)

# Set logger mode
if not LOGGING_CONSOLE_FLAG:
    coloredlogs.install(fmt=fmt, level='CRITICAL', logger=logger)
else:
    coloredlogs.install(fmt=fmt, level=LOGGING_CURRENT_LEVEL, logger=logger)
