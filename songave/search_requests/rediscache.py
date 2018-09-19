import rediscache


class RedisCache:
    def __init__(self, host="127.0.0.1", port=6379, db=0):
        redis_db = redis.StrictRedis(host=host, port=port, db=db)

    def get_key(self, key):
        redis_db.get(key)

    def set_key(self, key, value):
        redis_db.set(key, value)

    def __contains__(self, key):
        return self.redis_db.keys.exists(key)

    @property
    def size(self):
        return len(self.redis_db.items())


class HashTableCache(RedisCache):
    """
    Hash table redis cache, used to store requests as objects.
    every object have properties and assigned to a key:
    item
        url_id sdfsdfsd
    """
    def __init__(self):
        super().__init__()

    def set_key(self, key, value):
