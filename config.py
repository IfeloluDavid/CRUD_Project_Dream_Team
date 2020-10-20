# config.py

# Enable Flask's debugging features. 
# Should be False in production


class Config(object):
    """
    Common Configurations
    """

    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development Configurations
    """

    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Configuration
    """

    DEBUG = False

class TestingConfig(Config):
    """
    Testing Configuration
    """
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
