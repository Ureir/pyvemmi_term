# A module for constants definitions

# String terminator
ST = "\x9C"


# §8.4 VEMMI Command Syntax

# File transfer information
FTI_UNKNOWN = 0
FTI_X_MODEM = 1
FTI_Y_MODEM = 2
FTI_Z_MODEM = 3
FTI_KERMIT = 4
FTI_ISDN_EUROFILE = 5     # ETS 300 383
FTI_ISDN_FTAM = 6     # ETS 300 388
FTI_PDFT = 7     # ETS 300 075

# Text type
TT_T51 = 0
TT_T52 = 1
TT_ISO_8859_1 = 2
TT_UNICODE = 3              # UTF-16
TT_SJIS = 4
TT_ISO_8859_2 = 5
TT_ISO_8859_3 = 6
TT_ISO_8859_4 = 7
TT_ISO_8859_5 = 8
TT_ISO_8859_6 = 9
TT_ISO_8859_7 = 10
TT_ISO_8859_8 = 11
TT_ISO_8859_9 = 12
TT_ISO_8859_10 = 13
TT_UTF_8 = 14               # Not in standard!

# Encodings, for python
PY_ENCODING = {
    # T51 and T52 are not supported by python

    # ISO encoding
    TT_ISO_8859_1:  "iso8859-1",
    TT_ISO_8859_2:  "iso8859-2",
    TT_ISO_8859_3:  "iso8859-3",
    TT_ISO_8859_4:  "iso8859-4",
    TT_ISO_8859_5:  "iso8859-5",
    TT_ISO_8859_6:  "iso8859-6",
    TT_ISO_8859_7:  "iso8859-7",
    TT_ISO_8859_8:  "iso8859-8",
    TT_ISO_8859_9:  "iso8859-9",
    TT_ISO_8859_10: "iso8859-10",

    # Shifted-JIS
    TT_SJIS:        "shift_jis",

    # Unicode encoding
    TT_UNICODE: "utf_16_be",
    TT_UTF_8:   "utf_8"
 }

# Still picture
PIC_T101_F = 0     # T.101 Annex F = ETS 300 177, Photographic syntax, Videotex
PIC_JPEG = 1     # JPEG (ISO/IEC 10918)
PIC_VEMMI_DIB = 2     # VEMMI DIB
PIC_GIF = 3     # GIF
PIC_MS_DIB = 4     # MS DIB

# Graphic
GRAPH_VIDEOTEX = 0     # ETS 300 073 (Geometric Display, Videotex)
GRAPH_CGM = 1     # CGM

# Audio type
AUDIO_VIDEOTEX = 0     # ETS 300 149 (Audio syntax, Videotex)
AUDIO_WAVE = 1     # WAVE
AUDIO_MIDI = 2     # MIDI

# Audio visual
VIDEO_MPEG1S = 0     # MPEG1 System (ISO 11172-1, Audio and Video supported)
VIDEO_MPEG1V = 1     # MPEG1 Video  (ISO 11172-2, Video only)
VIDEO_MPEG2S = 2     # MPEG2 System (ISO 13818-1, Audio and Video supported)
VIDEO_MPEG2V = 3     # MPEG2 Video  (ISO 13818-2, Video only)
VIDEO_H261 = 4     # H.261 (video codec for AV services)
VIDEO_H320 = 5     # H.320 (videophone)
VIDEO_AVI = 6     # AVI
VIDEO_QUICKTIME = 7     # Quicktime

# Data syntax type
DATA_T101B = 0         # T.101 Annex B
DATA_T101C1 = 1         # T.101 Annex C, Profile 1
DATA_T101C2 = 2         # T.101 Annex C, Profile 2
DATA_T101C3 = 3         # T.101 Annex C, Profile 3
DATA_T101C4 = 4         # T.101 Annex C, Profile 4
DATA_T101C5 = 5         # T.101 Annex C, Profile 5
DATA_T101D = 6         # T.101 Annex D

# Multimedia type
HTML = 0             # HTML
HTML_1 = 1             # HTML 1
HTML_2 = 2             # HTML 2
HTML_3 = 3             # HTML 3
# Extension:
HTML_4 = 4             # HTML 4
HTML_5 = 5             # HTML 5

# Trigger
TRIGGER_ACTIVATION = 0     # activation of a component
TRIGGER_VALIDATION = 1     # validation of a component

