import os
from N64RET.Loader.Abstract.RomInterface import RomInterface

class RomImpl(RomInterface):
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

    def getRomFilesize(self):
        if self._inputPath:
            return os.path.getsize(self._inputPath)
        else:
            return 0x0

    def getContents(self):
        if not self._inputHandle:
            print("[RomInfo.getContents]: File not open")
        
        currentOffset = self._inputHandle.tell()
        
        self._inputHandle.seek(0)
        inputContents = self._inputHandle.read()
        self._inputHandle.seek(currentOffset)

        return inputContents

    def readAtOffset(self, offset : int, length : int):
        if not self._inputHandle:
            print("[RomInfo.readAtOffset]: File not open")
        
        self._inputHandle.seek(offset)
        inputContents = self._inputHandle.read(length)

        return inputContents

