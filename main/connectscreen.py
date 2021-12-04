from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex

from kivy.clock import Clock
from classi.csv import ExportConnectButton, ImportConnectButton, ImportDialog
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from bson.objectid import ObjectId
from pymongo import ASCENDING
import random
from operator import attrgetter
import utility.gvar as GV

# -- Caricamento Widget per li download PLC ZONA configuration ------------------------------------------------------- #
Builder.load_file('classi/downloadPLC.kv')
from classi.downloadPLC import DownloadPLC

Builder.load_file('main/classi/connect.kv')


# ----- Classe generale del layout ----------------------------------------------------------------------------------- #
class ConnectScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.cs_container.cscisb_system.populate_values()
        self.cs_container.csc_input_list.init_input(system='ALL')

    def on_enter(self, *args):
        self.cs_container.csc_module_library.init_data()
        self.cs_container.csc_module_list.clear_module()
        self.cs_container.csc_output_list.clear_output()

        for input_btn in self.cs_container.csc_input_list.children:
            if input_btn.state == 'down':
                input_btn.state = 'normal'


class ConnectContainer(RelativeLayout):

    def close_module_preview(self):
        self.csc_module_preview.disabled = True
        self.csc_module_preview.opacity = 0

    def download_btn(self):
        download_widget = DownloadPLC()
        download_widget.obj = self.parent
        download_widget.start_download()
        self.add_widget(download_widget)


# ----- Pulsante del modello all'interno della zona libreria --------------------------------------------------------- #
class ModuleLibraryButton(Button):
    color_normal = ListProperty([1, 1, 1, 0])
    color_down = ListProperty([1, 1, 1, 0])
    color_border = ListProperty([1, 1, 1, 0])

    def __init__(self, **kwargs):
        super(ModuleLibraryButton, self).__init__(**kwargs)
        self.color_normal = GV.RGBA_MOD_NORM
        self.color_down = GV.RGBA_MOD_DOWN
        self.color_border = GV.RGBA_MOD_BORDER


# ----- Marker del colore e del testo sulla mappa delle maniglie FUNCTION SX e DX ------------------------------------ #
class MapMarker(BoxLayout):
    color_bk = ListProperty([0, 0, 0, 0])


class LabelMarker(Label):
    pass


