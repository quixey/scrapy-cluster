import os
import ConfigParser
import logging
#BC from exc import ConfigError

logger = logging.getLogger(__name__)

def get_env():
    env = None
    try:
        env = os.environ['env']
        logger.info("Found env: "+env)
    except:
        logger.debug("Cannot read system env variable")
    if env == None or env.strip() == "":
        logger.debug("Environment variable env not set. Setting it to dev as default")
        env ='dev'
    return env

def get_config_parser():
    env = get_env()
    config = ConfigParser.ConfigParser()
    default_config = './config/RssSpider-default.cfg'
    config_file = './config/RssSpider-'+env+'.cfg';
    ok = config.read([default_config,config_file])
    logger.info("Successfully read "+str(ok)+" config files")
    if(len(ok) == 2):
        logger.info("Successfully read config file: "+config_file)
#BC    else:
#BC        raise ConfigError
    return config
        