# Component data
CPN_REPORT_CIN = 0     # cin report
CPN_REPORT_TEXT = 1     # text report
CPN_REPORT_LIST_STR = 2     # list string report
CPN_REPORT_BOOLEAN = 3     # boolean report
CPN_REPORT_SLIDER = 4     # slider report
CPN_REPORT_LOCATOR = 5     # locator report
CPN_REPORT_LIST_IDX = 6     # list index report

# Error type
ERROR_GENERAL = 0     # general error
ERROR_UNKNOWN_CMD = 1     # unknown command
ERROR_ERRONEOUS_CMD = 2     # erroneous command
ERROR_OBJ_SYNTAX = 3     # object syntax error
ERROR_UNEXP_CMD = 4     # unexpected command
ERROR_MEMORY = 5     # out of memory
ERROR_AUDIO = 6     # cannot process audio objects
ERROR_VIDEO = 7     # cannot process video objects
ERROR_COLOUR_IDX = 8     # invalid colour index
ERROR_FILE = 9     # file not found
ERROR_BITMAP = 10    # conversion to bitmap failed
ERROR_COLOUR_DEF = 11    # cannot process direct colour definition
ERROR_OPERATIVE = 12    # operative object was rejected by the user
ERROR_STORAGE = 13    # out of local storage space
ERROR_DESTROYED = 14    # a closed object has been destroyed
ERROR_SERVICE = 15    # service not supported
ERROR_OBJECT = 16    # object not supported
ERROR_DATA = 17    # data content not supported
ERROR_VERSION = 18    # VEMMI version not supported

# Transfer entity
TRANSFER_DATA = 0     # data transfer
TRANSFER_ABORT = 1     # transfer abort

# Acknowledge
ACK_SUCCESS = 0     # transfer successful
ACK_ABORT = 1     # transfer abort, no further information
ACK_ABORT_FILENAME = 2     # transfer abort, invalid filename
ACK_ABORT_DIRECTORY = 3     # transfer abort, directory not found
ACK_ABORT_ACCESS = 4     # transfer abort, access not allowed
ACK_ABORT_SIZE = 5     # transfer abort, filesize exceeds allowed space
ACK_ABORT_PROTOCOL = 6     # transfer abort, protocol error


# §8.5 Objects, components

# Multimedia content id
MM_HTML = 0     # HTML

# Sound format
SOUND_WAVE = 0     # WAVE
SOUND_MIDI = 1     # MIDI
SOUND_VIDEOTEX = 2     # ETS 300 149

# Message
MESSAGE_GENERAL = 0     # general message
MESSAGE_INFO = 1     # information message
MESSAGE_WARN = 2     # warning message
MESSAGE_ACTION = 3     # action message

# Destroy event
EVENT_DESTROY_ANY = 0     # destroy by any user action
EVENT_DESTROY_BUTTON = 1     # destroy by validation of implicit defined button
EVENT_DESTROY_CMD = 2     # destroy by an explicit command from the host
EVENT_CLOSE_BUTTON = 3     # close by validation of implicit defined button
EVENT_CLOSE_ANY = 4     # close by any user interaction
EVENT_NONE = 5     # no implicit destroy event defined

# Bitmap object
BITMAP_DATA = 0     # bitmap data
BITMAP_FILE = 1     # bitmap file

# Pict file type
PICT_JPEG = 0     # JPEG
PICT_GIF = 1     # GIF
PICT_BMP = 2     # BMP

# Font family
FN_SWISS = 0     # SWISS (sans-serif)
FN_ROMAN = 1     # ROMAN (serif)
FN_FIXFONT = 2     # FIXFONT (monospaced)

# Text file type
TEXT_IN_TEXT = 0     # "in-text" format
TEXT_PLAIN = 1     # plain text, incl. CR, LF


# §8.6 Local actions

# Report type
REPORT_OIN_CIN = 0     # report OIN, CIN
REPORT_CURRENT = 1     # report current value
REPORT_ALL = 2     # report all values
REPORT_CHANGED = 3     # report all changed values

# General command type
CMD_USER_LOCK = 50    # user lock
CMD_NOP = 52    # no operation

# Specific command type
CMD_OPEN_CPN = 100   # open components of the parent object
CMD_CLOSE_CPN = 101   # close components of the parent object
CMD_OPEN_OBJ = 102   # open objects
CMD_CLOSE_OBJ = 103   # close objects
CMD_DIS_CPN = 104   # change comp. of the parent obj. to inacc.
CMD_ENA_CPN = 105   # change comp. of the parent obj. to access.
CMD_DESTROY_OBJ = 106   # destroy objects
CMD_OPEN_BLKNG = 107   # open blocking object (only one)


