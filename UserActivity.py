from requests import get
from threading import Thread
import socket
class getUserActivity(Thread):
    def __init__(self,siteID):
        self.__siteID = siteID
        self.__rpc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__rpc.connect(('127.0.0.1',5624))
        super().__init__()
    def run(self):
        res = get('http://eduyun.ljlx.com/appdata/stat/mapDynamic?top=200&siteId=' + self.__siteID)
        data = res.text
        self.__rpc.sendall(data.encode("utf-8"))
if __name__ == "__main__":
    getUserActivity('d43f1ff7-ae36-4b1e-9af8-98a9cf027c22').run()
        