# ----- Contenitore della libreria dei moduli ------------------------------------------------------------------------ #
class ModuleLibraryContainer(StackLayout):

    def __init__(self, **kwargs):
        super(ModuleLibraryContainer, self).__init__(**kwargs)
        self.color_system = []

    def init_data(self):
        # create system color
        # for system in GV.DB_MODULECONFIG.distinct('system'):
        #     col1 = round(random.uniform(0, 1), 2)
        #     col2 = round(random.uniform(0, 1), 2)
        #     col3 = round(random.uniform(0, 1), 2)
        #     color_data = {system: {col1, col2, col3}}
        #     self.color_system.append(color_data)
        # for ele in self.color_system:
        #     print(ele)
        self.refresh_data()

    def show_map(self, instance):
        self.csc_module_export.module_select = instance.data['name']  # Send module ID to PDF btn
        self.csc_module_preview.cscmp_map_func.clear_widgets()
        self.csc_module_preview.cscmp_map_out_sx.clear_widgets()
        self.csc_module_preview.cscmp_map_out_dx.clear_widgets()
        self.csc_module_preview.disabled = False
        self.csc_module_preview.opacity = 1
        self.csc_module_preview.cscmp_name.text = 'Name: ' + instance.data['name']
        self.csc_module_preview.cscmp_system.text = 'System: ' + instance.data['system']
        self.csc_module_preview.cscmp_bit.text = 'BIT: ' + str(instance.data['bit'])

        self.csc_module_preview.cscmp_map_func.add_widget(LabelMarker(text='NORMAL'))

        normal_status_sx = instance.data['normal']['SX'][1:7]
        normal_status_dx = instance.data['normal']['DX'][1:7]
        if normal_status_sx == '000000':
            self.csc_module_preview.cscmp_map_out_sx.add_widget(LabelMarker(text='OFF'))
        else:
            marker_normal_sx = MapMarker()
            marker_normal_sx.color_bk = get_color_from_hex(normal_status_sx)
            self.csc_module_preview.cscmp_map_out_sx.add_widget(marker_normal_sx)

        if normal_status_dx == '000000':
            self.csc_module_preview.cscmp_map_out_dx.add_widget(LabelMarker(text='OFF'))
        else:
            marker_normal_dx = MapMarker()
            marker_normal_dx.color_bk = get_color_from_hex(normal_status_sx)
            self.csc_module_preview.cscmp_map_out_dx.add_widget(marker_normal_dx)

        for bit in instance.data['rules']:
            function = bit['function']

            if function:
                colorSX = bit['SX'][1:7]
                colorDX = bit['DX'][1:7]
                markerSX = MapMarker()
                markerDX = MapMarker()
                map_func_text = bit['function'] + ' (bit  ' + str(bit['bit']) + ')'
                self.csc_module_preview.cscmp_map_func.add_widget(LabelMarker(text=map_func_text))

                if colorSX:
                    if colorSX == '000000':
                        self.csc_module_preview.cscmp_map_out_sx.add_widget(LabelMarker(text='OFF'))
                    else:

                        markerSX.color_bk = get_color_from_hex(colorSX)
                        self.csc_module_preview.cscmp_map_out_sx.add_widget(markerSX)
                if colorDX:
                    if colorDX == '000000':
                        self.csc_module_preview.cscmp_map_out_dx.add_widget(LabelMarker(text='OFF'))
                    else:
                        markerDX.color_bk = get_color_from_hex(colorDX)
                        self.csc_module_preview.cscmp_map_out_dx.add_widget(markerDX)

    def refresh_data(self):
        result_module = GV.DB_MODULECONFIG.find({})
        self.clear_widgets()

        for data in result_module:
            btn = ModuleLibraryButton()
            # btn.color_normal = [.02, .5, .4, .03]
            # btn.color_down = [.02, .5, .4, .04]
            # btn.color_border = [.02, .5, .4, 1]
            btn.text = data['name']
            btn.data = data
            btn.bind(on_press=self.show_map)
            self.add_widget(btn)


# ----- Casella di selezione tipologia degli input ------------------------------------------------------------------- #
class SelectSystemInput(Spinner):

    def __init__(self, **kwargs):
        super(SelectSystemInput, self).__init__(**kwargs)
        self.option_cls = SelectSystemInputOption

    def populate_values(self):
        list_system = GV.DB_INPUTLIST.distinct('system')
        list_system.insert(0, 'ALL')
        self.values = list_system

    def selected_system(self, text):
        self.csc_input_list.init_input(text)
        self.csc_module_list.clear_module()
        self.csc_output_list.clear_output()


# ----- Classe per gestione dei bottoni dello spinner di selezione --------------------------------------------------- #
class SelectSystemInputOption(SpinnerOption):
    pass


# ----- Layout con la lista degli input ------------------------------------------------------------------------------ #
class InputListBox(GridLayout):
    input_selected = []
    connect_count_N = NumericProperty()

    def init_input(self, system):
        self.clear_input()
        self.get_list(system)

    def get_list(self, system):
        self.connect_count_N = 0
        if system == 'ALL':
            sys_values = GV.DB_INPUTLIST.find({}).sort('name', ASCENDING)
        else:
            sys_values = GV.DB_INPUTLIST.find({'system': system}).sort('name', ASCENDING)

        count = 0
        for count, item in enumerate(sys_values):
            if item['name'] != '':
                if GV.DB_CONNECTIONLIST.find({'inputID': item['_id']}).count() > 0:
                    input_button = InputButton(
                        text=(item['name'] + ' : ' + item['description']),
                        color=GV.RGBA_SUCCESS,
                        ilb=self,
                        input_obj=item)
                    self.connect_count_N += 1
                else:
                    input_button = InputButton(
                        text=(item['name'] + ' : ' + item['description']),
                        color=GV.RGBA_BLACK,
                        ilb=self,
                        input_obj=item)
                input_button.id = item['_id']
                self.add_widget(input_button)

        msg = 'Connect ' + str(self.connect_count_N) + '/' + str(count + 1) + ' of ' + str(system) + ' system'
        self.csc_connections_count.text = msg

    def clear_input(self):
        self.clear_widgets()
        self.csc_add_module_btn.disabled = True
        self.csc_add_module_btn.opacity = 0


