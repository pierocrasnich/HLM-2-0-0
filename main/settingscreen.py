from kivy.app import App
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from threading import Thread
from pymongo import MongoClient, errors, ASCENDING, DESCENDING
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.stacklayout import StackLayout
from kivy.uix.spinner import Spinner, SpinnerOption
from bson import ObjectId
import json
import signal

# -- Import Personal Utility ------------------------------------------------------------------------------------------#
import utility.gvar as GV

Builder.load_file('main/classi/settings.kv')


# ----- Classe generale del layout ----------------------------------------------------------------------------------- #
class SettingsScreen(Screen):
    mccm = ObjectProperty(None)

    def on_enter(self, *args):
        self.ss_container.update_info()
        self.ss_container.update_db()
        self.ss_container.update_plc_master()
        self.ss_container.ssc_plc_container.remove_plc()
        self.ss_container.ssc_input_container.init_container()
        self.ss_container.ssc_handles_num.text = str(GV.DOOR_NUMBER)
        self.ss_container.ssc_handles_num_ti.text = str(GV.DOOR_NUMBER)

    # ----- funzione per la chiusura dell'applicazione  -----#
    @staticmethod
    def exit():
        App.get_running_app().stop()
        Window.close()
        #  Kill all Thread Object
        signal.pthread_kill(GV.DB_STATUS_THREAD.ident, signal.SIGKILL)
        signal.pthread_kill(GV.CREATE_COLLECTION_THREAD.ident, signal.SIGKILL)
        signal.pthread_kill(GV.PLC_MASTER_STATUS.ident, signal.SIGKILL)
        signal.pthread_kill(GV.PLC_THREAD.ident, signal.SIGKILL)
        signal.pthread_kill(GV.OBJ_CHANGE_THREAD.ident, signal.SIGKILL)


# ----- Settings Container ------------------------------------------------------------------------------------------- #
class SettingsContainer(RelativeLayout):
    file_info = ObjectProperty(None)  # ----- in fase di inizializzazione per scrivere il testo nel label ----- #
    file_db = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SettingsContainer, self).__init__(**kwargs)
        self.file_info = JsonStore(GV.DIR_JSON + GV.FILE_INFO)
        self.file_db = JsonStore(GV.DIR_JSON + GV.FILE_DB)
        self.file_settings = JsonStore(GV.FILE_SETTINGS)
        self.schedule_plc = None

    # ----- funzione per l'aggiornamento dei label informazione in fase di inizializzazione -----#
    def update_info(self):
        self.ssc_project.text = self.file_info['Info']['project']
        self.ssc_version.text = self.file_info['Info']['version']
        self.ssc_data.text = self.file_info['Info']['date']
        self.ssc_engineer.text = self.file_info['Info']['eng']
        self.ssc_project_ti.text = self.file_info['Info']['project']
        self.ssc_version_ti.text = self.file_info['Info']['version']
        self.ssc_data_ti.text = self.file_info['Info']['date']
        self.ssc_engineer_ti.text = self.file_info['Info']['eng']

    def update_db(self):
        self.ssc_db_config_master.text = GV.DB_SERVER[0]['server']
        self.ssc_db_config_master_port.text = str(GV.DB_SERVER[0]['port'])
        self.ssc_db_config_replica.text = GV.DB_SERVER[1]['server']
        self.ssc_db_config_replica_port.text = str(GV.DB_SERVER[1]['port'])
        self.ssc_db_config_name.text = GV.DB_NAME
        self.ssc_db_config_alive.text = str(GV.DB_CHECK_TIME) + " sec."
        # self.ssc_db_config_ip_ti.text = self.file_db['DBConfig']['server']
        # self.ssc_db_config_port_ti.text = self.file_db['DBConfig']['port']
        # self.ssc_db_config_name_ti.text = self.file_db['DBConfig']['database']
        # self.ssc_db_config_time_ti.text = str(self.file_db['DBConfig']['check_time'])

    def update_info_json(self):
        self.file_info['Info'] = {'project': self.ssc_project_ti.text,
                                  'version': self.ssc_version_ti.text,
                                  'date': self.ssc_data_ti.text,
                                  'eng': self.ssc_engineer_ti.text}
        self.update_info()

    def update_db_json(self):
        try:
            db_test = MongoClient(host=[self.ssc_db_config_ip_ti.text + ':' + self.ssc_db_config_port_ti.text],
                                  ServerSelectionTimeoutMS=100)
            db_name = db_test[self.ssc_db_config_name_ti.text]
            GV.DB_IP = self.ssc_db_config_ip_ti.text
            GV.DB_PORT = self.ssc_db_config_port_ti.text
            GV.DB_NAME = self.ssc_db_config_name_ti.text
            GV.DB_CHECK_TIME = int(self.ssc_db_config_time_ti.text)
            GV.DB = db_name
            self.file_db['DBConfig'] = {'server': self.ssc_db_config_ip_ti.text,
                                        'port': self.ssc_db_config_port_ti.text,
                                        'database': self.ssc_db_config_name_ti.text,
                                        'check_time': int(self.ssc_db_config_time_ti.text)}
            self.update_db()
        except errors.ConnectionFailure as err:
            GV.DB = None

    def update_plc_master(self):
        self.ssc_plc_master.text = GV.PLC_MASTER + " (Alive " + str(GV.PLC_ALIVE) + "sec.)"
        self.ssc_plc_master_ti.text = GV.PLC_MASTER
        self.ssc_plc_alive_ti.text = str(GV.PLC_ALIVE)

    def update_plc_master_json(self):
        GV.PLC_MASTER = self.ssc_plc_master_ti.text
        GV.PLC_ALIVE = int(self.ssc_plc_alive_ti.text)
        self.ssc_plc_master.text = GV.PLC_MASTER + " (Alive " + str(GV.PLC_ALIVE) + "sec.)"
        self.file_settings['PLC_master'] = {'plc_master': self.ssc_plc_master_ti.text,
                                            'plc_alive': int(self.ssc_plc_alive_ti.text)}
        GV.DB_OBJECTLIST.update_one({'name': 'PLC Master'}, {'$set': {'address': GV.PLC_MASTER}})
        self.mccm_settings.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)
        print(self.ssc_plc_master_ti.text)

    def populate_plc_zona(self):
        while GV.DB_PLCZONECONFIG.find({}).count() != len(GV.PLC_ONLINE):
            pass
        else:
            self.ssc_plc_container.populate_plc()

    def schedule_plc_zona(self):
        self.schedule_plc = Clock.schedule_interval(self.plc_zona_status, 5)

    def plc_zona_status(self, dt):
        for child in self.ssc_plc_container.children:
            if len(GV.PLC_ONLINE) == GV.DB_PLCZONECONFIG.find({}).count():
                for item in GV.PLC_ONLINE:
                    if child.id['_id'] == item['item'] and item['state']:
                        child.color = GV.RGBA_SUCCESS
                    else:
                        child.color = GV.RGBA_ERROR

    def update_plc_zona(self):
        self.schedule_plc.cancel()
        self.ssc_plc_container.remove_plc()


