import os
from mako.template import Template
from N64RET.Loader.N64.N64RomImpl import N64Rom
import N64RET.Processor.MIPSR.Disassembler.DisasmImpl as DisasmImpl

class LdScript(object):
    _romClass : N64Rom

    def __init__(self, romClass : N64Rom):
        self._romClass = romClass
    
    def writeScript(self, scriptPath : str, dis : DisasmImpl.Disassembler, bssStart: int):
        rootPath = os.path.dirname(os.path.realpath(__file__))
        ldTemplate = Template(filename=rootPath + '/LdScriptTemplate.ld')
        
        codeObjectList = []
        detectedObjects = dis.objects
        for addr in detectedObjects:
            codeObjectList.append('build/src/%s_0x%08X.o(.text)' % ("CODE", addr))
        codeObjectList = sorted(codeObjectList, key = lambda entry: entry)
        f = open(scriptPath, "w+")
        f.write(ldTemplate.render(CODE_OBJECT_DEFINITIONS=codeObjectList, CODE_BSS_START=hex(bssStart).strip("L"), CODE_SEGMENT_START=hex(self._romClass._IPL3_SEGMENT_END).strip("L"), ENTRYPOINT_RELOCATED=hex(self._romClass.getEntrypointRelocated()).strip("L")))
        f.close()
