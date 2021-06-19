import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'

 
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://vwdxutaimazqis:200cb9d2da6110fdeefa73ceafa92732f4f8c6e5757af42e705ce23d96edb9d8@ec2-3-234-22-132.compute-1.amazonaws.com:5432/d3sn5mpsvgl0r0?sslmode=require"
    #postgres://vwdxutaimazqis:200cb9d2da6110fdeefa73ceafa92732f4f8c6e5757af42e705ce23d96edb9d8@ec2-3-234-22-132.compute-1.amazonaws.com:5432/d3sn5mpsvgl0r0

class DevConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://deepeters:password@localhost/currency'
        DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
