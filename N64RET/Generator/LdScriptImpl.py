import os
from N64RET.Loader.N64.N64RomImpl import N64Rom
from mako.template import Template

class LdScript(object):
    _romClass : N64Rom

    def __init__(self, romClass : N64Rom):
        self._romClass = romClass
    
    def writeScript(self, scriptPath : str, bssStart: int):
        rootPath = os.path.dirname(os.path.realpath(__file__))
        ldTemplate = Template(filename=rootPath + '/LdScriptTemplate.ld')
        
        f = open(scriptPath, "w+")
        f.write(ldTemplate.render(CODE_BSS_START=hex(bssStart).strip("L"), CODE_SEGMENT_START=hex(self._romClass._IPL3_SEGMENT_END).strip("L"), ENTRYPOINT_RELOCATED=hex(self._romClass.getEntrypointRelocated()).strip("L")))
        f.close()
