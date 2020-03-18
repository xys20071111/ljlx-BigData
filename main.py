import socketserver
class MsgHandler(socketserver.BaseRequestHandler):
    def Handler(self):
        data = self.request.recv(100000000000).decode('utf-8')
        print(data)
        self.request.sendall("OK")

socketserver.TCPServer(("127.0.0.1",5624),MsgHandler).serve_forever()
    
