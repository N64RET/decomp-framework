from N64RET.Loader.RomInfo import RomInfo

class N64Rom(RomInfo):
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
