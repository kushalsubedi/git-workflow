import time 
import redis

from flask import Flask 
app = Flask (__name__)

cache =redis.Redis(host='redis',port=6379)

def get_hit_count():
    retries = 5 
    while True:
        try: 
            return cache.incr('hits')
        except redis.exception.ConnectionError as  exc:
            if retries == 0:
                raise exc 
            retries -=1
            time.sleep(0.5)



@app.route('/')
def hello_route():
    count = get_hit_count()
    print("Good it works")
    return f"Hello World From Docker !! I have seen this {count}times"


if __name__ == '__main__':
    app.run (debug = True, host="0.0.0.0",port=8000 )
