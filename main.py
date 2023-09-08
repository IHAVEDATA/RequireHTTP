import requests
import threading

running = True

r = requests

threads = []


class CallHttp:

    repeat = 0

    @staticmethod
    def sendPost(address, repeat, number):
        for i in range(repeat):
            r.post(address)
            print(f"http request {i} is complete of {number} thread")


caller = CallHttp

for threadNumber in range(1000):
    tSendPost = threading.Thread(target=caller.sendPost, args=("", 5000, threadNumber))
    tSendPost.start()