# ----- Classe dei pulsanti generati all'interno del box lista input ------------------------------------------------- #
class InputButton(ToggleButton):
    input_obj = ObjectProperty(None)
    ilb = ObjectProperty(None)

    def on_press(self):
        self.ilb.csc_module_list.clear_module()
        self.ilb.csc_output_list.clear_output()
        if self.state == 'normal':
            self.ilb.csc_add_module_btn.disabled = True
            self.ilb.csc_add_module_btn.opacity = 0
            self.ilb.csc_module_list.input_obj = None
            self.parent.input_selected = []
            system = self.ilb.cscisb_system.text
            self.parent.init_input(system)
        else:
            self.ilb.csc_add_module_btn.disabled = False
            self.ilb.csc_add_module_btn.opacity = 1
            self.ilb.csc_module_list.input_obj = self.input_obj
            self.parent.input_selected = self.input_obj
            self.ilb.csc_module_list.connected_module()


# ----- Layout con la lista dei moduli selezionati ------------------------------------------------------------------- #
class ModuleListBox(GridLayout):
    input_obj = ObjectProperty(None, allownone=True)
    list_module = []
    module_selected = ''

    def __init__(self, **kwargs):
        super(ModuleListBox, self).__init__(**kwargs)
        self.module_popup = None

    def connected_module(self):
        if GV.DB_CONNECTIONLIST.find({'inputID': self.input_obj['_id']}).count() > 0:
            for item in GV.DB_CONNECTIONLIST.find({'inputID': self.input_obj['_id']}):
                for module in GV.DB_MODULECONFIG.find({'_id': item['moduleID']}):
                    self.list_module.append(module)
        else:
            self.list_module = []
        self.update_module()

    def update_module(self):
        self.clear_widgets()
        self.csc_output_list.clear_output()
        for item in self.list_module:
            module_button = ModuleButton(text=item['name'],
                                         group='module',
                                         mlb=self,
                                         module_obj=item,
                                         input_obj=self.input_obj)
            self.add_widget(module_button)

            if item['_id'] == self.module_selected:
                module_button.output_connected_to_module(self.module_selected)
                module_button.state = 'down'
                self.csc_add_output_btn.disabled = False
                self.csc_add_output_btn.opacity = 1

    def add_module(self):
        self.module_popup = ModulePopup(mlb=self, input_obj=self.input_obj)
        self.module_popup.open()

    def clear_module(self):
        self.list_module = []
        self.module_selected = ''
        self.csc_del_module_btn.disabled = True
        self.csc_del_module_btn.opacity = 0
        self.csc_add_module_btn.disabled = True
        self.csc_add_module_btn.opacity = 0
        self.clear_widgets()


