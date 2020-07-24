from abc import ABC, abstractmethod, abstractproperty

class SegmentInterface(ABC):
    _segmentStart : int
    _segmentEnd : int
    _segmentSize : int
    _segmentName : str
    _segmentType: str
    _segmentVirtualAddress : int

    def __init__(self, segmentStart, segmentEnd, segmentType = 'CODE', segmentVirtualAddress = 0x0, segmentName = ""):
        self._segmentStart = segmentStart
        self._segmentEnd = segmentEnd
        self._segmentSize = segmentEnd - segmentStart
        self._segmentType = segmentType
        self._segmentName = segmentName
        self._segmentVirtualAddress = segmentVirtualAddress

    def getSegmentStart(self):
        return self._segmentStart

    def getSegmentEnd(self):
        return self._segmentEnd

    def getSegmentSize(self):
        return self._segmentSize

    def getSegmentType(self):
        return self._segmentType

    def getSegmentName(self):
        return self._segmentName

    def getSegmentVirtualAddress(self):
        return self._segmentVirtualAddress
    
    @abstractmethod
    def processCallback(self):
        pass
