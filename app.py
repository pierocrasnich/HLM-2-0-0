# !/usr/bin/python3

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar
from kivy.config import Config

from pymongo import MongoClient, errors
from threading import Thread
import socket
import time


# -- Import Personal Utility ------------------------------------------------------------------------------------------#
import utility.gvar as GV

# -- Import Personal Style ------------------------------------------------------------------------------------------#
Builder.load_file('classi/style.kv')

# -- Carimento delle classi personali esterne ------------------------------------------------------------------------ #
Builder.load_file('classi/consoleLog.kv')
from classi.consoleLog import LoggerConsole

Builder.load_file('classi/jsoneditor.kv')
from classi.jsoneditor import JsonEditorPopup

# -- Caricamento screen main page ------------------------------------------------------------------------------------ #
Builder.load_file('main/dashscreen.kv')
from main.dashscreen import DashScreen

Builder.load_file('main/connectscreen.kv')
from main.connectscreen import ConnectScreen

Builder.load_file('main/inputscreen.kv')
from main.inputscreen import InputScreen

Builder.load_file('main/outputscreen.kv')
from main.outputscreen import OutputScreen

Builder.load_file('main/informationscreen.kv')
from main.informationscreen import ProjectScreen

Builder.load_file('main/loginscreen.kv')
from main.loginscreen import LoginScreen

Builder.load_file('main/settingscreen.kv')
from main.settingscreen import SettingsScreen

Builder.load_file('main/connectlist.kv')
from main.connectlist import ConnectListScreen

Builder.load_file('main/testingscreen.kv')
from main.testingscreen import TestingScreen

Builder.load_file('main/modulescreen.kv')
from main.modulescreen import ModuleScreen

Builder.load_file('main/objectscreen.kv')
from main.objectscreen import ObjectScreen


# ################################################## INIT APP ######################################################## #
def init_config():
    json_store = JsonStore(GV.FILE_SETTINGS)
    GV.REG_TYPE = json_store['Config']['register_type']
    GV.INPUT_TYPE = json_store['Config']['input_type']
    GV.PLC_MASTER = json_store['PLC_master']['plc_master']
    GV.PLC_ALIVE = json_store['PLC_master']['plc_alive']
    GV.DIR_JSON = json_store['Settings']['dir_json']
    GV.DIR_DB = json_store['Settings']['dir_db']
    GV.DIR_CSV = json_store['Settings']['dir_csv']
    GV.DIR_ICONS = json_store['Settings']['dir_icons']
    GV.DIR_IMAGES = json_store['Settings']['dir_images']
    GV.FILE_DB = json_store['Settings']['file_db']
    GV.FILE_INFO = json_store['Settings']['file_info']
    GV.FILE_HANDLES = json_store['Settings']['file_handles']


def init_db():
    json_store = JsonStore(GV.DIR_JSON + GV.FILE_DB)
    GV.DB_SERVER = json_store['DBConfig']
    for server in GV.DB_SERVER:
        GV.DB_IP.append(server['server']+':'+server['port'])
    # GV.DB_IP = json_store['DBConfig']['server']
    # GV.DB_PORT = json_store['DBConfig']['port']
    GV.DB_NAME = json_store['DBName']
    GV.DB_CHECK_TIME = json_store['DBCheckTime']
    GV.DB_INPUTCONFIG = json_store['DBCollection']['inputConfig']
    GV.DB_STATUS_THREAD = Thread(target=db_status)
    GV.DB_STATUS_THREAD.setDaemon(True)
    GV.DB_STATUS_THREAD.start()


def db_status():
    while True:
        try:
            db_connect = MongoClient(host=GV.DB_IP, ServerSelectionTimeoutMS=50, replicaset="rs0")
            GV.DB = db_connect[GV.DB_NAME]
            status = db_connect.server_info()
        except errors.ServerSelectionTimeoutError:
            GV.DB = None
        except errors.ConnectionFailure:
            GV.DB = None
        time.sleep(GV.DB_CHECK_TIME)


def init_parameter():
    json_store = JsonStore(GV.FILE_SETTINGS)
    GV.RGBA_INFO = json_store['Color']['info']
    GV.RGBA_ERROR = json_store['Color']['error']
    GV.RGBA_SUCCESS = json_store['Color']['success']
    GV.RGBA_BG_DARK = json_store['Color']['bg_dark']
    GV.RGBA_BG_LIGHT = json_store['Color']['bg_light']
    GV.RGBA_WHITE = json_store['Color']['white']
    GV.RGBA_WHITE50 = json_store['Color']['white50']
    GV.RGBA_BLACK = json_store['Color']['black']
    GV.RGBA_BLACK50 = json_store['Color']['black50']
    GV.RGBA_ORANGE = json_store['Color']['orange']
    GV.RGBA_BLUE = json_store['Color']['blue']
    GV.RGBA_TITLE_COL = json_store['Color']['title_col']
    GV.RGBA_BAR_ON = json_store['Color']['bar_on']
    GV.RGBA_BAR_OFF = json_store['Color']['bar_off']
    GV.RGBA_BTN_ON = json_store['Color']['btn_on']
    GV.RGBA_BTN_OFF = json_store['Color']['btn_off']
    GV.RGBA_INPUT_FOREG = json_store['Color']['input_foreg']
    GV.RGBA_CURSOR = json_store['Color']['cursor']
    GV.RGBA_MODULE = json_store['Color']['module']
    GV.RGBA_NORMAL = json_store['Color']['btn_normal']
    GV.RGBA_DOWN = json_store['Color']['btn_down']
    GV.RGBA_BORDER = json_store['Color']['btn_border']
    GV.RGBA_MOD_NORM = json_store['Color']['mod_normal']
    GV.RGBA_MOD_DOWN = json_store['Color']['mod_down']
    GV.RGBA_MOD_BORDER = json_store['Color']['mod_border']


