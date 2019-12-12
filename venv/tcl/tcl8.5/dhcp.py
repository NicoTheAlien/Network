class dhcp():

    def __init__(self, name, ip, mac, ippc, macpc, gateway, maxpc):
        self.name = name
        self.ip = ip
        self.mac = mac
        self.ippc = ippc
        self.mpc = macpc
        self.gateway = gateway
        self.npc = maxpc

    def getipPC(self):
        return self.ippc

    def getmPC(self):
        return self.mpc

    def getgateway(self):
        return self.gateway

    def getname(self):
        return self.name
