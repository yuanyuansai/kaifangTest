import redis


class Operation_redis:
    def __init__(self):
        self.conn = redis.StrictRedis(
            host="r-2zevydf8nbsjcbuwhp.redis.rds.aliyuncs.com",
            password="Thu1911thu",
            port=6379,
            db=0
        )

    def search_string(self,key):
        ret = self.conn.get(key)
        ret1=str(ret,encoding='utf-8')
        return ret1


if __name__ == '__main__':
    print(Operation_redis().search_string("jwtTokenKey_200000139_app"))