# ----- Classe con i pulsanti generati nel layout dei moduli selezionati --------------------------------------------- #
class ModuleButton(ToggleButton):
    mlb = ObjectProperty(None)
    input_obj = ObjectProperty(None, allownone=True)
    module_obj = ObjectProperty(None, allownone=True)

    def on_press(self):
        self.mlb.csc_output_list.clear_output()
        if self.state == 'normal':
            self.mlb.csc_del_module_btn.disabled = True
            self.mlb.csc_del_module_btn.opacity = 0
            self.mlb.csc_del_module_btn.module_obj = None
            self.mlb.csc_add_output_btn.disabled = True
            self.mlb.csc_add_output_btn.opacity = 0
        else:
            self.mlb.csc_del_module_btn.disabled = False
            self.mlb.csc_del_module_btn.opacity = 1
            self.mlb.csc_add_output_btn.disabled = False
            self.mlb.csc_add_output_btn.opacity = 1
            self.mlb.csc_del_module_btn.module_obj = self.module_obj
            self.output_connected_to_module(ObjectId(self.module_obj['_id']))
            self.mlb.module_selected = ObjectId(self.module_obj['_id'])

    def output_connected_to_module(self, module):
        self.mlb.csc_output_list.output_connected = []
        input_select = ObjectId(str(self.mlb.csc_input_list.input_selected['_id']))
        collection = GV.DB_CONNECTIONLIST
        connection = collection.find_one({'inputID': input_select, 'moduleID': module})
        if connection:
            for item in connection['outputList']:
                self.mlb.csc_output_list.list_output.append(item)
            self.mlb.csc_output_list.update_output()


# ----- Layout con la lista degli output selezionti ------------------------------------------------------------------ #
class OutputListBox(GridLayout):
    list_output = []
    output_popup = ObjectProperty()

    def update_output(self):
        self.clear_widgets()
        for output_obj in self.list_output:
            output_button = OutputButton(text=output_obj['name'], olb=self, output_obj=output_obj)
            self.add_widget(output_button)

    def add_output(self):
        self.output_popup = OutputPopup(olb=self)
        self.output_popup.open()

    def clear_output(self):
        self.list_output = []
        self.csc_add_output_btn.disabled = True
        self.csc_add_output_btn.opacity = 0
        self.csc_del_output_btn.disabled = True
        self.csc_del_output_btn.opacity = 0
        self.clear_widgets()

    def save_connection(self):
        system = self.csc_input_list.input_selected['system']
        input_select = ObjectId(str(self.csc_input_list.input_selected['_id']))
        module_select = self.csc_module_list.module_selected
        query = {'system_input': system, 'inputID': input_select, 'moduleID': module_select}
        new_set = {"$set": {'outputList': self.list_output}, }

        for input_btn_select in self.csc_input_list.children:
            if input_btn_select.id == input_select:
                input_btn_select.color = GV.RGBA_SUCCESS

        if input_select and module_select:
            if self.list_output:
                GV.DB_CONNECTIONLIST.update_one(query, new_set, upsert=True)
            else:
                GV.DB_CONNECTIONLIST.delete_one(query)
            # system = self.cscisb_system.text
            # self.csc_input_list.init_input(system)
            # self.csc_module_list.clear_module()
            # self.csc_output_list.clear_output()
            msg_color = 'success'
            msg_text = 'Input config connection'
            self.mccm_connect.mccm.mm_notification.notification_msg(msg_color, msg_text)


# ----- Pulsanti generati nel layout degli output -------------------------------------------------------------------- #
class OutputButton(ToggleButton):
    output_obj = ObjectProperty(None, allownone=True)
    olb = ObjectProperty(None)

    def on_press(self):
        if self.state == 'normal':
            self.olb.csc_del_output_btn.disabled = True
            self.olb.csc_del_output_btn.opacity = 0
            self.olb.csc_del_output_btn.obj = None
            self.olb.csc_del_output_btn.obj.remove(self.output_obj)
        else:
            self.olb.csc_del_output_btn.disabled = False
            self.olb.csc_del_output_btn.opacity = 1
            self.olb.csc_del_output_btn.obj.append(self.output_obj)


# ----- DEL and ADD Button Class ------------------------------------------------------------------------------------- #
class AddButton(Button):
    input_obj = ObjectProperty(None, allownone=True)
    module_obj = ObjectProperty(None, allownone=True)


