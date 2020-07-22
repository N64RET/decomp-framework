from N64RET.Loader.N64Rom import N64Rom

def main():
    romClass = N64Rom("rom.z64")
    print(romClass.getRomFilename())
    print("RomOpen: " + str(romClass.romOpen()))
    print("RomClose: " + str(romClass.romClose()))

if __name__ == "__main__":
    main()
