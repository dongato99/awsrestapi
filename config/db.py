from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:lolsitoforever@databasexd.c3qe5pxggdnm.us-east-1.rds.amazonaws.com:3306/storedb");

meta = MetaData()

conn = engine.connect()