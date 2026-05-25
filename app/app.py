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
        "message": "DevOps Stage 1 - Running in Docker!",
        "hit_count": count
    }

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
