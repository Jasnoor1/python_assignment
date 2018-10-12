import redis
import time
import random


config = {
            'host': 'localhost',
                'port': 6379,
                    'db': 0,
                    }

r = redis.StrictRedis(**config)

if __name__ == '__main__':
    while True:
        rand_value = random.random()
        print( "sent {}".format(rand_value))
        a=r.publish("get_rand_numbers", rand_value)
        print('gdyaskfas',a)
        time.sleep(random.randint(1,3))
