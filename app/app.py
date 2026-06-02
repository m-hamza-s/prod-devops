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
    return 1 / 0  # Crashes

@app.route('/health')
def health():
    # Return 500 so readiness probe fails
    return {"status": "unhealthy"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

