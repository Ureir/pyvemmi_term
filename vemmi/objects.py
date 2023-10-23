# Classes for VEMMI Objects
from . import component as cmp
from . import constant as cst

class VEMMI_Object:
    kind  : bytes = None
    dirty : bool = True
    local : None            # local gui instance object, for terminals

    attributes = {}
    components = {}



class ApplicationBar(VEMMI_Object):
    kind = cst.OPC_APPLICATION_BAR
    YPos: float = -1.0
    Closed: bool = False
    NotAccessible: bool = False
    DefActive: int = -1
    Vertical: bool = False


class ButtonBar(VEMMI_Object):
    kind = cst.OPC_BUTTON_BAR
    XPos: float = -1.0
    YPos: float = -1.0
    Vertical: bool = False
    FirstActive: int = -1
    Modal: bool = False
    Closed: bool = False
    NotAccessible: bool = False
    Title: str = ""

class PopUpMenu(VEMMI_Object):
    kind = cst.OPC_POP_UP_MENU
    XPos: float = -1.0
    YPos: float = -1.0
    Title: str = ""
    TitleFont: int = -1
    FirstActive: int = -1
    Modal: bool = False
    Closed: bool = False
    NotAccessible: bool = False

class DialogueBox(VEMMI_Object):
    kind = cst.OPC_DIALOG_BOX
    XPos: float = -1.0
    YPos: float = -1.0
    Width: float = -1.0
    Height: float = -1.0
    NoBorder: bool = False
    Title: str = ""
    FirstActive: int = -1
    Modal: bool = False
    Closed: bool = False
    NotAccessible: bool = False
    Maximizable: bool = False
    Colour: int = -1
    BIN: int = -1
    DispType: int = -1

class MessageBox(VEMMI_Object):
    kind = cst.OPC_MESSAGE_BOX
    XPos: float = -1.0
    YPos: float = -1.0
    Width: float = -1.0
    Height: float = -1.0
    Closed: bool = False
    MessageType: int = 0
    Modal: bool = False
    Title: str = ""
    NoBorder: bool = False
    AttributedText: InTextAttribute = None
    MaxTime: int = 0
    DestroyEvent: int = 0
    NoSound: bool = False

class Operative(VEMMI_Object):
    kind = cst.OPC_OPERATIVE_OBJECT
    Closed: bool = False
    ProgName: str = ""
    ProgFilename: str = ""
    ProgDescr: str = ""
    ProgAbout: str = ""
    ProgPar: str = ""
    ProgType: int = 0
    DefaultDirectory: str = ""

class Bitmap(VEMMI_Object):
    kind = cst.OPC_BITMAP_OBJECT

class DirectBitmap(Bitmap):
    BmWidth: int = -1
    BmHeight: int = -1
    BmCompr: int = 0

class DirectBitmapIndexed(DirectBitmap):
    BmBitsPerPixel: int = 1
    BmClrEntry: int = 0
    BmClrIxList: int = []

class DirectBitmapColour(DirectBitmap):
    BmBitsPerComp: int = 8
    BmClrCompList: int = []

class FileBitmap(Bitmap):
    Filename: str = ""
    PictFileType: int = 0

class Videotex(VEMMI_Object):
    kind = cst.OPC_VIDEOTEX_OBJECT
    VTX: bytearray = bytearray(0)
    Filename: str = ""

class Text(VEMMI_Object):
    kind = cst.OPC_TEXT_OBJECT
    Text: str = ""
    Filename: str = ""

class Font(VEMMI_Object):
    kind = cst.OPC_FONT_OBJECT
    FnFamily: int = 0
    FnHeight: int = 10
    FnBold: bool = False
    FnUnderline: bool = False
    FnItalic: bool = False
    FnColour: int = 0

class Metacode(VEMMI_Object):
    kind = cst.OPC_METACODE_OBJECT
    VEMMICommands = []

class Sound(VEMMI_Object):
    kind = cst.OPC_SOUND_OBJECT
    Closed: bool = False
    Filename: str = ""
    SoundForm: int = 0

class Video(VEMMI_Object):
    kind = cst.OPC_VIDEO_OBJECT
    Closed: bool = False
    VideoForm: int = 0
    Filename: str = ""
    
class Multimedia(VEMMI_Object):
    kind = cst.OPC_MULTIMEDIA_OBJECT
    Filename: str = ""

    