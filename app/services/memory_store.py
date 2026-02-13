import redis
import json

r = redis.Redis(host="localhost", port=6379)

def save_memory(session_id, message):
    r.rpush(session_id, json.dumps(message))

def get_memory(session_id):
    messages = r.lrange(session_id, 0, -1)
    return [json.loads(m) for m in messages]
