import os
from decouple import config
from flask_mysqldb import MySQL, MySQLdb


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    # SQLALCHEMY_DATABASE_URI = "mysql://root:kentland55@localhost:3306/sports_data"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='root'),
        config('DB_PASS', default='kentland55'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=3306),
        config('DB_NAME', default='sports_data')
    )


class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