# ----- PLC StackLayout Class ---------------------------------------------------------------------------------------- #
class PLCStackLayout(StackLayout):

    def __init__(self, **kwargs):
        super(PLCStackLayout, self).__init__(**kwargs)
        self.plc_zona = None

    def populate_plc(self):
        for item in GV.DB_PLCZONECONFIG.find({}):
            for status in GV.PLC_ONLINE:
                if status['item'] == item['_id'] and status['state']:
                    color = GV.RGBA_SUCCESS
                else:
                    color = GV.RGBA_ERROR
            self.plc_zona = PLCLabel(id=item,
                                     text=(item['name'] +
                                           " -> IP: " + str(item['address']) +
                                           " -- Com: " + str(item['ComPort'])),
                                     color=color)
            self.plc_zona.bind(on_press=self.plc_zona.print_text)
            self.add_widget(self.plc_zona)
        self.ss_container.schedule_plc_zona()

    def remove_plc(self):
        self.clear_widgets()
        self.ss_container.populate_plc_zona()


# ----- VoiceLabel Class dichiarazione ------------------------------------------------------------------------------- #
class PLCLabel(ButtonBehavior, Label):
    id = ObjectProperty(None)

    def print_text(self, instance):
        if self.parent.ssc_plc_zona_ti.disabled:
            self.parent.ssc_plc_zona_ti.text = instance.id['name']
            self.parent.ssc_plc_zona_ip_ti.text = str(instance.id['address'])
            self.parent.ssc_plc_zona_com_ti.text = str(instance.id['ComPort'])
            self.parent.ssc_plc_zona_info_ti.text = str(instance.id['info'])
            self.parent.ssc_plc_zona_id_ti.text = str(instance.id['_id'])


# ----- classe dei pulsanti che generano le collection all'interno del database -------------------------------------- #
class LoaderCreateCollection(ModalView):
    pass


