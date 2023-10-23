# Classes for VEMMI Components
import .protocol as p
import .constant as cst

class Attribute:

    name = None
    value = None
    dirty = False
    
    def __init__(self, name: bytes, value: object = None, dirty: bool = False)
        self.name = name
        self.value = value
        self.dirty = dirty
        
    def setval(self, value: object = None)
        """Update value only"""
        self.value = value
        
    def setdirty(self, flag: bool = True)
        """Update dirty flag only"""
        self.dirty = flag
        
    def encode(self) -> bytearray:
        """Encode attribute, typically for CreateObject or StoreObject""" 
        return bytearray(0)
        
    def modified(self) -> bytearray:
        """Encode attribute for ModifyObject"""
        if self.dirty:
            return self.encode
        else:
            return bytearray(0)

class BoolAttribute:
    def __init__(self, name: bytes, value: bool = False, dirty: bool = True)
        super().__init__(name, value, dirty)
        
    def encode(self) -> bytearray:
        if self.value:
            return bytearray(self.name)
        else:
            return bytearray(0)
            
    def modified(self) -> bytearray:
        if self.dirty:
            ret = bytearray(self.name)
            if !self.value:
                ret = ret.join(ret)
            return ret
        else:
            return bytearray(0)
            
class NDCAttribute:
    def __init__(self, name: bytes, value: float = 0.0, dirty: bool = True)
        super().__init__(name, value, dirty)
        
    def encode(self) -> bytearray:
        ret = bytearray(self.name)
        ret.join(p.EncodeNDC(self.value))
        return ret
            
    def modified(self) -> bytearray:
        if self.dirty:
            ret = bytearray(self.name)
            ret.join(p.EncodeNDC(self.value))
        else:
            ret = bytearray(0)
        return ret

class IntAttribute:
    def __init__(self, name: bytes, value: int = 0, dirty: bool = True)
        super().__init__(name, value, dirty)
        
    def encode(self) -> bytearray:
        if self.value != 0:
            ret = bytearray(self.name)
            ret.join(p.EncodeInteger(self.value))
        else:
            ret = bytearray(0)
        return ret
            
    def modified(self) -> bytearray:
        if self.dirty:
            ret = bytearray(self.name)
            ret.join(p.EncodeInteger(self.value))
        else:
            ret = bytearray(0)
        return ret

class StrAttribute:
    def __init__(self, name: bytes, value: str = "", dirty: bool = True)
        super().__init__(name, value, dirty)
        
    def encode(self) -> bytearray:
        if self.value != 0:
            ret = bytearray(self.name)
            ret.join(p.EncodeString(self.value))
        else:
            ret = bytearray(0)
        return ret
            
    def modified(self) -> bytearray:
        if self.dirty:
            ret = bytearray(self.name)
            ret.join(p.EncodeString(self.value))
        else:
            ret = bytearray(0)
        return ret

def parseNDC(params: bytes) -> (float, bytes):
    val = 0
    one = 1
    i = 0
    code = params[0]
    while code & 128 == 0:
        val = (val << 6) | (code & 63)
        one = one << 6
        i = i+1
        code = params[i]
    val = (val << 7) | (code & 127)
    one = one << 7
    i = i+1
    return (val/one, params[i:])

def parse_int(params: bytes) -> (int, bytes):
    val = 0
    i = 0
    code = params[0]
    while code & 128 == 0:
        val = (val << 6) | (code & 63)
        i = i+1
        code = params[i]
    val = (val << 7) | (code & 127)
    i = i+1
    return (val, params[i:])

def parse_str(params: bytes, coding: str) -> (str, bytes):
    val = ""
    end = params.find(cst.ST.encode(coding))           # try to find the string terminator
    if end >= 0:                        # if found
        val = params[:end].decode(encoding=coding, errors="replace")
    elif coding == "utf-16":
        end = params.find(b'\xFF\xFF')  # Alternate terminator in unicode mode
        if end >= 0:
            val = params[:end].decode(encoding=coding, errors="replace")
    return (val, params[end:])


def parse(params: bytes, out: dict) -> bytes:
    if out is None:
        out = {}
    opc = params[0]
    while opc > 0x60 and opc < 0xEF:
        match opc >> 4:
            case 6 | 7:         # Boolean attributes
                params = params[1:]
                val = True
                if params[0] == opc:
                    val = False
                    params = params[1:]
                out |= { opc: BoolAttribute(name=opc, value=val) }
                
            case 9 :            # NDC attributes    
                val, params = parseNDC(params[1:])
                out |= { opc: NDCAttribute(name=opc, value=val) }
                
            case 10|11|12|13:   # Integer attributes
                val, params = parseInteger(params[1:])
                out |= { opc: IntAttribute(name=opc, value=val) }
            
            case 14:            # String attributes
                val, params = parseInteger(params[1:])
                out |= { opc: StrAttribute(name=opc, value=val) }
        opc = params[0]        
    return params
