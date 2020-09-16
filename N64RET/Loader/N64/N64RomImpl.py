import zlib
from N64RET.Loader.RomImpl import RomImpl
from N64RET.Loader.N64.InternalHeaderStruct import InternalHeader

class N64Rom(RomImpl):
    _CRC_TO_CIC_TABLE = {
        0x6170A4A1: {"NTSC-Name": "6101", "PAL-Name": "7102", "Offset": 0x000000},
        0x90BB6CB5: {"NTSC-Name": "6102", "PAL-Name": "7101", "Offset": 0x000000},
        0x0B050EE0: {"NTSC-Name": "6103", "PAL-Name": "7103", "Offset": 0x100000},
        0x98BC2C86: {"NTSC-Name": "6105", "PAL-Name": "7105", "Offset": 0x000000},
        0xACC8580A: {"NTSC-Name": "6106", "PAL-Name": "7106", "Offset": 0x200000},
        0x00000000: {"NTSC-Name": "Unknown", "PAL-Name": "Unknown", "Offset": 0x0000000}
    }
    
    _INTERNAL_HEADER_SIZE : int = 0x40
    _IPL3_SEGMENT_END : int = 0x1000
    _CODE_SEGMENT_STANDARD_SIZE : int = 0x100000

    def romOpen(self, inputPath = ""):
        returnValue = super().romOpen(inputPath)
        
        # Setup Base segments
        self.addSegment(0, self._INTERNAL_HEADER_SIZE, "INTERNAL_HEADER", 0x0, "HEADER")
        self.addSegment(self._INTERNAL_HEADER_SIZE, self._IPL3_SEGMENT_END, "CODE", 0xA4000040, "IPL3")
        self.addSegment(self.getCodeOffset(), self.getCodeOffset() + self.getCodeSize(), "CODE", self.getEntrypointRelocated(), "CODE")
        self.addSegment(self.getCodeOffset() + self.getCodeSize(), self.getRomFilesize(), "DATA", 0x0, "ROM_GAP")
        
        return returnValue

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
        CIC = self.getCIC()
        return self.getEntrypoint() - CIC["Offset"]

    def getCIC(self):
        CRC = zlib.crc32(self.getIPL3Contents())
        if CRC in self._CRC_TO_CIC_TABLE:
            return self._CRC_TO_CIC_TABLE[CRC]
        else:
            return self._CRC_TO_CIC_TABLE[0]
