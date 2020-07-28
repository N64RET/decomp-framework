import os
import N64RET.Processor.MIPSR.Disassembler.DisasmImpl as DisasmImpl

from N64RET.Loader.N64.N64RomImpl import N64Rom
from N64RET.Generator.N64SplitConfigImpl import N64SplitConfig
from N64RET.Generator.LdScriptImpl import LdScript

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

    #n64splitConfig = N64SplitConfig(romClass)
    #n64splitConfig.writeConfig("split.yaml")

    dis = DisasmImpl.Disassembler()
    dis.load_defaults()
    dis.set_auto_analysis(True)

    f = open("code_original.bin", "wb+")
    f.write(romClass.getCodeContents())
    f.close()

    dis.files.append(dis.File("INTERNAL_HEADER", romClass.readAtOffset(0, romClass._INTERNAL_HEADER_SIZE), 0xA4000000))
    #dis.add_data_region(0xA4000000, 0xA400003F, "INTERNAL_HEADER")

    ipl3Binary = romClass.getIPL3Contents()
    dis.files.append(dis.File("IPL3", ipl3Binary, 0xA4000040))
    #dis.add_data_region(0xA4000B70, 0xA4000040 + len(ipl3Binary), "IPL3")

    dis.files.append(dis.File("CODE", romClass.getCodeContents(), romClass.getEntrypointRelocated()))
    dis.files = sorted(dis.files, key = lambda file: file.vaddr)
    dis.reset_cache()

    #dis.add_data_region(0x800731A0, 0x80125D18, "CODE")
    #dis.add_bss_region(0x8009A5B0, 0x8009A5B0 + 0x41F50, "CODE")
    
    dis.first_pass()
    os.makedirs("src/", exist_ok=True)
    os.makedirs("build/src/", exist_ok=True)
    dis.second_pass("src/")
    dis.generate_undefined("src/")
    dis.generate_headers("src/")

    f = open("src/GAP.bin", "wb+")
    f.write(romClass.readAtOffset(romClass.getCodeOffset() + romClass.getCodeSize(), romClass.getRomFilesize() - romClass.getCodeOffset() - romClass.getCodeSize()))
    f.close()

    #ldScript = LdScript(romClass)
    #ldScript.writeScript("src/linker_script.ld", 0x8009A5B0)

    print("RomClose: " + str(romClass.romClose()))

if __name__ == "__main__":
    main()