class CreateListButton (Button):

    def create_collection(self, cursor):
        GV.CREATE_COLLECTION_THREAD = Thread(target=self.generate_collection(cursor))
        GV.CREATE_COLLECTION_THREAD.setDaemon(True)
        GV.CREATE_COLLECTION_THREAD.start()

    def generate_collection(self, cursor):
        loader = LoaderCreateCollection()
        self.parent.add_widget(loader)
        cursor.drop()
        if cursor == GV.DB_INPUTLIST:
            collection_name = 'INPUT'
            list_input = GV.DB_INPUTCONFIG.find({})

            for item in list_input:
                loader.ssc_loader_description.text = 'Generate INPUT collection'
                loader.ssc_loader_progress_bar.max = item['registerNumber']
                for i in range(item['registerNumber']):
                    loader.ssc_loader_progress_bar.value += 1
                    loader.ssc_loader_num.text = '[ ****  ' \
                                                 + str(int(loader.ssc_loader_progress_bar.value)) \
                                                 + ' / ' \
                                                 + str(item['registerNumber']) \
                                                 + '  **** ]'

                    GV.DB_INPUTLIST.insert_one({'register': (item['registerStart'] + i),
                                                'bit': item['registerType'],
                                                'system': item['name'],
                                                'name': item['name'] + '_' + str(item['registerStart'] + i),
                                                'description': ''})

        if cursor == GV.DB_OUTPUTLIST:
            GV.DB_OBJECTLIST.drop()
            collection_name = 'OUTPUT'
            loader.ssc_loader_description.text = 'Generate OBJECT collection'
            loader.ssc_loader_progress_bar.max = GV.DOOR_NUMBER + 1
            for old_hl in GV.DB_OBJECTLIST.find({'system': 'HL'}):
                GV.DB_OBJECTLIST.delete_one({'_id': ObjectId(old_hl['_id'])})

            for hl in range(1, GV.DOOR_NUMBER + 1, 1):
                loader.ssc_loader_progress_bar.value += 1
                loader.ssc_loader_num.text = '[ ****  ' \
                                             + str(int(loader.ssc_loader_progress_bar.value)) \
                                             + ' / ' \
                                             + str(GV.DOOR_NUMBER) \
                                             + '  **** ]'

                GV.DB_OUTPUTLIST.insert_one({'system': 'HL',
                                             'address': str(hl).rjust(4, '0'),
                                             'plc': '',
                                             'port': '',
                                             'name': 'HL' + str(hl).rjust(4, '0'),
                                             'description': ''})

        if cursor == GV.DB_CONNECTIONLIST:
            collection_name = 'CONNECTIONS'
            GV.DB['connectionList']

        if cursor == GV.DB_OBJECTLIST:
            collection_name = 'OBJECT'
            loader.ssc_loader_description.text = 'Generate OBJECT collection'
            loader.ssc_loader_progress_bar.max = GV.DOOR_NUMBER - 1
            # Create PLC MASTER object
            plc_master_obj = JsonStore(GV.FILE_SETTINGS)
            plc_master_address = plc_master_obj['PLC_master']['plc_master']
            GV.DB_OBJECTLIST.insert_one({'system': 'PLCM',
                                         'address': str(plc_master_address),
                                         'name': 'PLC Master',
                                         'deck': GV.OBJ_DEFAULT_DK,
                                         'posX': 0,
                                         'posY': 0,
                                         'rotate': 0,
                                         'status': ''})
            # Create PLC ZONE object
            plc_zone_obj = list(GV.DB_PLCZONECONFIG.find({}))
            for plcZone in plc_zone_obj:
                GV.DB_OBJECTLIST.insert_one({'system': 'PLCZ',
                                             'address': str(plc_master_address[:-3]) + str(plcZone['address']),
                                             'name': plcZone['name'],
                                             'deck': GV.OBJ_DEFAULT_DK,
                                             'posX': 0,
                                             'posY': 0,
                                             'rotate': 0,
                                             'status': ''})
            # Create Handles object
            hl_list = GV.DB_OUTPUTLIST.find({})
            for hl in hl_list:
                loader.ssc_loader_progress_bar.value += 1
                loader.ssc_loader_num.text = '[ ****  ' \
                                             + str(int(loader.ssc_loader_progress_bar.value)) \
                                             + ' / ' \
                                             + str(GV.DOOR_NUMBER) \
                                             + '  **** ]'
                GV.DB_OBJECTLIST.insert_one({'system': 'HL',
                                             'address': hl['address'],
                                             'name': hl['name'],
                                             'deck': GV.OBJ_DEFAULT_DK,
                                             'posX': 0,
                                             'posY': 0,
                                             'rotate': 0,
                                             'status': '',
                                             'colorDX': '000000',
                                             'colorSX': '000000'})
            #  Init OBJECTS - redraw objects
            self.parent.parent.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)

        msg_color = 'success'
        msg_text = 'Reset ' + collection_name + ' collection'
        self.parent.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
        self.parent.remove_widget(loader)


# ----- classe del layout per pallini dello stato delle collection --------------------------------------------------- #
class StatusObject(BoxLayout):
    running = BooleanProperty(None)


