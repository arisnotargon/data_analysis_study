from sqlalchemy import create_engine
import config
from model.Test import Test
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm  as  sqlorm
import datetime

Base = declarative_base()
pg_conf = config.psql_conf
engine = create_engine('postgresql://%s:%s@%s:%s/%s' % (
    pg_conf['user'],
    pg_conf['password'],
    pg_conf['host'],
    pg_conf['port'],
    pg_conf['dbname'],
),echo=pg_conf["debug"])
#echo = Truw可以打印每条语句
Base.metadata.bind = engine
Base.metadata.create_all()

session = sqlorm.scoped_session(sqlorm.sessionmaker(bind=engine))
for item in session.query(Test):
    print(item.name)

now_time = datetime.datetime.now()