class DelButton(Button):
    obj = ListProperty([])
    module_obj = ObjectProperty(None, allownone=True)

    def delete_module(self):
        input_select = ObjectId(str(self.csc_input_list.input_selected['_id']))
        if self.obj is not None:
            GV.DB_CONNECTIONLIST.delete_one({'inputID': input_select, 'moduleID':  ObjectId(self.module_obj['_id'])})
            self.csc_module_list.list_module.remove(self.module_obj)

        self.csc_module_list.update_module()

    def delete_output(self):
        if self.obj is not None:
            for item in list(self.obj):
                self.csc_output_list.list_output.remove(item)
        self.csc_output_list.update_output()
        self.csc_output_list.save_connection()
        self.clear_btn()

    def clear_btn(self):
        self.disabled = True
        self.opacity = 0
        self.obj = []


# ----- Popup per la selezione dei moduli ---------------------------------------------------------------------------- #
class ModulePopup(Popup):
    list_from_popup = []
    mlb = ObjectProperty(None)
    input_obj = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(ModulePopup, self).__init__(**kwargs)
        module_query = GV.DB_MODULECONFIG.find({'system': self.input_obj['system'], 'bit': int(self.input_obj['bit'])})
        self.list_from_popup = []

        if module_query.count() > 0:
            for item in module_query:

                if item not in self.mlb.list_module:
                    self.module_list.add_widget(ModulePopupButton(text=item['name'],
                                                                  popup=self,
                                                                  input_obj=self.input_obj,
                                                                  module_obj=item))

    def adding_module_to_list(self):
        for item in self.list_from_popup:
            if item not in self.mlb.list_module:
                self.mlb.list_module.append(item)
                self.mlb.module_selected = ObjectId(item['_id'])
        self.mlb.update_module()


# ----- Classe con i pulsanti generati nel popup di selezione dei moduli --------------------------------------------- #
class ModulePopupButton(ToggleButton):
    input_obj = ObjectProperty(None, allownone=True)
    module_obj = ObjectProperty(None, allownone=True)
    popup = ObjectProperty(None)

    def on_press(self):
        if self.state == 'normal':
            self.popup.list_from_popup.remove(self.module_obj)
        else:
            if self.module_obj not in self.popup.list_from_popup:
                self.popup.list_from_popup.append(self.module_obj)
        if len(self.popup.list_from_popup) == 0:
            self.popup.add_module_btn.disabled = True
        else:
            self.popup.add_module_btn.disabled = False


# ----- Popup per la selezione degli output -------------------------------------------------------------------------- #
class OutputPopup(Popup):
    olb = ObjectProperty(None)
    list_from_popup = []

    def __init__(self, **kwargs):
        super(OutputPopup, self).__init__(**kwargs)
        self.list_from_popup.clear()
        for output_obj in GV.DB_OUTPUTLIST.find({}).sort('name', ASCENDING):
            if output_obj['name'] != '' and output_obj['plc'] != '' and output_obj['port'] != '':
                if output_obj not in self.olb.list_output:
                    output_button = OutputPopupButton(text=output_obj['name'], popup=self, output_obj=output_obj)
                    self.output_list.add_widget(output_button)

    def adding_output_to_list(self):
        for item in self.list_from_popup:
            if item not in self.olb.list_output:
                self.olb.list_output.append(item)
        self.olb.update_output()
        self.olb.save_connection()


# ----- Pulsanti generati nel popup di selezione degli output -------------------------------------------------------- #
class OutputPopupButton(ToggleButton):
    output_obj = ObjectProperty(None, allownone=True)
    popup = ObjectProperty(None)

    def on_press(self):
        if self.state == 'normal':
            self.popup.list_from_popup.remove(self.output_obj)
        else:
            if self.output_obj not in self.popup.list_from_popup:
                self.popup.list_from_popup.append(self.output_obj)
        if len(self.popup.list_from_popup) == 0:
            self.popup.add_output_btn.disabled = True
        else:
            self.popup.add_output_btn.disabled = False
