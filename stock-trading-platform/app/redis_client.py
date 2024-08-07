import redis

client = redis.Redis(host='redis', port=6379, decode_responses=True)

def set_value(key, value):
    client.set(key, value)

def get_value(key):
    return client.get(key)
