SECTIONS
{
    /* Objects with .gptab.* sections error if they are not referenced, for some reason */
    /DISCARD/ : { *(.gptab.data) }
    /DISCARD/ : { *(.gptab.bss) }

    RomLocation = 0x0;
    . = 0xA4000000;
    INTERNAL_HEADER : AT(RomLocation)
    {
        INTERNAL_HEADER_start = .;
        build/src/INTERNAL_HEADER_0xA4000000.o(.text)
        INTERNAL_HEADER_end = .;
    }

    RomLocation = 0x40;
    . = 0xA4000040;
    IPL3 : AT(RomLocation)
    {
        IPL3_text_start = .;
        build/src/IPL3_0xA4000040.o(.text)
        IPL3_text_end = .;
    }

    RomLocation = ${CODE_SEGMENT_START};
    . = ${ENTRYPOINT_RELOCATED};
    SegmentStart = .;
    CODE : AT(RomLocation)
    {
        CODE_text_start = .;
        %for objectFile in CODE_OBJECT_DEFINITIONS:
        ${objectFile}
        %endfor
        CODE_text_end = .;
    }
    SegmentEnd = .;
    SegmentSize = SegmentEnd - SegmentStart;
    RomLocation += SegmentSize;

    CODE_bss_start = ${CODE_BSS_START};
    
    /DISCARD/ : { *(.reginfo) *(.MIPS.abiflags) }
    
    GAP_BIN : AT(RomLocation)
    {
        GAP_BIN_start = .;
        build/src/GAP.o(.text)
        GAP_BIN_end = .;
    }
}
