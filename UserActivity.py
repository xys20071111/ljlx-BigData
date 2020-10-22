from multiprocessing import Process,Queue
from requests import get
from time import sleep
class getUserActivity(Process):
    def __init__(self,siteID,msg):
        super().__init__()
        self.__siteID = siteID
        self.__msg = msg
    def run(self):
        while True:
            res = get('http://eduyun.ljlx.com/appdata/stat/mapDynamic?top=200&siteId=' + self.__siteID).json()
            data = res['data']
            result = list()
            for v in data:
                result.append(v["publishDate"]+v["areaName"] + v["content"] + ' uid:'+ str(v["userId"]))
            self.__msg.put({'type':'activity','data':result})
            sleep(3)
if __name__ == "__main__":
    msg = Queue()
    getUserActivity('d43f1ff7-ae36-4b1e-9af8-98a9cf027c22',msg).run()
    while True:
        print(msg.get())
        sleep(5)       