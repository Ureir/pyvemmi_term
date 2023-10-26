# Classes for VEMMI Components
from . import constant as cst


class Component:

    CIN: int = 0
    kind: bytes = None
    dirty: bool = True

    attributes = {}

    def __init__(self, cin: int, kind: bytes, dirty: bool = True):
        self.CIN = cin
        self.kind = kind
        self.dirty = dirty


class MenuChoice(Component):    # Virtual Menu Choice
    NotAccessible: bool = False
    Text: str = ""
    LocActAct = []
    LocActVal = []


class BarMenuChoice(MenuChoice):    # Application Bar first level
    kind = cst.OPC_BAR_MENU_CHOICE
    pass


class PullDownMenuChoice(MenuChoice):
    kind = cst.OPC_PULL_DOWN_CHOICE
    Separated: bool = False


class CascadingMenuChoice(MenuChoice):
    kind = cst.OPC_CASC_MENU_CHOICE
    Separated: bool = False


class Button(Component):
    kind = cst.OPC_BUTTON
    Height: float = -1.0
    Width: float = -1.0
    Closed: bool = False
    NotAccessible: bool = False
    BIN: int = -1
    LabelFont: int = -1
    Text: str = ""
    LocActAct = []
    LocActVal = []


class PopUpMenuChoice(MenuChoice):
    kind = cst.OPC_POP_UP_CHOICE
    Separated: bool = False


class DialogComponent(Component):
    XPos: float = -1.0
    YPos: float = -1.0
    Height: float = -1.0
    Width: float = -1.0
    Closed: bool = False
    Colour: int = -1


class Separator(DialogComponent):
    kind = cst.OPC_SEPARATOR
    Vertical: bool = False


class Frame(DialogComponent):
    kind = cst.OPC_FRAME
    TextLabel: str = ""
    LabelFont: int = -1


class InTextStr:
    pass


class TextArea(DialogComponent):
    kind = cst.OPC_TEXT_AREA
    NoScrollingTools: bool = False
    NoFormat: bool = False
    MaximTxt: bool = False
    NoBorder: bool = False
    InitialFnt: int = -1
    InText: InTextStr = None
    TextCompRef: int = -1
    # No colour!


class TextCmp(Component):
    kind = cst.OPC_TEXT_COMPONENT
    PreviousText: int = -1
    CurrentText: InTextStr = None
    NextText: int = -1


class SensitiveText(Component):
    kind = cst.OPC_SENSITIVE_TEXT
    NotAccessible: bool = False
    LocActAct = []
    LocActVal = []


class GraphicOutputArea(DialogComponent):
    kind = cst.OPC_GRAPHIC_OUTPUT_AREA
    Maximizable: bool = False
    DispType: int = 0
    BIN: int = -1
    VIN: int = -1


class PushButton(DialogComponent):
    kind = cst.OPC_BOX_PUSH_BUTTON
    NotAccessible: bool = False
    BIN: int = -1
    LabelFont: int = -1
    Text: str = ""
    LocActAct = []
    LocActVal = []


class TextInput(DialogComponent):
    kind = cst.OPC_TEXT_INPUT_FIELD
    NotAccessible: bool = False
    MaximText: bool = False
    DefValue: str = ""
    TextLabel: str = ""
    LabelFont: int = -1
    InputType: int = 0
    InputFont: int = -1
    EchoType: int = 0
    EchoChar: str = '-'
    MaxChar: int = 80
    MaxLine: int = 1
    InputTransformation: int = 0
    LocActAct = []
    LocActVal = []


class CheckBox(DialogComponent):
    kind = cst.OPC_CHECK_BOX
    NotAccessible: bool = False
    TextLabel: str = ""
    LabelFont: int = -1
    DefMarked: bool = False
    LocActAct = []
    LocActVal = []


class RadioButton(DialogComponent):
    kind = cst.OPC_RADIO_BUTTON
    NotAccessible: bool = False
    TextLabel: str = ""
    LabelFont: int = -1
    Group: int = 1
    DefMarked: bool = False
    LocActAct = []
    LocActVal = []


class ListBoxItem:
    ListIndex: int = -1
    Text: str = ""
    TextFont: int = -1
    IconReference: int = -1
    ItemLocAct = []
    ItemLocVal = []


class ListBox(DialogComponent):
    kind = cst.OPC_LIST_BOX
    NotAccessible: bool = False
    DefItem: int = 1
    Sorted: bool = False
    MultipleChoice: bool = False
    Arrayed: bool = False
    ColumnWidth = []
    Alignment: int = 0
    ReportIndex: bool = False
    LocActAct = []
    LocActVal = []
    items: ListBoxItem = []


class ComboBox(DialogComponent):
    kind = cst.OPC_COMBO_BOX
    NotAccessible: bool = False
    DefItem: int = 1
    NoEdit: bool = False
    NoConsistency: bool = False
    MaxChar: int = 80
    NoDropDown: bool = False
    Sorted: bool = False
    LocActAct = []
    LocActVal = []
    items: ListBoxItem = []


class Slider(DialogComponent):
    kind = cst.OPC_SLIDER
    NotAccessible: bool = False
    MinValue: int = -1
    MaxValue: int = -1
    Increment: int = 1
    InitialValue: int = -1
    DirectIn: bool = False
    Vertical: bool = False
    LocActAct = []
    LocActVal = []


class SensitiveArea(DialogComponent):
    kind = cst.OPC_SENSITIVE_AREA
    NotAccessible: bool = False
    Locator: (float, float) = (-1.0, -1.0)
    AssGraphicReference: int = -1
    LocActAct = []
    LocActVal = []


class MultimediaArea(DialogComponent):
    kind = cst.OPC_MULTIMEDIA_AREA
    NotAccessible: bool = False
    Maximizable: bool = False
    NoBorder: bool = False
    MultimContentType: int = 0
    MultimediaContent: str = ""
    DirectNavigation: bool = False
    NonControlledMode: bool = False