def init_handles():
    json_store = JsonStore(GV.DIR_JSON + GV.FILE_HANDLES)
    GV.DOOR_NUMBER = json_store['door_number']
    GV.DOOR_DEFAULT = json_store['door_default']
    GV.DOOR_BROADCAST = json_store['door_broadcast']
    GV.BEGIN = json_store['begin']
    GV.END = json_store['end']
    GV.OFF = json_store['off']
    GV.CHANGE = json_store['change']
    GV.TEMPERATURE = json_store['temperature']
    GV.HL_FLASH = json_store['flash']
    GV.HL_POWER = json_store['power']
    GV.TEST = json_store['test']


def init_collection():
    json_store = JsonStore(GV.DIR_JSON + GV.FILE_DB)
    if GV.DB:
        GV.DB_INPUTCONFIG = GV.DB[json_store['DBCollection']['inputConfig']]
        GV.DB_INPUTLIST = GV.DB[json_store['DBCollection']['inputList']]
        GV.DB_MODULECONFIG = GV.DB[json_store['DBCollection']['moduleConfig']]
        GV.DB_OUTPUTLIST = GV.DB[json_store['DBCollection']['outputList']]
        GV.DB_CONNECTIONLIST = GV.DB[json_store['DBCollection']['connectionList']]
        GV.DB_OBJECTLIST = GV.DB[json_store['DBCollection']['objectList']]
        GV.DB_PLCZONECONFIG = GV.DB[json_store['DBCollection']['plcZoneConfig']]
        GV.DB_LOGGER = GV.DB[json_store['DBCollection']['logger']]
    else:
        time.sleep(.5)
        init_collection()


def init_plc():
    GV.PLC_MASTER_THREAD = Thread(target=plc_master_status)
    GV.PLC_MASTER_THREAD.start()
    GV.PLC_THREAD = Thread(target=plc_status)
    GV.PLC_THREAD.setDaemon(True)
    GV.PLC_THREAD.start()


def plc_master_status():
    plc_master_log = True
    while True:
        timestamp = time.strftime('%d/%m/%Y   %H:%M:%S')
        try:
            plc_master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            plc_master.settimeout(1)
            plc_master.connect((GV.PLC_MASTER, 2455))
            GV.PLC_MASTER_ONLINE = True
            if not plc_master_log:
                plc_master_log = True
                logger_class = 'success'
                logger_text = 'PLC Master is online'
                if GV.LOGGER_ACTIVE:
                    GV.DB_LOGGER.insert_one({'timestamp': timestamp, 'event': logger_class, 'message': logger_text})
        except:
            GV.PLC_MASTER_ONLINE = False
            if plc_master_log:
                plc_master_log = False
                logger_class = 'error'
                logger_text = 'PLC zone Master is offline'
                if GV.LOGGER_ACTIVE:
                    GV.DB_LOGGER.insert_one({'timestamp': timestamp, 'event': logger_class, 'message': logger_text})
        time.sleep(GV.PLC_ALIVE)


def plc_status():
    # plc_area_log = []
    # for item in GV.DB_PLCZONECONFIG.find({}):
    #     plc_area_log.append({'item': item['_id'], 'state': True})
    while True:
        plc_area_log = []
        for item in GV.DB_PLCZONECONFIG.find({}):
            plc_area_log.append({'item': item['_id'], 'state': True})
        GV.PLC_ONLINE = []
        for item in GV.DB_PLCZONECONFIG.find({}):
            log_status = next(x for x in plc_area_log if x["item"] == item["_id"])
            timestamp = time.strftime('%d/%m/%Y   %H:%M:%S')
            try:
                plc_area = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                plc_area.settimeout(1)
                plc_area.connect((GV.PLC_MASTER[:-3] + str(item['address']), 2455))
                GV.PLC_ONLINE.append({'item': item['_id'], 'state': True})
                if not log_status['state']:
                    log_status['state'] = True
                    logger_class = 'success'
                    logger_text = 'PLC zone ' + item['name'] + ' is online'
                    if GV.LOGGER_ACTIVE:
                        GV.DB_LOGGER.insert_one({'timestamp': timestamp, 'event': logger_class, 'message': logger_text})
            except:
                GV.PLC_ONLINE.append({'item': item['_id'], 'state': False})
                if log_status['state']:
                    log_status['state'] = False
                    logger_class = 'error'
                    logger_text = 'PLC zone ' + item['name'] + ' is offline'
                    if GV.LOGGER_ACTIVE:
                        GV.DB_LOGGER.insert_one({'timestamp': timestamp, 'event': logger_class, 'message': logger_text})
        time.sleep(GV.PLC_ALIVE)


