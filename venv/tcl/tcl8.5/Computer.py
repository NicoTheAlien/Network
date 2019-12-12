from dhcp import dhcp


class Computer:
    def __init__(self, nombre, ip, mac, gateway, so, hddSpace):
        self.nombre = nombre
        self.ip = ip
        self.mac = mac
        self.gateway = gateway
        self.so = so
        self.hddSpace = hddSpace

    def getip(self):
        return self.ip

    def getnombre(self):
        return self.nombre

    def getmac(self):
        return self.mac

    def getgateway(self):
        return self.gateway

    def InstallSO(self):
        return self.so
