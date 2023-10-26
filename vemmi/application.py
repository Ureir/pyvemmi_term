# vemmi.Application class
# Should be used by application for Application-side protocol management
from . import VEMMI_VERSION, protocol as p, constant as cst


class Application:
    """
    Application Class

    Implements all Host-side commands and behaviour.
    """
    objects = []

    def Open(self):
        """
        VEMMI_Open command.

        No parameters since only one version and only the standard "native" protocol is supported.
        """
        cmd = bytearray(cst.OPC_OPEN)
        cmd.join(p.EncodeInteger(VEMMI_VERSION))
        cmd.join(cst.OPC_MODE)
        cmd.join(p.EncodeInteger(0))     # Native mode
        p.Send(cmd)
        for o in self.objects:              # if any object is already managed
            o.loaded = False                # it is no longer loaded in terminal

    def Close(self):
        """
        VEMMI_Close command.

        No parameter since private parameters are not supported yet.
        """
        p.Send(bytearray(cst.OPC_CLOSE))

    def OpenApplication(self):
        """
        VEMMI_Open command.

        No parameters since only one version and only the standard "native" protocol is supported.
        """
        cmd = bytearray(cst.OPC_OPEN)
        cmd.join(p.EncodeInteger(VEMMI_VERSION))
        cmd.join(cst.OPC_MODE)
        cmd.join(p.EncodeInteger(0))     # Native mode
        p.Send(cmd)
        resp = p.Wait(cst.OPC_OPEN_APPL_RESP)
        return (resp is True)

    def __init__(self, name=""):
        pass
