from settings import r
import sys

if __name__ == '__main__':
    name = sys.argv[0]
    channel  = sys.argv[0]

    print('Welcome to {channel}'.format(**locals()))

    while True:
        message = input('Enter a message:')

        if message.lower() == 'exit':
            break
        message = '{name} says: {message}'.format(**locals())

        r.publish(channel,message)
        
