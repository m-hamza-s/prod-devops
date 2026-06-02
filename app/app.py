from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)


@app.route('/')
def home():
    count = redis_client.incr('hits')
    return {
        "message": "DevOps Stage 2 - Rolling Update!",
        "version": "v2",
        "hit_count": count
    }

@app.route('/health')
def health():
    return {"status": "healthy", "version": "v2"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

