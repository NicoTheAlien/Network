class Switch:

    def __init__(self, nombre, gateway):
        self.nombre = nombre
        self.gateway = gateway
        self.Dispositivos = []

    def anadirDipositivo(self, nuevoDisp):
        self.Dispositivos.append(nuevoDisp)

    def getgateway(self):
        return self.gateway

    def listadispositivos(self):
        return self.Dispositivos
