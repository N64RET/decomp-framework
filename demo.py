import os
import N64RET.Processor.MIPSR.Disassembler.DisasmImpl as DisasmImpl

from N64RET.Loader.N64.N64RomImpl import N64Rom
from N64RET.Generator.N64SplitConfigImpl import N64SplitConfig

def main():
    romClass = N64Rom("rom.z64")
    print(romClass.getRomFilename())
    print("RomOpen: " + str(romClass.romOpen()))

    headerBinary = romClass.readAtOffset(0, 0x40)
    print("Header repr: " + repr(headerBinary))
    print("Header Length: " + hex(len(headerBinary)))

    headerStruct = romClass.getInternalHeader()
    print("Header Struct repr: " + repr(headerStruct))
    
    ipl3Binary = romClass.getIPL3Contents()
    print("IPL3 repr: " + repr(ipl3Binary[:0x10]))
    print("IPL3 Length: " + hex(len(ipl3Binary)))

    codeBinary = romClass.getCodeContents()
    print("CODE repr: " + repr(codeBinary[:0x10]))
    print("CODE Length: " + hex(len(codeBinary)))

    entrypoint = romClass.getEntrypoint()
    print("Entrypoint: " + hex(entrypoint))
    entrypoint = romClass.getEntrypointRelocated()
    print("Entrypoint (Relocated): " + hex(entrypoint))

    n64splitConfig = N64SplitConfig(romClass)
    n64splitConfig.writeConfig("split.yaml")

    dis = DisasmImpl.Disassembler()
    dis.load_defaults()
    dis.set_auto_analysis(True)

    dis.files.append(dis.File("CODE", romClass.getCodeContents(), romClass.getEntrypointRelocated()))
    dis.files = sorted(dis.files, key = lambda file: file.vaddr)
    dis.reset_cache()
    dis.add_data_region(0x800969C0, 0x8017FFFC, "CODE")
    
    dis.first_pass()
    os.makedirs("disasm/", exist_ok=True)
    dis.second_pass("disasm/")
    #dis.disassemble(args.disassemble)

    print("RomClose: " + str(romClass.romClose()))

if __name__ == "__main__":
    main()
