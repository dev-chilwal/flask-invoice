"""Flask Configuration"""

from distutils.debug import DEBUG
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:

    # Flask Config Variables
    SECRET_KEY = environ.get('SECRET_KEY')
    UPLOAD_FOLDER = 'static/uploads'
    ALLOWED_EXTENSIONS = {'pdf'}

    # AWS Secrets
    #AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    #AWS_KEY_ID = environ.get('AWS_KEY_ID')


class ProdConfig(Config):

    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False

    # DB
    MONGO_URI = environ.get('PROD_MONGO_URI')

    # AWS Secrets
    #AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    #AWS_KEY_ID = environ.get('AWS_KEY_ID')


class DevConfig(Config):

    FLASK_ENV = "dev"
    DEBUG = True
    TESTING = True

    # DB
    MONGO_URI = environ.get('DEV_MONGO_URI')

    # AWS Secrets
    #AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    #AWS_KEY_ID = environ.get('AWS_KEY_ID')