# §9 Encoding

# §9.1 Command structure

# MDI (see T.101 for encodings)
MDI_MORE = b'\x2E'   # MORE, no translation
MDI_MORE_3IN4 = b'\x3E'   # MORE, 3 in 4 encoding
MDI_MORE_7SHIFT = b'\x4E'   # MORE, 7 shift encoding
MDI_LAST = b'\x2F'   # LAST, no translation
MDI_LAST_3IN4 = b'\x3F'   # LAST, 3 in 4 encoding
MDI_LAST_7SHIFT = b'\x4F'   # LAST, 7 shift encoding


# §9.4 Attributes and lower level symbols

# Alignments
ALIGN_LEFT = 0
ALIGN_RIGHT = 1
ALIGN_CENTRED = 2

# Bitmap disp type
BM_STRETCHED = 0
BM_CENTRED = 1
BM_TILED = 2

# Echo
ECHO_LOCAL = 0     # local echo
ECHO_NONE = 1     # no echo
ECHO_CHAR = 2     # echo defined character

# Input type
INPUT_ANY = 0     # any character
INPUT_ALPHA = 1     # alphabetic
INPUT_NUM = 2     # numeric
INPUT_ALPHANUM = 3     # alphanumeric

# Input transform
INP_TRANS_NONE = 0     # no transformation
INP_TRANS_LOWER = 1     # to lower
INP_TRANS_UPPER = 2     # to upper

# Program type
PROGRAM_STANDALONE = 0     # standalone program
PROGRAM_FILTER = 1     # filter interface

# Request type
REQUEST_OBJECT = 0     # object request
REQUEST_RESOURCE = 1     # request for resource-file
REQUEST_TEXT_CPN = 2     # request for text component


# §9.5 Opcodes

# Table 39: Host commands opcodes
OPC_OPEN = b'\x20'
OPC_CLOSE = b'\x21'
OPC_RESUME = b'\x22'
OPC_SUSPEND = b'\x23'
OPC_CLOSE_ALL = b'\x24'
OPC_RESET_COLTABLE = b'\x25'
OPC_USER_LOCK = b'\x26'
OPC_USER_UNLOCK = b'\x27'
OPC_OPEN_OBJECT = b'\x28'
OPC_CLOSE_OBJECT = b'\x29'
OPC_DESTROY_OBJECT = b'\x2A'
OPC_ACCESS_DISABLE = b'\x2B'
OPC_ACCESS_ENABLE = b'\x2C'

OPC_CREATE_OBJECT = b'\x30'
OPC_DELETE_OUTDATED_OBJECTS = b'\x31'
OPC_MODIFY_COMPONENT = b'\x32'
OPC_OBJ_LOCATION_CHANGE = b'\x33'
OPC_LOAD_COLTABLE = b'\x34'
OPC_OPEN_APPLICATION = b'\x35'
OPC_STORE_OBJECTS = b'\x36'
OPC_ERASE_OBJECTS = b'\x37'
OPC_OPEN_BLOCKING_OBJECT = b'\x38'
OPC_RESOURCE_FILE_TRANSFERT = b'\x39'
OPC_TERM_CAP_REQUEST = b'\x3A'
OPC_SET_OPTIONS = b'\x3C'


# Table 40: Terminal commands opcodes
OPC_STORE_OBJECTS_RESP = b'\x20'
OPC_OBJECT_RETRANS = b'\x21'
OPC_OPEN_APPL_RESP = b'\x22'
OPC_USER_DATA = b'\x23'
OPC_ERROR = b'\x24'
OPC_TERM_CAP_RESP = b'\x26'

# OPC_RESOURCE_FILE_TRANSFERT is the same as host


# Table 41, 42 & 43: Opcodes
# Objects (2)
OPC_APPLICATION_BAR = b'\x20'
OPC_BUTTON_BAR = b'\x21'
OPC_POP_UP_MENU = b'\x22'
OPC_DIALOG_BOX = b'\x23'
OPC_MULTIMEDIA_OBJECT = b'\x24'
OPC_OPERATIVE_OBJECT = b'\x25'
OPC_SOUND_OBJECT = b'\x26'
OPC_VIDEO_OBJECT = b'\x27'
OPC_MESSAGE_BOX = b'\x28'
OPC_METACODE_OBJECT = b'\x29'
OPC_BITMAP_OBJECT = b'\x2A'
OPC_FONT_OBJECT = b'\x2B'
OPC_TEXT_OBJECT = b'\x2C'
OPC_VIDEOTEX_OBJECT = b'\x2D'
OPC_COMMAND_END = b'\x2F'

