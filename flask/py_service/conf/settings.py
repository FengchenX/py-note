class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE='postgres'
    DBUSER='postgres'
    DBPWD='123456'
    # DBHOST='192.168.2.245'
    # DBHOST='192.168.43.245'
    DBHOST='192.168.1.245'
    DBPORT='5432'

# class ProductionConfig(Config):
#     pass
# class DevelopmentConfig(Config):
#     DEBUG = True

# class TestingConfig(Config):
#     TESTING = True