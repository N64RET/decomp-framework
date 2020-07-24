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

        # Iterate Segments
        for segment in self._romClass.getSegments():
            if segment.getSegmentType() is "INTERNAL_HEADER":
                configHandle.write('  - [0x' + self.formatValueHex(segment.getSegmentStart(), 8) + ', 0x' + self.formatValueHex(segment.getSegmentEnd(), 8) + ', "header", "Header"]\n')
            elif segment.getSegmentType() is "CODE":
                configHandle.write('  - [0x' + self.formatValueHex(segment.getSegmentStart(), 8) + ', 0x' + self.formatValueHex(segment.getSegmentEnd(), 8) + ', "asm", "' + segment.getSegmentName() + '", 0x' + self.formatValueHex(segment.getSegmentVirtualAddress(), 8) + ']\n')
            else:
                configHandle.write('  - [0x' + self.formatValueHex(segment.getSegmentStart(), 8) + ', 0x' + self.formatValueHex(segment.getSegmentEnd(), 8) + ', "bin", "' + segment.getSegmentName() + '"]\n')

        configHandle.close()
        return True