# "End"-codes (3)
OPC_END_OF_LIST = b'\x3F'

# Components (4)
OPC_BAR_MENU_CHOICE = b'\x40'
OPC_MENU_CHOICE = b'\x40'
OPC_PULL_DOWN_CHOICE = b'\x41'
OPC_PUSH_BUTTON_COMP = b'\x42'
OPC_POP_UP_CHOICE = b'\x43'
OPC_SEPARATOR = b'\x44'
OPC_FRAME = b'\x45'
OPC_GRAPHIC_OUTPUT_AREA = b'\x46'
OPC_TEXT_AREA = b'\x47'
OPC_TEXT_INPUT_FIELD = b'\x48'
OPC_BOX_PUSH_BUTTON = b'\x49'
OPC_CHECK_BOX = b'\x4A'
OPC_RADIO_BUTTON = b'\x4B'
OPC_LIST_BOX = b'\x4C'
OPC_COMBO_BOX = b'\x4D'
OPC_SENSITIVE_AREA = b'\x4E'

# Components (5)
OPC_SLIDER = b'\x50'
OPC_TEXT_COMPONENT = b'\x51'
OPC_SENSITIVE_TEXT = b'\x52'
OPC_CASC_MENU_CHOICE = b'\x53'
OPC_MULTIMEDIA_AREA = b'\x54'

# Boolean attributes, higher layer symbols (6)
OPC_FN_BOLD = b'\x60'
OPC_FN_UNDERLINE = b'\x61'
OPC_FN_ITALIC = b'\x62'
OPC_INDEX_DEF = b'\x63'
OPC_RGB_DEF = b'\x64'
OPC_LOCACTACT = b'\x65'
OPC_LOCACTVAL = b'\x66'
OPC_VERTICAL = b'\x67'
OPC_CLOSED = b'\x68'
OPC_MODE = b'\x69'
OPC_SEPARATED = b'\x6A'
OPC_NOTACCESSIBLE = b'\x6B'
OPC_MODAL = b'\x6C'
OPC_NO_BORDER = b'\x6D'
OPC_MAXIMIZABLE = b'\x6E'
OPC_RETRANSMISSION_RULE_B = b'\x6F'

OPC_LOCATOR = b'\x60'
OPC_LOCAL_STORAGE = b'\x61'
OPC_REPORT_INDEX = b'\x62'
OPC_DIRECT_NAVIGATION = b'\x63'
OPC_ALIGNMENT = b'\x64'
OPC_DELETE_LIST_ITEM = b'\x6C'

# Boolean attributes, higher layer symbols (7)
OPC_MAXIM_TEXT = b'\x70'
OPC_MARKED = b'\x71'
OPC_MULTIPLE_CHOICE = b'\x72'
OPC_NO_DROP = b'\x73'
OPC_NO_EDIT = b'\x74'
OPC_NO_FORMAT = b'\x76'
OPC_TEMPLATE = b'\x77'
OPC_AUTOSTORE = b'\x78'
OPC_NEGATIVE = b'\x79'
OPC_DIRECT_IN = b'\x7A'
OPC_NO_SOUND = b'\x7B'
OPC_SORTED = b'\x7C'
OPC_ITEM_LOCACT = b'\x7D'
OPC_ITEM_LOCVAL = b'\x7E'
OPC_NO_CONSISTENCY = b'\x7F'

OPC_ARRAYED = b'\x70'
OPC_LIST_TEXT_UNIT = b'\x71'
OPC_DIRECT_TEXT_COMP_REFERENCE = b'\x72'
OPC_CONTENT_ASSOCIATED = b'\x73'
OPC_NON_CONTROLLED_MODE = b'\x74'
OPC_DELETE_ALL_ITEMS = b'\x76'
OPC_MORE_BLOCKS = b'\x7A'
OPC_DIRECT_DATA = b'\x7C'

