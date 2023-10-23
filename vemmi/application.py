# vemmi.Application class
# Should be used by application for Application-side protocol management
import protocol
import constant as cst
import objects as obj

class Application:
    """
    Application Class
    
    Implements all Host-side commands and behaviour.
    """
    p = protocol.Protocol()
    
    objects = []

    def Open:
        """
        VEMMI_Open command.
        
        No parameters since only one version and only the standard "native" protocol is supported.
        """
        cmd = bytesarray(cst.OPC_OPEN)
        cmd.join(p.EncodeInteger(VEMMI_VERSION))
        cmd.join(cst.OPC_MODE)
        cmd.join(p.EncodeInteger(0))     # Native mode
        p.Send(cmd)
        for o in objects:                   # if any object is already managed
            o.loaded = false                # it is no longer loaded in terminal

    def Close:
        """
        VEMMI_Close command.
        
        No parameter since private parameters are not supported yet.
        """
        p.Send(bytesarray(cst.OPC_CLOSE))

    def OpenApplication:
        """
        VEMMI_Open command.
        
        No parameters since only one version and only the standard "native" protocol is supported.
        """
        cmd = bytesarray(constant.OPC_OPEN)
        cmd.join(p.EncodeInteger(VEMMI_VERSION))
        cmd.join(cst.OPC_MODE)
        cmd.join(p.EncodeInteger(0))     # Native mode
        p.Send(cmd)
        resp = p.Wait(cst.OPC_OPEN_APPL_RESP)
        return (resp==true)

    def __init__(name=""):
        pass

