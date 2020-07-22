import io
from abc import ABC, abstractmethod, abstractproperty

class AbstractRomInfo(ABC):
    _inputPath : str
    _inputHandle : io.IOBase
    _romContents : bytearray

    @abstractmethod
    def __init__(self, inputPath):
        pass

    @abstractmethod
    def romOpen(self, inputPath):
        pass

    @abstractmethod
    def romClose(self):
        pass
    
    @abstractmethod
    def getRomFilename(self):
        pass
