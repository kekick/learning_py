class Server:
    SERVER_IP = 1

    def __init__(self):
        self.ip = Server.SERVER_IP
        Server.SERVER_IP += 1
        self.router = None
        self.buffer = []

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
            self.router.servers.update()

    def get_data(self):
        data = self.buffer
        self.buffer = []
        return data

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        server.router = self
        self.servers.update({server.ip: server})

    def unlink(self, server):
        server.router = None
        self.servers.pop(server.ip)

    def send_data(self):
        for i in self.buffer:
            if i.ip in self.servers:
                self.servers[i.ip].buffer.append(i)
        self.buffer = []


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
print(tuple(i.data for i in router.buffer))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
print(tuple(i.data for i in router.buffer))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.buffer
msg_lst_to = sv_to.buffer

print(msg_lst_from[0].data, msg_lst_to[0].data)
router.unlink(sv_to)