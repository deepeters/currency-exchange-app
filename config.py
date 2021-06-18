import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'

 
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://dulfrqrkamwwcb:109cdefcd744280f24480af769762f1158267b87ae59ace20d612555b2869f07@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d21mkvhn8nmuc9?sslmode=require"


class DevConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://deepeters:password@localhost/currency'
        DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
