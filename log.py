import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)
hdlr = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
hdlr.setLevel(logging.INFO)
logger.addHandler(hdlr)
