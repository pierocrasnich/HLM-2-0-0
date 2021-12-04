# ----- File and Path ------------------------------------------------------------------------------------------------ #
DIR_JSON = ''
DIR_CSV = ''
DIR_DB = ''
DIR_IMAGES = ''
DIR_ICONS = ''
DIR_CLASSI = ''
DIR_UTILITY = ''
DIR_BACKUP = 'backup/'
DIR_DECKS = 'deckFiles/'
DIR_OBJ = 'object/'
FILE_SETTINGS = 'json/settings.json'
FILE_HANDLES = ''
FILE_DB = ''
FILE_INFO = ''
# ----- Database Configuration --------------------------------------------------------------------------------------- #
DB_SERVER = []
DB_IP = []
DB_PORT = 0
DB_NAME = ''
DB_CHECK_TIME = 0
DB = None
DB_INPUTLIST = None
DB_INPUTCONFIG = None
DB_OUTPUTLIST = None
DB_MODULECONFIG = None
DB_CONNECTIONLIST = None
DB_OBJECTLIST = None
DB_PLCZONECONFIG = None
DB_LOGGER = None
# ----- Logger Configuration ----------------------------------------------------------------------------------------- #
LOGGER_ACTIVE = False
# ----- Export device Configuration ---------------------------------------------------------------------------------- #
EXPORT_DEVICE = 'USB'  # USB or DESKTOP
# ----- Configurazione registri input -------------------------------------------------------------------------------- #
INPUT_TYPE = []
REG_TYPE = []
# ----- Numero Porte ------------------------------------------------------------------------------------------------- #
DOOR_NUMBER = 0
# ----- Configurazione PLC ------------------------------------------------------------------------------------------- #
PLC_MASTER = ''
PLC_ALIVE = 0
PLC_MASTER_ONLINE = False
PLC_MASTER_THREAD = None
PLC_THREAD = None
PLC_ONLINE = []
# ----- Deck Configuration ------------------------------------------------------------------------------------------- #
# file dimension
DECK_CONF = [
    {"name": "Deck 01", "file": "01.png"},
    {"name": "Deck 02", "file": "02.png"},
    {"name": "Deck 03", "file": "03.png"},
    ]
# ----- OBJECT Configuration ----------------------------------------------------------------------------------------- #
OBJ_MODIFY = False
OBJ_DEFAULT_DK = 0
OBJ_RGB_NORMAL = [0, .8, 0, 1]
OBJ_RGB_FAULT = [200/255, 220/255, 0/255, 1]
OBJ_RGB_NO_DATA = [0, .2, 1, 1]
# ----- Comandi Stringa ---------------------------------------------------------------------------------------------- #
DOOR_DEFAULT = ''
DOOR_BROADCAST = ''
BEGIN = ''
END = ''
CHANGE = ''
TEMPERATURE = ''
HL_FLASH = []
HL_POWER = []
TEST = ''
OFF = ''
COMMAND = ''
# ----- Color VAR ---------------------------------------------------------------------------------------------------- #
RGBA_INFO = []
RGBA_ERROR = []
RGBA_SUCCESS = []
RGBA_BG_DARK = []
RGBA_BG_LIGHT = []
RGBA_WHITE = []
RGBA_WHITE50 = []
RGBA_BLACK = []
RGBA_BLACK50 = []
RGBA_ORANGE = []
RGBA_BLUE = []
RGBA_TITLE_COL = []
RGBA_BAR_ON = []
RGBA_BAR_OFF = []
RGBA_BTN_ON = []
RGBA_BTN_OFF = []
RGBA_INPUT_FOREG = []
RGBA_CURSOR = []
RGBA_MODULE = []
RGBA_NORMAL = []
RGBA_DOWN = []
RGBA_BORDER = []
RGBA_MOD_NORM = []
RGBA_MOD_DOWN = []
RGBA_MOD_BORDER = []
# ----- Thread Object ------------------------------------------------------------------------------------------------ #
DB_STATUS = None
PLC_MASTER_STATUS = None
# ----- Module List -------------------------------------------------------------------------------------------------- #
MODULE = []
# ----- Global Var fot TCP Server ------------------------------------------------------------------------------------ #
HEADER = 64
PORT = 10000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = ''