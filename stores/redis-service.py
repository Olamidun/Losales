import redis
import json

redis_client = redis.StrictRedis(port=6379, db=0)

class RedisClass:
    def set(cache_key, data):
        redis.set(cache_key, json.dumps(data))
        return True

    def get(cache_key):
       cache_data = redis.get(cache_key)
       cache_data = json.loads(cache_data)

       return cache_data