# Coordinates, dimensions, end-of-string
OPC_XPOS = b'\x90'
OPC_YPOS = b'\x91'
OPC_HEIGHT = b'\x92'
OPC_WIDTH = b'\x93'
OPC_END_OF_STRING = b'\x9C'
OPC_END_OF_STRING_LIST = b'\x9D'
OPC_LIST_STRING = b'\x9E'

# Integer attributes (10)
OPC_FN_FAMILY = b'\xA0'
OPC_FN_HEIGHT = b'\xA1'
OPC_FN_COLOUR = b'\xA2'
OPC_BMCOMPR = b'\xA3'
OPC_BITS_PER_UNIT = b'\xA4'
OPC_COLOUR_ENTRY = b'\xA5'
OPC_GRAPHIC = b'\xA6'
OPC_AUDIOVISUAL = b'\xA7'
OPC_FILE_TRANSFERT = b'\xA8'
OPC_MESSAGE_TYPE = b'\xA9'
OPC_DESTROY_EVENT = b'\xAA'
OPC_VIN_REFERENCE = b'\xAC'
OPC_FIN_REFERENCE = b'\xAD'
OPC_MIN_REFERENCE = b'\xAE'
OPC_TIN_REFERENCE = b'\xAF'

OPC_DATA_TYPES = b'\xA1'
OPC_TEXT_TYPE = b'\xA2'
OPC_STILL_PICTURE = b'\xA3'
OPC_VIDEOTEX = b'\xA4'
OPC_AUDIO = b'\xA5'

# Integer attributes (11)
OPC_LIST_SPEC = b'\xB0'
OPC_ERROR_OIN = b'\xB1'
OPC_ERROR_CIN = b'\xB2'
OPC_ERROR_COM_CODE = b'\xB3'
OPC_LOCAL_COMMANDS = b'\xB4'
OPC_INPUT_TRANSFORM = b'\xB5'
OPC_REQUEST_TYPE = b'\xB6'
OPC_DEFECTIVE = b'\xB7'
OPC_BIN_REFERENCE = b'\xB8'
OPC_TITLE_FONT = b'\xB9'
OPC_COLOUR = b'\xBA'
OPC_BITMAP_DISPTYPE = b'\xBB'
OPC_INITIAL_FONT = b'\xBC'
OPC_LABEL_FONT = b'\xBD'
OPC_INPUT_TYPE = b'\xBE'

OPC_MULTIMEDIA_TYPE = b'\xB2'
OPC_INPUT_FONT = b'\xB9'

# Integer attributes (12)
OPC_ECHO_TYPE = b'\xC0'
OPC_MAX_CHAR = b'\xC1'
OPC_GROUP = b'\xC2'
OPC_DEFAULT_ITEM = b'\xC3'
OPC_LIST_INDEX = b'\xC4'
OPC_MAX_LINE = b'\xC5'
OPC_MULTIMEDIA_CONTENT_TYPE = b'\xC6'
OPC_CIN_REFERENCE = b'\xC7'
OPC_MIN_VALUE = b'\xC8'
OPC_MAX_VALUE = b'\xC9'
OPC_INCREMENT = b'\xCA'
OPC_INITIAL_VALUE = b'\xCB'
OPC_MAX_TIME = b'\xCC'
OPC_INPUT_TIMEOUT = b'\xCD'
OPC_TIMESTAMP = b'\xCE'

OPC_MAPPED = b'\xCB'

# Integer attributes (13)
OPC_RANGE_SPEC = b'\xD0'
OPC_PROGRAM_TYPE = b'\xD1'
OPC_PREV_TEXT = b'\xD2'
OPC_CURRENT_TEXT = b'\xD3'
OPC_NEXT_TEXT = b'\xD4'
OPC_ONE_IN = b'\xD5'

# String attributes (14)
OPC_APPLID = b'\xE0'
OPC_APPL_ADD_DATA = b'\xE1'
OPC_DEFAULT_DIRECTORY = b'\xE2'
OPC_TEXT = b'\xE3'
OPC_TITLE = b'\xE4'
OPC_LABEL = b'\xE5'
OPC_ECHO_CHAR = b'\xE6'
OPC_VTX_CONTENT = b'\xE7'
OPC_FILENAME = b'\xE8'
OPC_PROGRAM_PARAMETER = b'\xE9'
OPC_CURRENT_BLOCK = b'\xEA'
OPC_BASIC_PAGE_NBR = b'\xEC'

OPC_USER_LANGUAGE = b'\xE0'
OPC_SYSTEM_INFORMATION = b'\xE1'
