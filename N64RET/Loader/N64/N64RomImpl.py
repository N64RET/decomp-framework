from N64RET.Loader.RomImpl import RomImpl
from N64RET.Loader.N64.InternalHeaderStruct import InternalHeader
class N64Rom(RomImpl):
    _INTERNAL_HEADER_SIZE : int = 0x40
    _IPL3_SEGMENT_END : int = 0x1000
    _CODE_SEGMENT_STANDARD_SIZE : int = 0x100000

    def getIPL3Contents(self):
        return self.readAtOffset(self._INTERNAL_HEADER_SIZE, self._IPL3_SEGMENT_END - self._INTERNAL_HEADER_SIZE)

    def getCodeOffset(self):
        return self._IPL3_SEGMENT_END

    def getCodeSize(self):
        # TODO: Detect via CIC/IPL Variant, however the actual DMA Transfer will always be _CODE_SEGMENT_STANDARD_SIZE
        return self._CODE_SEGMENT_STANDARD_SIZE

    def getCodeContents(self):
        return self.readAtOffset(self.getCodeOffset(), self.getCodeSize())

    def getInternalHeader(self):
        # TODO: Cache header?
        headerData = self.readAtOffset(0, self._INTERNAL_HEADER_SIZE)
        return InternalHeader(headerData)
    
    def getEntrypoint(self):
        return self.getInternalHeader().Entrypoint

    def getEntrypointRelocated(self):
        # TODO: Implement via CIC/IPL Variant
        return self.getEntrypoint()
