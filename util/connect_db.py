import pymysql.cursors
import json
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host="rm-2ze67p557wd9p0m70.mysql.rds.aliyuncs.com",
            port=3306,
            user='root',
            password='arNV3CN7gTwMGt5nMm',
            database='dev_1911edu',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
            )
        self.cur = self.conn.cursor()
    def search_one(self):
        sql="SELECT id FROM `user` WHERE user_name = 13681319134"
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        ret = json.loads(result)
        return ret['id']

if __name__ == '__main__':
    ret = OperationMysql().search_one()
    print(ret)
