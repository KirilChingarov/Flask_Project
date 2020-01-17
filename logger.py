import logging
from logging.handlers import RotatingFileHandler


infolog = logging.getLogger('infolog')
infolog.setLevel(logging.INFO)
errorlog = logging.getLogger('errorlog')
errorlog.setLevel(logging.ERROR)

infohandler = RotatingFileHandler('var/log/info.log', maxBytes=10000, backupCount=5)
errorhandler = RotatingFileHandler('var/log/error.log', maxBytes=10000, backupCount=5)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
infohandler.setFormatter(formatter)
errorhandler.setFormatter(formatter)

infolog.addHandler(infohandler)
errorlog.addHandler(errorhandler)
