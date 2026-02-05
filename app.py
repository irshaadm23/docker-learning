from flask import Flask
import redis
import os

app = Flask(__name__)

# Use env vars IF they exist, otherwise fall back to hardcoded values
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

@app.route("/")
def home():
    redis_client.incr("visits")
    return "CoderCo Containers Session!"

@app.route("/count")
def count():
    visits = redis_client.get("visits") or 0
    return f"Total visits so far: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
