class SO():
    def __init__(self, name, version, architecture, onlyCommands, caseSensitive, spaceRequirement):
        self.name = name
        self.version = version
        self.architecture = architecture
        self.onlyCommands = onlyCommands
        self.caseSensitive = caseSensitive
        self.spaceRequirement = spaceRequirement

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getVersion(self):
        return self.version
    def setVersion(self, version):
        self.version = version
    def getArchitecture(self):
        return self.architecture
    def setArchitecture(self, architecture):
        self.architecture = architecture
    def getOnlyCommands(self):
        return self.onlyCommands
    def setOnlyCommands(self, onlyCommands):
        self.onlyCommands = onlyCommands
    def getCaseSensitive(self):
        return self.caseSensitive
    def setCaseSensitive(self, caseSensitive):
        self.caseSensitive = caseSensitive
    def getSpaceRequirement(self):
        return self.spaceRequirement
    def setSpaceRequirement(self, spaceRequirement):
        self.spaceRequirement = spaceRequirement