from multiprocessing import Process, Queue
from UserActivity import getUserActivity
import sys
if __name__ == '__main__':
    message = Queue()
    getUserActivity('d43f1ff7-ae36-4b1e-9af8-98a9cf027c22',message).start()
    try:
        while True:
            if not message.empty():
                data = message.get()
                if data['type'] == 'activity':
                    for v in data['data']:
                        print(v)
    except KeyboardInterrupt :
        sys.exit(0)

