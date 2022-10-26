from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://masterusername:myspmdbcom@spm-instance-identifier.c2gotl0sxsdt.ap-southeast-1.rds.amazonaws.com/myspmdbname"
engine = create_engine(DATABASE_URL)

conn = engine.connect(close_with_result=False)
session = sessionmaker(bind=engine)

meta = MetaData()
