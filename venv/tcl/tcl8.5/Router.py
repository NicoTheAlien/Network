class router():
    def __init__(self, newGateWay):
        self.ListRouter = []
        self.Gateway = newGateWay

    def getListRouter(self):
        return self.ListRouter

    def anadirListRouter(self):
        return self.ListoRouter

    def anadirDispAlRouter(self, newDisp):
        self.ListRouter.append(newDisp)