# ################################################## Splash Page ##################################################### #
class LoadProgressBar(ProgressBar):

    def update_value(self):
        self.load = Clock.schedule_interval(self.new_value, .05)

    def new_value(self, dt):
        if self.value < 1:
            self.value += .01
        else:
            self.load.cancel()
            self.ms_splash.ms.switch_to(self.ms_splash.ms.main)


# ################################################## Clock ########################################################### #
class ClockWidget(Label):

    def __init__(self, **kwargs):
        super(ClockWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.text = time.strftime('%d/%m/%Y   %H:%M:%S')


# ################################################## Notification MSG ################################################ #
class NotificationMSG(Label):

    def __init__(self, **kwargs):
        super(NotificationMSG, self).__init__(**kwargs)

    def notification_msg(self, msg_color, msg_text):
        color_set = []
        if msg_color == 'info':
            color_set = 0/255, 162/255, 162/255, 1
        elif msg_color == 'error':
            color_set = 229/255, 36/255, 33/255, 1
        elif msg_color == 'success':
            color_set = 102/255, 179/255, 46/255, 1
        self.color = color_set
        self.text = msg_text
        Clock.schedule_once(self.clear, 7)

    def clear(self, instance):
        self.text = ''


# ################################################## Logger ########################################################## #
class LoggerStatus(Button):
    # logger_class = 'info'/ 'error' / 'success'

    def __init__(self, **kwargs):
        super(LoggerStatus, self).__init__(**kwargs)
        self.console = LoggerConsole()

    def build(self):
        if GV.LOGGER_ACTIVE:
            self.text = 'Logger enabled'
            self.color = GV.RGBA_SUCCESS
        else:
            self.color = GV.RGBA_ERROR
            self.text = 'Logger disabled'
        self.ms_main.add_widget(self.console)

    def open_console(self):
        self.console.opacity = 1
        self.console.init_data()

    def logger_add(self, logger_class, logger_text):
        timestamp = time.strftime('%d/%m/%Y   %H:%M:%S')

        if GV.LOGGER_ACTIVE:
            GV.DB_LOGGER.insert_one({'timestamp': timestamp, 'event': logger_class, 'message': logger_text})


# ################################################ Main Menu BUTTON ################################################## #
class MainMenuButton(ToggleButton):

    def open_dash_screen(self):
        self.mcc_manager.switch_to(self.mcc_manager.mccm_dash)

    def open_input_screen(self):
        self.mcc_manager.switch_to(self.mcc_manager.mccm_input)

    def open_output_screen(self):
        self.mcc_manager.switch_to(self.mcc_manager.mccm_output)

    def open_connect_screen(self):
        self.mcc_manager.switch_to(self.mcc_manager.mccm_connect)

    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)


# ################################################ Service Menu BUTTON ############################################### #
class ServiceMenuButton(ToggleButton):

    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)

    def change_screen(self, screen):
        self.mcc_manager.switch_to(screen)


# ################################################ Main ScreenManager     ############################################ #
class MainScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        self.transition = FadeTransition()
        self.main = MainScreen(ms=self)
        self.splash = SplashScreen(ms=self)
        self.switch_to(self.splash)


class MainScreen(Screen):
    ms = ObjectProperty(None)

    def on_enter(self, *args):
        self.mm_logger.build()


class SplashScreen(Screen):
    ms = ObjectProperty(None)

    def on_enter(self, *args):
        self.mss_load.update_value()
        # init_parameter()
        # init_config()
        init_db()
        init_collection()
        init_plc()
        init_handles()


# ############################################### Content Screen Manager ############################################# #
class ContentScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(ContentScreenManager, self).__init__(**kwargs)
        self.transition = NoTransition(duration=0)
        self.mccm_dash = DashScreen(mccm=self)
        self.mccm_input = InputScreen(mccm=self)
        self.mccm_output = OutputScreen(mccm=self)
        self.mccm_connect = ConnectScreen(mccm=self)
        self.mccm_settings = SettingsScreen(mccm=self)
        self.mccm_project = ProjectScreen(mccm=self)
        self.mccm_test = TestingScreen(mccm=self)
        self.mccm_login = LoginScreen(mccm=self)
        self.mccm_list = ConnectListScreen(mccm=self)
        self.mccm_module = ModuleScreen(mccm=self)
        self.mccm_object =ObjectScreen(mccm=self)
        self.switch_to(self.mccm_dash)



# ################################################ Main Application Start ############################################ #
class HLMApp(App):

    def build(self):
        return MainScreenManager()


if __name__ == '__main__':
    init_config()
    # init_db()
    init_parameter()
    # init_plc()
    Window.size = (1920, 1080)
    Window.left = 50
    Window.top = 50
    # Window.borderless = True
    Window.borderless = False
    Config.set('kivy', 'exit_on_escape', '0')  # Disable ESC button
    HLMApp().run()
