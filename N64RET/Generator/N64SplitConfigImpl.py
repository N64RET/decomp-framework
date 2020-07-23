import os
from N64RET.Loader.N64.N64RomImpl import N64Rom

class N64SplitConfig(object):
    _romClass : N64Rom

    def __init__(self, romClass : N64Rom):
        self._romClass = romClass
    
    def formatValueHex(self, number : int, zfill : int = 8):
        return hex(number).strip("L")[2:].zfill(zfill)
    
    def writeConfig(self, configPath : str):
        configHandle = open(configPath, "w+")
        if not configHandle:
            print("[N64SplitConfig.writeConfig] Can't open file " + configPath + " for writing!")
            return False
        
        configHandle.write('name: "' + str(self._romClass.getInternalHeader().InternalName).strip(' "')[2:] + '"\n')
        configHandle.write("checksum1: " + hex(self._romClass.getInternalHeader().CRC1).strip("L") + "\n")
        configHandle.write("checksum2: " + hex(self._romClass.getInternalHeader().CRC2).strip("L") + "\n")
        configHandle.write('basename: "' + self._romClass.getRomFilename()[:-4] + '"\n')
        configHandle.write('ranges:\n')
        configHandle.write('  # start,       end,        type,     label\n')

        # Basic pre-defined segments
        # TODO: Segment API Iteration
        configHandle.write('  - [0x00000000, 0x' + self.formatValueHex(self._romClass._INTERNAL_HEADER_SIZE, 8) + ', "header", "header"]\n')
        configHandle.write('  - [0x' + self.formatValueHex(self._romClass._INTERNAL_HEADER_SIZE) + ', 0x' + self.formatValueHex(self._romClass._IPL3_SEGMENT_END) + ', "asm",    "IPL3", 0xA4000040]\n')
        configHandle.write('  - [0x' + self.formatValueHex(self._romClass.getCodeOffset()) + ', 0x' + self.formatValueHex(self._romClass.getCodeOffset() + self._romClass.getCodeSize()) + ', "asm",    "CODE", 0x' + self.formatValueHex(self._romClass.getEntrypointRelocated()) + ']\n')
        configHandle.write('  - [0x' + self.formatValueHex(self._romClass.getCodeOffset() + self._romClass.getCodeSize()) + ', 0x' + self.formatValueHex(os.path.getsize(self._romClass.getRomFilename())) + ', "bin",    "bin_' + self.formatValueHex(self._romClass.getCodeOffset() + self._romClass.getCodeSize(), 6) + '"]\n')
        