class DBStatusObject(StatusObject):

    def __init__(self, **kwargs):
        super(DBStatusObject, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.DB is None:
            self.running = False
        else:
            self.running = True


# ----- Classe per il pallino dello status PLC Master ---------------------------------------------------------------- #
class PLCMasterStatusObject(StatusObject):

    def __init__(self, **kwargs):
        super(PLCMasterStatusObject, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.PLC_MASTER_ONLINE is False:
            self.running = False
        else:
            self.running = True


# ----- classe del per il pallino status INPUT collection ------------------------------------------------------------ #
class InputCollectionStatus(StatusObject):

    def __init__(self, **kwargs):
        super(InputCollectionStatus, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.DB is None:
            self.running = False
        elif 'inputList' in GV.DB.list_collection_names():
            self.running = True
        else:
            self.running = False


# ----- classe del per il pallino status OUTPUT collection ----------------------------------------------------------- #
class OutputCollectionStatus(StatusObject):

    def __init__(self, **kwargs):
        super(OutputCollectionStatus, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.DB is None:
            self.running = False
        elif 'outputList' in GV.DB.list_collection_names():
            self.running = True
        else:
            self.running = False


# ----- classe del per il pallino status MODULE collection ----------------------------------------------------------- #
class ModuleCollectionStatus(StatusObject):

    def __init__(self, **kwargs):
        super(ModuleCollectionStatus, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.DB is None:
            self.running = False
        elif 'moduleConfig' in GV.DB.list_collection_names():
            self.running = True
        else:
            self.running = False


# ----- classe del per il pallino status CONNECTION collection ------------------------------------------------------- #
class ListConnectionStatus(StatusObject):

    def __init__(self, **kwargs):
        super(ListConnectionStatus, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.DB is None:
            self.running = False
        elif 'connectionList' in GV.DB.list_collection_names():
            self.running = True
        else:
            self.running = False


# ----- classe del per il pallino status CONNECTION collection ------------------------------------------------------- #
class ListObjectStatus(StatusObject):

    def __init__(self, **kwargs):
        super(ListObjectStatus, self).__init__(**kwargs)
        self.status = Clock.schedule_interval(self.check_status, 5)

    def check_status(self, dt):
        if GV.DB is None:
            self.running = False
        elif 'objectList' in GV.DB.list_collection_names():
            self.running = True
        else:
            self.running = False


# ----- classe pulsante per la visualizzazione dei collegamenti registrati ------------------------------------------- #
class ListConnectButton(Button):

    def update(self):
        if 'connectionList' in GV.DB.list_collection_names():
            self.disabled = False
        else:
            self.disabled = True

    def open_list_connection(self):
        self.mccm_settings.mccm.switch_to(self.mccm_settings.mccm.mccm_list)


# ---- Edit Button Class --------------------------------------------------------------------------------------------- #
class EditSettingsBtn(Button):
    ref = ObjectProperty(None)

    def edit_info(self):
        if self.ssc_project.opacity == 1:
            self.ssc_project.opacity = 0
            self.ssc_project_ti.disabled = False
            self.ssc_project_ti.opacity = 1
            self.ssc_version.opacity = 0
            self.ssc_version_ti.disabled = False
            self.ssc_version_ti.opacity = 1
            self.ssc_data.opacity = 0
            self.ssc_data_ti.disabled = False
            self.ssc_data_ti.opacity = 1
            self.ssc_engineer.opacity = 0
            self.ssc_engineer_ti.disabled = False
            self.ssc_engineer_ti.opacity = 1
        else:
            self.ssc_project.opacity = 1
            self.ssc_project_ti.disabled = True
            self.ssc_project_ti.opacity = 0
            self.ssc_version.opacity = 1
            self.ssc_version_ti.disabled = True
            self.ssc_version_ti.opacity = 0
            self.ssc_data.opacity = 1
            self.ssc_data_ti.disabled = True
            self.ssc_data_ti.opacity = 0
            self.ssc_engineer.opacity = 1
            self.ssc_engineer_ti.disabled = True
            self.ssc_engineer_ti.opacity = 0
            self.ss_container.update_info_json()

    def edit_db(self):
        if self.ssc_db_config.opacity == 1:
            self.ssc_db_config.opacity = 0
            self.ssc_db_config_ip_ti.disabled = False
            self.ssc_db_config_ip_ti.opacity = 1
            self.ssc_db_config_port_ti.disabled = False
            self.ssc_db_config_port_ti.opacity = 1
            self.ssc_db_config_name_ti.disabled = False
            self.ssc_db_config_name_ti.opacity = 1
            self.ssc_db_config_time_ti.disabled = False
            self.ssc_db_config_time_ti.opacity = 1
        else:
            self.ssc_db_config.opacity = 1
            self.ssc_db_config_ip_ti.disabled = True
            self.ssc_db_config_ip_ti.opacity = 0
            self.ssc_db_config_port_ti.disabled = True
            self.ssc_db_config_port_ti.opacity = 0
            self.ssc_db_config_name_ti.disabled = True
            self.ssc_db_config_name_ti.opacity = 0
            self.ssc_db_config_time_ti.disabled = True
            self.ssc_db_config_time_ti.opacity = 0
            self.ss_container.update_db_json()

    def edit_plc_master(self):
        if self.ssc_plc_master.opacity == 1:
            self.ssc_plc_master.opacity = 0
            self.ssc_plc_master_ti.disabled = False
            self.ssc_plc_master_ti.opacity = 1
            self.ssc_plc_alive_ti.disabled = False
            self.ssc_plc_alive_ti.opacity = 1
        else:
            self.ssc_plc_master.opacity = 1
            self.ssc_plc_master_ti.disabled = True
            self.ssc_plc_master_ti.opacity = 0
            self.ssc_plc_alive_ti.disabled = True
            self.ssc_plc_alive_ti.opacity = 0
            self.ss_container.update_plc_master_json()

    def edit_plc_zona(self):
        if self.ssc_plc_zona_ti.disabled:
            self.ssc_plc_zona_ti.disabled = False
            self.ssc_plc_zona_ip_ti.disabled = False
            self.ssc_plc_zona_com_ti.disabled = False
            self.ssc_plc_zona_info_ti.disabled = False
            self.ssc_plc_zona_add_btn.disabled = True
            self.ssc_plc_zona_del_btn.disabled = True
        else:
            if self.ssc_plc_zona_ti.text != '':
                if 1 <= int(self.ssc_plc_zona_ip_ti.text) < 255:
                    if int(self.ssc_plc_zona_ip_ti.text) != int(GV.PLC_MASTER[-3:]):
                        for item in GV.DB_PLCZONECONFIG.find({}):
                            if item['_id'] != ObjectId(self.ssc_plc_zona_id_ti.text):
                                if item['address'] != int(self.ssc_plc_zona_ip_ti.text):
                                    if 0 < int(self.ssc_plc_zona_com_ti.text) < 65:
                                        self.ssc_plc_zona_ti.disabled = True
                                        self.ssc_plc_zona_ip_ti.disabled = True
                                        self.ssc_plc_zona_com_ti.disabled = True
                                        self.ssc_plc_zona_info_ti.disabled = True
                                        self.ssc_plc_zona_add_btn.disabled = False
                                        self.ssc_plc_zona_del_btn.disabled = False
                                        self.update_plc_zona()

    def update_plc_zona(self):
        plc_zone_obj = GV.DB_PLCZONECONFIG.find_one({'_id': ObjectId(self.ssc_plc_zona_id_ti.text)})
        GV.DB_OBJECTLIST.update_one({'name': plc_zone_obj['name']},
                                    {'$set': {'name': self.ssc_plc_zona_ti.text,
                                              'address': GV.PLC_MASTER[:-3] + self.ssc_plc_zona_ip_ti.text}})
        self.mccm_settings.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)
        GV.DB_PLCZONECONFIG.update_one({'_id': ObjectId(self.ssc_plc_zona_id_ti.text)},
                                       {'$set': {'name': self.ssc_plc_zona_ti.text,
                                                 'address': int(self.ssc_plc_zona_ip_ti.text),
                                                 'ComPort': int(self.ssc_plc_zona_com_ti.text),
                                                 'info': self.ssc_plc_zona_info_ti.text}})
        self.ss_container.update_plc_zona()

    def edit_handles(self):

        if self.ssc_handles_num_ti.disabled:
            self.ssc_handles_num_ti.disabled = False
            self.ssc_handles_num_ti.opacity = 1
            self.ssc_handles_num.opacity = 0
        else:
            self.ssc_handles_num_ti.disabled = True
            self.ssc_handles_num_ti.opacity = 0
            self.ssc_handles_num.opacity = 1
            GV.CREATE_COLLECTION_THREAD = Thread(target=self.update_door)
            GV.CREATE_COLLECTION_THREAD.setDaemon(True)
            GV.CREATE_COLLECTION_THREAD.start()

    def update_door(self):
        loader = LoaderCreateCollection()

        self.parent.add_widget(loader)

        if int(self.ssc_handles_num_ti.text) == 0:
            self.ssc_handles_num_ti.text = str(GV.DOOR_NUMBER)
            self.parent.remove_widget(loader)
            return
        elif int(self.ssc_handles_num_ti.text) == GV.DOOR_NUMBER:
            self.parent.remove_widget(loader)
            return
        elif int(self.ssc_handles_num_ti.text) > 0 and int(self.ssc_handles_num_ti.text) > GV.DOOR_NUMBER:
            loader.ssc_loader_description.text = 'Add Handler'
            document_add = int(self.ssc_handles_num_ti.text) - GV.DOOR_NUMBER
            loader.ssc_loader_progress_bar.max = document_add
            # print('add', document_add)
            for hl in range(GV.DOOR_NUMBER + 1, GV.DOOR_NUMBER + 1 + document_add, 1):
                loader.ssc_loader_progress_bar.value += 1
                loader.ssc_loader_num.text = '[ ****  ' + str(int(loader.ssc_loader_progress_bar.value)) + ' / ' + str(document_add) + '  **** ]'
                GV.DB_OUTPUTLIST.insert_one({'system': 'HL',
                                             'address': str(hl).rjust(4, '0'),
                                             'plc': '',
                                             'port': '',
                                             'name': 'HL' + str(hl).rjust(4, '0'),
                                             'description': ''})
                self.mccm_settings.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)
        elif int(self.ssc_handles_num_ti.text) < GV.DOOR_NUMBER:
            loader.ssc_loader_description.text = 'Remove Handler'
            document_del = GV.DOOR_NUMBER - int(self.ssc_handles_num_ti.text)
            loader.ssc_loader_progress_bar.max = document_del
            result = GV.DB_OUTPUTLIST.find({}).sort('_id', DESCENDING).limit(document_del)
            for count, item in enumerate(list(result)):
                loader.ssc_loader_progress_bar.value += 1
                loader.ssc_loader_num.text = '[ ****  ' + str(int(loader.ssc_loader_progress_bar.value)) + '/' + str(document_del) + '  **** ]'
                # Remove Output from "outputList"
                GV.DB_OUTPUTLIST.delete_one({'_id': item.get("_id")})
                self.mccm_settings.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)
                # Remove doors from array "OutputList" of "connectionList"
                for outList in GV.DB_CONNECTIONLIST.find({}):
                    GV.DB_CONNECTIONLIST.update({"_id": outList['_id']},
                                                {"$pull": {"outputList": {"name": item.get("name")}}},
                                                upsert=True)

        GV.DOOR_NUMBER = int(self.ssc_handles_num_ti.text)
        with open(GV.DIR_JSON + GV.FILE_HANDLES, 'r') as file_handles:
            file_data = json.load(file_handles)
        file_data['door_number'] = int(self.ssc_handles_num_ti.text)
        with open(GV.DIR_JSON + GV.FILE_HANDLES, 'w') as file_handles:
            json.dump(file_data, file_handles, indent=4)
        self.ssc_handles_num.text = str(GV.DOOR_NUMBER)

        msg_color = 'success'
        msg_text = 'Update HANDLES collection'
        self.parent.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
        self.parent.remove_widget(loader)

    def go_to_modulescreen(self):
        self.mccm_settings.mccm.switch_to(self.mccm_settings.mccm.mccm_module)

    def go_to_objectscreen(self):
        self.mccm_settings.mccm.switch_to(self.mccm_settings.mccm.mccm_object)


# ----- Add Button Class --------------------------------------------------------------------------------------------- #
class AddSettingsBtn(Button):
    ref = ObjectProperty(None, allownone=True)

    def add_plc_zona(self):
        if self.ssc_plc_zona_ti.disabled:
            self.ssc_plc_zona_ti.disabled = False
            self.ssc_plc_zona_ip_ti.disabled = False
            self.ssc_plc_zona_com_ti.disabled = False
            self.ssc_plc_zona_info_ti.disabled = False
            self.ssc_plc_zona_info_ti.text = ''
            self.ssc_plc_zona_ti.text = ''
            self.ssc_plc_zona_ip_ti.text = ''
            self.ssc_plc_zona_com_ti.text = ''
        else:
            if self.ssc_plc_zona_ti.text != '':
                if 1 <= int(self.ssc_plc_zona_ip_ti.text) < 255:
                    if int(self.ssc_plc_zona_ip_ti.text) != int(GV.PLC_MASTER[-3:]):
                        if GV.DB_PLCZONECONFIG.find({}).count() == 0:
                            found = False
                        else:
                            for item in GV.DB_PLCZONECONFIG.find({}):
                                if item['address'] != int(self.ssc_plc_zona_ip_ti.text):
                                    found = False
                                else:
                                    found = True
                                    break
                        if not found:
                            if 0 < int(self.ssc_plc_zona_com_ti.text) < 65:
                                self.ssc_plc_zona_ti.disabled = True
                                self.ssc_plc_zona_ip_ti.disabled = True
                                self.ssc_plc_zona_com_ti.disabled = True
                                self.insert_plczona()

    def insert_plczona(self):
        GV.DB_PLCZONECONFIG.insert_one({'name': self.ssc_plc_zona_ti.text,
                                        'address': int(self.ssc_plc_zona_ip_ti.text),
                                        'ComPort': int(self.ssc_plc_zona_com_ti.text),
                                        'info': self.ssc_plc_zona_info_ti.text})
        GV.DB_OBJECTLIST.insert_one({'system': 'PLCZ',
                                     'address': int(self.ssc_plc_zona_ip_ti.text),
                                     'name': self.ssc_plc_zona_ti.text,
                                     'deck': GV.OBJ_DEFAULT_DK,
                                     'posX': 0,
                                     'posY': 0,
                                     'rotate': 0,
                                     'status': ''})
        self.mccm_settings.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)

        self.ssc_plc_zona_ti.text = ''
        self.ssc_plc_zona_ip_ti.text = ''
        self.ssc_plc_zona_com_ti.text = ''
        self.ssc_plc_zona_info_ti.text = ''
        self.ssc_plc_zona_ti.disabled = True
        self.ssc_plc_zona_ip_ti.disabled = True
        self.ssc_plc_zona_com_ti.disabled = True
        self.ssc_plc_zona_info_ti.disabled = True
        self.ss_container.update_plc_zona()

    def add_input(self):
        if not self.ref:
            if self.ssc_input_system.disabled:
                self.ssc_input_container.enable_input_zone()
            else:
                if self.ssc_input_system.text != 'System...':
                    if self.ssc_input_reg_type.text != 'Reg Bit...':
                        if 30000 < int(self.ssc_input_reg_start.text) < 50000:
                            if 0 < int(self.ssc_input_reg_quantity.text) < 10000:
                                GV.DB_INPUTCONFIG.insert_one({'name': self.ssc_input_system.text,
                                                              'registerStart': int(self.ssc_input_reg_start.text),
                                                              'registerNumber': int(self.ssc_input_reg_quantity.text),
                                                              'registerType': int(self.ssc_input_reg_type.text)})
                                for item in range(0, int(self.ssc_input_reg_quantity.text)):
                                    register = int(self.ssc_input_reg_start.text) + item
                                    bit = int(self.ssc_input_reg_type.text)
                                    system = self.ssc_input_system.text
                                    name = self.ssc_input_system.text + '_' + str(register)
                                    GV.DB_INPUTLIST.insert_one({'register': register,
                                                                'bit': bit,
                                                                'system': system,
                                                                'name': name,
                                                                'description': ''})
                                self.ssc_input_container.disable_input_zone()
                                self.ssc_input_container.init_container()
                                msg_color = 'success'
                                msg_text = 'Add INPUT system success'
                                self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)
                            else:
                                msg_color = 'error'
                                msg_text = 'Quantity Register wrong'
                                self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)
                        else:
                            msg_color = 'error'
                            msg_text = 'Input Register start wrong'
                            self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)
                    else:
                        msg_color = 'error'
                        msg_text = 'Register BIT missing'
                        self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)
                else:
                    msg_color = 'error'
                    msg_text = 'System not select'
                    self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)
        else:
            GV.DB_INPUTCONFIG.update_one({'_id': self.ref['_id']},
                                         {'$set': {'name': self.ssc_input_system.text,
                                                   'registerStart': int(self.ssc_input_reg_start.text),
                                                   'registerNumber': int(self.ssc_input_reg_quantity.text),
                                                   'registerType': int(self.ssc_input_reg_type.text)}})
            self.ssc_input_container.disable_input_zone()
            self.ssc_input_container.init_container()
            msg_color = 'success'
            msg_text = 'Update INPUT system success'
            self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)


