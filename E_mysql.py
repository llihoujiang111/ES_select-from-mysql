# encoding=utf-8
import pymysql

DATABASE = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "passwd": "****",
    "db": "****",
    "charset": "utf8"

}
def insert_db(count, parm_key):
    db = pymysql.connect(host=DATABASE["host"], port=DATABASE["port"], user=DATABASE["user"], passwd=DATABASE["passwd"],
                         db=DATABASE["db"], charset=DATABASE["charset"])
    cun = db.cursor()
    select_sql = "select * from yourmysqodb"
    cun.execute(select_sql, parm_key)
    select_sqls = cun.fetchall()
    if len(select_sqls) == 0:
        spl = 'insert into yourmysqodb'''
        cun.execute(spl, count)
        db.commit()
        cun.close()
        db.close()
    else:
        print('-----------数据库存在---------------')
