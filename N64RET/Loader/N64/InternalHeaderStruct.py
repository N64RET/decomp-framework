import cstruct
from N64RET.CTypes.StandardTypesTypedefs import defineStandardCTypes

# Setup Standard types
defineStandardCTypes()

class InternalHeader(cstruct.CStruct):
    __byte_order__ = cstruct.BIG_ENDIAN
    __struct__ = """
        /* 0x00 */ u32 BSD_DOM1_CONFIG;
        /* 0x04 */ u32 ClockrateOverride;
        /* 0x08 */ u32 Entrypoint;
        /* 0x0C */ u32 ReturnAddress;
        /* 0x10 */ u32 CRC1;
        /* 0x14 */ u32 CRC2;
        /* 0x18 */ u32 unkReserved0[2];
        /* 0x20 */ char InternalName[20];
        /* 0x34 */ u32 unkReserved1;
        /* 0x38 */ u32 MediaFormat;
        /* 0x3C */ u16 CartridgeId;
        /* 0x3E */ u8 CountryCode;
        /* 0x3F */ u8 Version;
    """
