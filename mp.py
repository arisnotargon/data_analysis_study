# -*- coding:utf-8 -*-#

import redis
import gzip
import json
import logging
import psycopg2
import time

logging.basicConfig(filename=time.strftime("%Y_%m_%d", time.localtime())+ ".log", level=logging.DEBUG)

logging.critical('log')
exit()

psql_conf = {
    "dbname": "bida_analytics",
    "user": "postgres",
    "password": "159753",
    "host": "127.0.0.1",
    "port": "5432",
}

psql_conf_str = ""
for (k, v) in psql_conf.items():
    psql_conf_str += k + "=" + v + " "

psql_conf_str = psql_conf_str[:-1]

conn = psycopg2.connect(psql_conf_str)
cur = conn.cursor()

cur.execute("""
    select * from bida_analytics.public.test where id = %s
""",["1 or 1=1"])

rows = cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()