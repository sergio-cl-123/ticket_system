class Config:
    secret_key = 'mysecretkey'

class DevelopmentConfig(Config):
    DEBUG = True
    host = "mysql-limiteurbano.alwaysdata.net",
    user = "320313_lu",
    password = "9!8z5WvPqXs5MBw",
    database = 'limiteurbano_loginDB'

config = {
    'development': DevelopmentConfig
}