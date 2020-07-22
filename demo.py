from N64RET.Loader.N64Rom import N64Rom

def main():
    romClass = N64Rom("rom.z64")
    print(romClass.getRomFilename())
    print("RomOpen: " + str(romClass.romOpen()))

    headerBinary = romClass.readAtOffset(0, 0x40)
    print("Header repr: " + repr(headerBinary))
    print("Header Length: " + hex(len(headerBinary)))

    print("RomClose: " + str(romClass.romClose()))

if __name__ == "__main__":
    main()