# ----- Del Button Class --------------------------------------------------------------------------------------------- #
class DelSettingsBtn(Button):
    ref = ObjectProperty(None, allownone=True)

    def del_plc_zona(self):
        GV.DB_PLCZONECONFIG.delete_one({'_id': ObjectId(self.ssc_plc_zona_id_ti.text)})
        GV.DB_OBJECTLIST.delete_one({'name': self.ssc_plc_zona_ti.text})
        self.mccm_settings.mccm.mccm_dash.dsc_deck_scatter.init_obj(None)

        self.ssc_plc_zona_ti.text = ''
        self.ssc_plc_zona_ip_ti.text = ''
        self.ssc_plc_zona_com_ti.text = ''
        self.ssc_plc_zona_id_ti.text = ''
        self.ss_container.update_plc_zona()


# ----- Container Input Settings ------------------------------------------------------------------------------------- #
class InputContainerSettings(StackLayout):

    def __init__(self, **kwargs):
        super(InputContainerSettings, self).__init__(**kwargs)
        self.input_list_config = []
        self.layout = None
        self.input_label = None
        self.button_edit = None

    def populate_input(self):
        self.input_list_config = GV.DB_INPUTCONFIG.find({})
        for item in self.input_list_config:
            self.layout = RelativeLayout(size_hint=(1, None), height=20)
            self.input_label = InputLabelSettings(id=item, text=item['name'], pos=(0, 0))
            self.layout.add_widget(self.input_label)
            self.input_label = InputLabelSettings(id=item, text=str(item['registerStart']),
                                                  pos=(180, 0))
            self.layout.add_widget(self.input_label)
            self.input_label = InputLabelSettings(id=item, text=str(item['registerNumber']),
                                                  pos=(360, 0))
            self.layout.add_widget(self.input_label)
            self.input_label = InputLabelSettings(id=item, text=str(item['registerType']),
                                                  pos=(540, 0))
            self.layout.add_widget(self.input_label)
            self.input_label = InputLabelSettings(id=item, text=str(item['registerType']),
                                                  pos=(540, 0))
            self.layout.add_widget(self.input_label)
            # self.button_edit = EditSettingsBtn(ref=item, pos=(710, 0))
            # self.button_edit.bind(on_press=self.edit_input)
            # self.layout.add_widget(self.button_edit)
            self.button_edit = DelSettingsBtn(ref=item, pos=(760, 0))
            self.button_edit.bind(on_press=self.del_input)
            self.layout.add_widget(self.button_edit)
            self.add_widget(self.layout)

    def init_container(self):
        self.clear_widgets()
        self.populate_input()

    # def edit_input(self, instance):
    #     if self.ssc_input_system.disabled:
    #         self.enable_input_zone()
    #         self.ssc_input_system.text = instance.ref['name']
    #         self.ssc_input_reg_start.text = str(instance.ref['registerStart'])
    #         self.ssc_input_reg_quantity.text = str(instance.ref['registerNumber'])
    #         self.ssc_input_reg_type.text = str(instance.ref['registerType'])
    #         self.ssc_input_add_btn.ref = instance.ref
    #     else:
    #         if self.ssc_input_add_btn.ref == instance.ref:
    #             self.disable_input_zone()
    #             print('edit', instance.ref)
    #         else:
    #             self.ssc_input_system.text = instance.ref['name']
    #             self.ssc_input_reg_start.text = str(instance.ref['registerStart'])
    #             self.ssc_input_reg_quantity.text = str(instance.ref['registerNumber'])
    #             self.ssc_input_reg_type.text = str(instance.ref['registerType'])
    #             self.ssc_input_add_btn.ref = instance.ref

    def del_input(self, instance):
        GV.DB_INPUTCONFIG.delete_one({'_id': instance.ref['_id']})
        GV.DB_CONNECTIONLIST.delete_many({'system_input': instance.ref['name']})
        GV.DB_MODULECONFIG.delete_many({'system': instance.ref['name']})
        GV.DB_INPUTLIST.delete_many({'system': instance.ref['name']})
        self.init_container()
        msg_color = 'success'
        msg_text = 'Delete INPUT system success'
        self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)

    def enable_input_zone(self):
        self.ssc_input_system.disabled = False
        self.ssc_input_reg_start.disabled = False
        self.ssc_input_reg_quantity.disabled = False
        self.ssc_input_reg_type.disabled = False
        self.ssc_input_system.opacity = 1
        self.ssc_input_reg_start.opacity = 1
        self.ssc_input_reg_quantity.opacity = 1
        self.ssc_input_reg_type.opacity = 1

    def disable_input_zone(self):
        self.ssc_input_system.disabled = True
        self.ssc_input_reg_start.disabled = True
        self.ssc_input_reg_quantity.disabled = True
        self.ssc_input_reg_type.disabled = True
        self.ssc_input_system.opacity = 0
        self.ssc_input_reg_start.opacity = 0
        self.ssc_input_reg_quantity.opacity = 0
        self.ssc_input_reg_type.opacity = 0
        self.ssc_input_system.text = 'System...'
        self.ssc_input_reg_start.text = ''
        self.ssc_input_reg_quantity.text = ''
        self.ssc_input_reg_type.text = 'Reg Bit...'
        self.ssc_input_add_btn.ref = None


