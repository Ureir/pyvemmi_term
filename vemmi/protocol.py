# Protocol class
# This is the low-level VEMMI protocol.
# It is not supposed to be called directly, but only through Application or Terminal class.
from . import constant as cst
from sys import stdout


max_mtu: int = 1024
initialized: int = 0

# §9 Encoding
# §9.3 Terminal symbols encoding
# §9.3.1 Opcode
# Opcodes are encoded as byte literal constants OPC_*


# §9.3.2 Integers
def EncodeInteger(value: int) -> bytearray:
    if value < 0:
        value = 0
    ret = bytearray(1)
    ret[0] = 128 | (value & 127)            # Last byte
    value = value >> 7
    while (value != 0):
        ret.rjust(len(ret)+1, b'\0')        # pre-pend byte
        ret[0] = 64 | (value & 63)          # update byte value
        value = value >> 6                  # consume bits
    return ret                              # return byte array


# §9.3.3 Enumerated
# Enumerated are coded as integers

# §9.3.4 Strings
def EncodeString(value: str, encoding: int = cst.ENC_ISO_8859_1) -> bytearray:
    return bytearray(value + cst.LATIN_ST, cst.PY_ENCODING[encoding])


# §9.3.5 NDC
def EncodeNDC(value: float) -> bytearray:
    cnt = 0
    if value >= 0.999998:
        value = 0.999998
    if value <= 0.0:
        value = 0.0
    ret = bytearray(0)      # return value, start as an empty bytearray
    byte = bytearray(1)     # current byte
    while value > 0.000002 and cnt < 2:
        value = value * 64
        byte[0] = 64 | int(value)
        ret.join(byte)
        value = value - int(value)
        cnt = cnt + 1
    if value >= 0.9921875:  # (1.0-1/128)
        byte[0] = 255
    else:
        byte[0] = 128 | int(value*128)
    ret.join(byte)
    return ret                              # return byte array


def EncodeCommand():
    pass


false: bytes = b'\x80'    # <INTEGER: 0> coded by byte value 128
true: bytes = b'\x81'    # <INTEGER: 1> coded by byte value 129


def InitHost():
    stdout.buffer.write(b'\x1B\x25\x41')   # enter Data Syntax III


def EncodeLI(value: int) -> bytearray:
    """Encode the LI value of a VEMMI PCE"""
    ret = bytearray(0)    # empty bytearray
    while value >= 32:      # encode in reverse order
        ret.ralign(len(ret)+1)
        ret[0] = 96 | (value & 31)
        value = value >> 5
    ret.ralign(len(ret)+2)
    ret[1] = 64 | value
    ret[0] = b'\x7F'                # First LI byte is always 0x7F
    return ret


def Send(cmd: bytearray):
    """
    Send a command as a Picture Entity
    """
    vemmi = bytearray(b'\x1B\x70\x25\x40')  # VEMMI Header: PCD CMI(PM PI)
    li = len(cmd)+1                         # computes length (+1 is for MDI byte)
    vemmi.join(EncodeLI(li))                # add LI encoding for length
    vemmi.join(cst.MDI_LAST)                # PDE start with MDI
    stdout.buffer.write(vemmi)
    stdout.buffer.write(cmd)


def Wait(opc: bytes) -> bytearray:
    pass
