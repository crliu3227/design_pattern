class Server():
    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class InfoServer(Server):
    def __init__(self):
        self.content = ""

    def recv(self, info):
        self.content = info
        return "Recv OK !"

    def show(self):
        print("SHOW : %s" % self.content)

# info = {"addr": "10.190.68.1", "content": "something"}
# 服务器所接收的info内容如上所示，那么如果要给服务器设置一个白名单：
# 使得服务器只能接收含白名单地址的info，此时可以修改Server结构方法，
# 但这不符合软件设计原则中的单一职责原则，那么此时使用代理模式，是个不错的方法


class ServerProxy():
    pass


class InfoServerProxy(ServerProxy):
    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    def __init__(self, server):
        super(WhiteInfoServerProxy, self).__init__(server)
        self.white_addr = set()

    def add_white_addr(self, addr):
        self.white_addr.add(addr)

    def remove_white_addr(self, addr):
        self.white_addr.remove(addr)

    def clear_white_addr(self, addr):
        self.white_addr.clear()

    def recv(self, info):
        try:
            assert isinstance(info, dict)
        except:
            return "Info must be a dict!"
        else:
            addr = info.get("addr", None)
            if addr not in self.white_addr:
                return "Your address is not in the white list."
            return self.server.recv(info)


# 代理中有一个server字段，控制代理的服务器对象，infoServerProxy充当Server的直接接口代理，
# 而whiteInfoServerProxy直接继承了infoServerProxy对象，同时加入了white_list和对白名单的操作。
# 这样，在场景中通过对白名单代理的访问，就可以实现服务器的白名单访问了。


if __name__ == "__main__":
    info_struct = {"addr": "10.190.68.1", "content": "Hello World !"}
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)

    print(info_server_proxy.recv(info_struct))
    info_server.show()

    info_server_proxy.add_white_addr("10.190.68.1")
    print(info_server_proxy.recv(info_struct))
    info_server.show()