# ----- Input Label Settings ----------------------------------------------------------------------------------------- #
class InputLabelSettings(Label):
    id = ObjectProperty(None)


# ----- Spinner Voice ------------------------------------------------------------------------------------------------ #
class VoiceSpinner(Spinner):

    def __init__(self, **kwargs):
        super(VoiceSpinner, self).__init__(**kwargs)
        self.option_cls = VoiceSpinnerOption


class VoiceSpinnerOption(SpinnerOption):
    pass


# ----- Logger button ------------------------------------------------------------------------------------------------ #
class LoggerButton(Button):

    def logger_active(self):
        active = GV.LOGGER_ACTIVE
        if active:
            GV.LOGGER_ACTIVE = False
            self.mccm_settings.mccm.mm_logger.text = 'Logger disabled'
            self.mccm_settings.mccm.mm_logger.color = GV.RGBA_ERROR
            self.text = 'OFF'
        else:
            GV.LOGGER_ACTIVE = True
            self.mccm_settings.mccm.mm_logger.text = 'Logger enabled'
            self.mccm_settings.mccm.mm_logger.color = GV.RGBA_SUCCESS
            self.text = 'ON'

    def logger_clear(self):
        GV.DB_LOGGER.drop()
        msg_color = 'success'
        msg_text = 'Clear Logger success'
        self.mccm_settings.mccm.mm_notification.notification_msg(msg_color, msg_text)


# ----- Export file device ------------------------------------------------------------------------------------------- #
class ExportDeviceButton (Button):

    def select_device(self):
        if self.text == 'USB':
            GV.EXPORT_DEVICE = 'DESKTOP'
            self.text = 'DESKTOP'
            return
        if self.text == 'DESKTOP':
            GV.EXPORT_DEVICE = 'USB'
            self.text = 'USB'
            return

# ----- Commissioning documentation button --------------------------------------------------------------------------- #

