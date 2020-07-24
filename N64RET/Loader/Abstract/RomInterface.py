import io
import array
from abc import ABC, abstractmethod, abstractproperty
from N64RET.Loader.SegmentImpl import Segment

class RomInterface(ABC):
    _inputPath : str
    _inputHandle : io.IOBase
    _segments : array.array = []

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

    @abstractmethod
    def getRomFilesize(self):
        pass

    @abstractmethod
    def getContents(self):
        pass
    
    @abstractmethod
    def readAtOffset(self, offset : int, length : int):
        pass

    def addSegment(self, segmentStart : int, segmentEnd : int, segmentType : str = "CODE", segmentVirtualAddress = 0x0, segmentName : str = ""):
        self._segments.append(Segment(segmentStart, segmentEnd, segmentType, segmentVirtualAddress, segmentName))
    
    def getSegment(self, segmentStart : int):
        for segment in self._segments:
            if segment.getSegmentStart() is segmentStart:
                return segment

    def removeSegment(self, segmentStart : int):
        for segment in self._segments:
            if segment.getSegmentStart() is segmentStart:
                self._segments.remove(segment)
                break
    
    def getSegments(self):
        return self._segments
