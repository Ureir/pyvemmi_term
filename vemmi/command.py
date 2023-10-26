# VEMMI Commands
from . import constant as cst
from . import objects as o
from . import protocol as p


class Command:
    opc: bytes

    def encode(self) -> bytearray:
        return bytearray(self.opc)


class Open(Command):
    opc = cst.OPC_OPEN


class Close(Command):
    opc = cst.OPC_CLOSE


class Resume(Command):
    opc = cst.OPC_RESUME


class Suspend(Command):
    opc = cst.OPC_SUSPEND


class Close_All(Command):
    opc = cst.OPC_CLOSE_ALL


class Identify_Term_Cap(Command):
    opc = cst.OPC_TERM_CAP_REQUEST
    caps = []

    def __init__(self, caps: bytes):
        self.caps = caps

    def encode(self) -> bytearray:
        ret = bytearray(self.opc)
        for cap in self.caps:
            ret.join(bytes(cap))
        return ret


class Set_Options(Command):
    text_standard: int = cst.TT_ISO_8859_1

    def __init__(self, std: int):
        self.opc = cst.OPC_SET_OPTIONS
        self.text_standard = std

    def encode(self) -> bytearray:
        ret = super().encode()
        ret.join(cst.OPC_TEXT_TYPE)
        ret.join(p.EncodeInteger(self.text_standard))
        return ret


class Create_Object(Command):
    oin: int
    template: bool
    autostore: bool
    obj: o.VEMMI_Object

    def __init__(self, oin: int, obj: o.VEMMI_Object, template: bool = False, autostore: bool = False):
        self.opc = cst.OPC_CREATE_OBJECT
        self.oin = oin
        self.template = template
        self.autostore = autostore
        self.obj = obj

    def encode(self) -> bytearray:
        ret = super().encode()
        ret.join(p.EncodeInteger(self.oin))
        if self.template:
            ret.join(cst.OPC_TEMPLATE)
        elif self.autostore:
            ret.join(cst.OPC_AUTOSTORE)
        ret.join(self.obj.encode())
        return ret
