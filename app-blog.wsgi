APP_CONFIG = "/srv/http/proloco/proloco/production.ini"

#Setup logging
#import logging.config
#logging.config.fileConfig(APP_CONFIG)

#Load the application
from paste.deploy import loadapp
application = loadapp('config:%s' % APP_CONFIG)
