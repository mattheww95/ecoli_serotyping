#!/usr/bin/env python

"""
    Set up the logging
"""

import logging
import tempfile
import os
from tqdm import tqdm
from ectyper import definitions

LOG = logging.getLogger(__name__)

'''
https://stackoverflow.com/questions/38543506/change-logging-print-function-to-tqdm-write-so-logging-doesnt-interfere-wit
'''
class TqdmLoggingHandler (logging.Handler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        tqdm()

    def emit(self, record):
        msg = self.format(record)
        tqdm.write(msg)

def initialize_logging(log_file=None):
    '''
    setup logging to stream INFO log to console
    and ALL log to log_file
    :param
        log_file (str): log filename [optional]
    :return
        Log filename
    '''
    if log_file is None:
        log_file = os.path.join(definitions.ROOT_DIR, 'default.log')


    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)02d %(name)-25s %(levelname)-8s %(message)s',
                        datefmt='%y-%m-%d %H:%M:%S',
                        filename=log_file,
                        filemode='w')
    # If logger already exist, return the existing logger
    if len(logging.getLogger('').handlers)>1:
        return log_file
    # add the handler to the root logger
    tqdm_logger = logging.getLogger('')
    tqdm_logger.setLevel(logging.INFO)
    tqdm_logger.addHandler(TqdmLoggingHandler())

    # Now, we can log to the root logger, or any other logger. First the root...
    LOG.info('Logger initialized. Debug log stored at %s', log_file)
    return log_file