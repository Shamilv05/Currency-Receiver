import logging
from aiomisc.log import basic_config

basic_config(level=logging.INFO, buffered=False, log_format='json')
log = logging.getLogger('service')
