from N64RET.Loader.N64.N64RomImpl import N64Rom

def main():
    romClass = N64Rom("rom.z64")
    print(romClass.getRomFilename())
    print("RomOpen: " + str(romClass.romOpen()))

    headerBinary = romClass.readAtOffset(0, 0x40)
    print("Header repr: " + repr(headerBinary))
    print("Header Length: " + hex(len(headerBinary)))

    ipl3Binary = romClass.getIPL3Contents()
    print("IPL3 repr: " + repr(ipl3Binary[:0x10]))
    print("IPL3 Length: " + hex(len(ipl3Binary)))

    codeBinary = romClass.getCodeContents()
    print("CODE repr: " + repr(codeBinary[:0x10]))
    print("CODE Length: " + hex(len(codeBinary)))

    entrypoint = romClass.getEntrypoint()
    print("Entrypoint: " + hex(entrypoint))
    print("RomClose: " + str(romClass.romClose()))

if __name__ == "__main__":
    main()
