from N64RET.Loader.Abstract.AbstractRomInfo import AbstractRomInfo

class RomInfo(AbstractRomInfo):
    def __init__(self, inputPath = ""):
        self._inputPath = inputPath

    def romOpen(self, inputPath = ""):
        if inputPath is "" and self.getRomFilename() is "":
            print("[RomInfo.romOpen]: Missing inputPath")
            return False
        
        if self.getRomFilename() is "" and inputPath is not "":
            self._inputPath = inputPath
        
        self._inputHandle = open(self.getRomFilename(), "rb")
        if not self._inputHandle:
            print("[RomInfo.romOpen]: Can't open " + self._inputPath)
            return False
        
        return True

    def romClose(self):
        if self._inputHandle:
            self._inputHandle.close()
            self._inputHandle = None
            return True
        else:
            print("[RomInfo.romClose]: File not open")
            return False
    
    def getRomFilename(self):
        return self._inputPath
