class Server:
    lst_servers = []

    def __new__(cls, *args, **kwargs):
        cls.lst_servers.append(super().__new__(cls))
        return super().__new__(cls)

    def __init__(self):
        self.router = None
        self.buffer = []
        self.ip = len(self.lst_servers)

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):

        s = self.buffer[:]
        self.buffer.clear()
        return s

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.all_server = {}
        self.buffer = []

    def link(self, server):
        self.all_server[id(server)] = server
        server.router = self

    def unlink(self, server):
        serv = self.all_server.pop(server.ip, False)
        if serv:
            serv.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.all_server:
                self.all_server[data.ip].buffer.append(data)
        self.buffer.clear()


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

