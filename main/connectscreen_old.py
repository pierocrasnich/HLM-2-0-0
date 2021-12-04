from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.modalview import ModalView
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
import utility.gvar as GV

Builder.load_file('main/classi/connect.kv')


# ----- Classe generale del layout ----------------------------------------------------------------------------------- #
class ConnectScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.cs_container.csc_input_list.get_list(system='ALL')

    def on_enter(self, *args):
        self.cs_container.csc_module_library.init_data()

    def on_pre_leave(self, *args):
        self.cs_container.csc_input_list.clear_input()


class ConnectContainer(RelativeLayout):

    def close_module_preview(self):
        self.csc_module_preview.disabled = True
        self.csc_module_preview.opacity = 0


# ----- Pulsante del modello all'interno della zona libreria --------------------------------------------------------- #
class ModuleLibraryButton(Button):
    pass


# ----- Marker del colore e del testo sulla mappa delle maniglie FUNCTION SX e DX ------------------------------------ #
class MapMarker(BoxLayout):
    color_bk = ListProperty([0, 0, 0, 0])


class LabelMarker(Label):
    pass


# ----- Contenitore della libreria dei moduli ------------------------------------------------------------------------ #
class ModuleLibraryContainer(StackLayout):

    def __init__(self, **kwargs):
        super(ModuleLibraryContainer, self).__init__(**kwargs)

    def init_data(self):
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
            btn.text = data['name']
            btn.data = data
            btn.bind(on_press=self.show_map)
            self.add_widget(btn)


# ----- Casella di selezione tipologia degli input ------------------------------------------------------------------- #
class SelectSystemInput(Spinner):

    def __init__(self, **kwargs):
        super(SelectSystemInput, self).__init__(**kwargs)
        self.option_cls = SelectSystemInputOption

    def selected_system(self, text):
        self.csc_input_list.init_input(text)


# ----- Classe per gestione dei bottoni dello spinner di selezione --------------------------------------------------- #
class SelectSystemInputOption(SpinnerOption):
    pass


# ----- Layout con la lista degli input ------------------------------------------------------------------------------ #
class InputListBox(GridLayout):

    def update_list(self, system, input_select=''):
        self.list_input.clear()
        self.input_selected = ''
        self.clear_widgets()
        self.system = system
        self.get_list(systems=system)
        if input_select != '':
            self.input_selected = input_select
            self.list_input.append(input_select)
            for child in self.children:
                if child.text == input_select:
                    child.state = 'down'
        self.csc_add_module_btn.disabled = True
        self.csc_add_module_btn.opacity = 0
        self.csc_del_module_btn.disabled = True
        self.csc_del_module_btn.opacity = 0
        self.csc_add_output_btn.disabled = True
        self.csc_add_output_btn.opacity = 0
        self.csc_del_output_btn.disabled = True
        self.csc_del_output_btn.opacity = 0

    def update_list_with_select(self, system, input_select):
        self.list_input.clear()
        self.list_input.append(input_select)
        self.clear_widgets()
        self.system = system
        self.get_list(system=system)
        for child in self.children:
            if child.text == input_select:
                child.state = 'down'

    def get_list(self, system):
        if system == 'ALL':
            sys_values = GV.DB_INPUTLIST.find({})
        else:
            sys_values = GV.DB_INPUTLIST.find({'system': system})
        for item in sys_values:
            if item['name'] != '':
                if GV.DB_CONNECTIONLIST.find({'inputID': item['_id']}).count() > 0:
                    input_button = InputButton(text=(item['name'] + ' : ' + item['description']),
                                               color=GV.RGBA_SUCCESS,
                                               ilb=self,
                                               input_obj=item)
                else:
                    input_button = InputButton(text=(item['name'] + ' : ' + item['description']),
                                               ilb=self,
                                               input_obj=item)
                self.add_widget(input_button)

    def init_input(self, system):
        self.clear_input()
        self.get_list(system)

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
        if self.state == 'normal':
            self.ilb.csc_module_list.list_module.clear()
            self.ilb.csc_add_module_btn.disabled = True
            self.ilb.csc_add_module_btn.opacity = 0
            self.ilb.csc_module_list.input_obj = None
        else:
            self.ilb.csc_add_module_btn.disabled = False
            self.ilb.csc_add_module_btn.opacity = 1
            self.ilb.csc_module_list.input_obj = self.input_obj
            self.ilb.csc_module_list.connected_module()


# ----- Layout con la lista dei moduli selezionati ------------------------------------------------------------------- #
class ModuleListBox(GridLayout):
    input_obj = ObjectProperty(None, allownone=True)
    list_module = []
    module_selected = ''

    def __init__(self, **kwargs):
        super(ModuleListBox, self).__init__(**kwargs)
        self.module_popup = None

    def add_module(self):
        self.module_popup = ModulePopup(mlb=self, input_obj=self.input_obj)
        self.module_popup.open()

    def update_module(self):
        self.clear_widgets()
        for item in self.list_module:
            module_button = ModuleButton(text=item['name'], group='module', mlb=self, module_obj=item,
                                         input_obj=self.input_obj)
            self.add_widget(module_button)
        if len(self.module_selected) == 0 or len(self.list_module) == 0:
            self.csc_del_module_btn.disabled = True
            self.csc_del_module_btn.opacity = 0
        else:
            self.csc_del_module_btn.disabled = False
            self.csc_del_module_btn.opacity = 1

    def clear_module(self):
        self.list_module = []
        self.module_selected = ''
        self.clear_widgets()

    def connected_module(self):
        if GV.DB_CONNECTIONLIST.find({'inputID': self.input_obj['_id']}).count() > 0:
            for item in GV.DB_CONNECTIONLIST.find({'inputID': self.input_obj['_id']}):
                for module in GV.DB_MODULECONFIG.find({'_id': item['moduleID']}):
                    self.list_module.append(module)
            self.update_module()

    def init_module(self):
        self.clear_widgets()
        self.module_selected = ''
        self.list_module.clear()
        self.csc_add_module_btn.disabled = True
        self.csc_add_module_btn.opacity = 0


# ----- Popup per la selezione dei moduli ---------------------------------------------------------------------------- #
class ModulePopup(Popup):
    list_from_popup = []
    mlb = ObjectProperty(None)
    input_obj = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(ModulePopup, self).__init__(**kwargs)
        module_query = GV.DB_MODULECONFIG.find({'system': self.input_obj['system'], 'bit': int(self.input_obj['bit'])})
        # self.list_from_popup.clear()

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
        self.mlb.update_module()


# ----- Classe con i pulsanti generati nel layout dei moduli selezionati --------------------------------------------- #
class ModuleButton(ToggleButton):
    mlb = ObjectProperty(None)
    input_obj = ObjectProperty(None, allownone=True)
    module_obj = ObjectProperty(None, allownone=True)

    def on_press(self):
        if self.state == 'normal':
            self.mlb.csc_del_module_btn.disabled = True
            self.mlb.csc_del_module_btn.opacity = 0
            self.mlb.csc_del_module_btn.obj = None
            self.mlb.csc_add_output_btn.disabled = True
            self.mlb.csc_add_output_btn.opacity = 0
            self.mlb.csc_confirm_btn.input_obj = None
            self.mlb.csc_confirm_btn.module_obj = None
        else:
            self.mlb.csc_del_module_btn.disabled = False
            self.mlb.csc_del_module_btn.opacity = 1
            self.mlb.csc_add_output_btn.disabled = False
            self.mlb.csc_add_output_btn.opacity = 1
            self.mlb.csc_del_module_btn.obj = self.module_obj
            self.mlb.csc_output_list.update_output()
            self.mlb.csc_confirm_btn.input_obj = self.input_obj
            self.mlb.csc_confirm_btn.module_obj = self.module_obj

    def output_connected_to_module(self, module):
        self.mlb.csc_output_list.output_connected = []
        collection = GV.DB['connection']
        connection = collection.find_one({'input': self.mlb.csc_input_list.input_selected, 'module': module})
        if connection:
            for item in connection['output']:
                self.mlb.csc_output_list.output_connected.append(item)
            self.mlb.csc_output_list.output_connected_with_module()


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


# ----- Layout con la lista degli output selezionti ------------------------------------------------------------------ #
class OutputListBox(GridLayout):
    list_output = []

    def add_output(self):
        self.output_popup = OutputPopup(olb=self)
        self.output_popup.open()

    def update_output(self):
        self.clear_widgets()
        for output_obj in self.list_output:
            output_button = OutputButton(text=output_obj['name'], olb=self, output_obj=output_obj,  group='output')
            self.add_widget(output_button)
        if self.list_output:
            self.csc_confirm_btn.disabled = False
        else:
            self.csc_confirm_btn.disabled = True

    def clear_output(self):
        self.list_output = []
        self.clear_widgets()

    def write_notification(self, color, msg):
        self.mccm_connect.mccm.mm_notification.color = color
        self.mccm_connect.mccm.mm_notification.text = msg
        Clock.schedule_once(self.hide_notification_text, 5)

    def hide_notification_text(self, dt):
        self.mccm_connect.mccm.mm_notification.text = ''

    def output_connected_with_module(self):
        if self.list_output == []:
            self.list_output = self.output_connected.copy()
        else:
            self.list_output += self.output_connected
        self.output_connected.clear()
        self.update_output()

    def init_output(self):
        self.clear_widgets()
        self.output_connected.clear()
        self.list_output.clear()


# ----- Popup per la selezione degli output -------------------------------------------------------------------------- #
class OutputPopup(Popup):
    olb = ObjectProperty(None)
    list_from_popup = []

    def __init__(self, **kwargs):
        super(OutputPopup, self).__init__(**kwargs)
        self.list_from_popup.clear()
        for output_obj in GV.DB_OUTPUTLIST.find({}):
            if output_obj not in self.olb.list_output:
                output_button = OutputPopupButton(text=output_obj['name'], popup=self, output_obj=output_obj)
                self.output_list.add_widget(output_button)

    def adding_output_to_list(self):
        for item in self.list_from_popup:
            if item not in self.olb.list_output:
                self.olb.list_output.append(item)
        self.olb.update_output()


# ----- Pulsanti generati nel layout degli output -------------------------------------------------------------------- #
class OutputButton(ToggleButton):
    output_obj = ObjectProperty(None, allownone=True)
    olb = ObjectProperty(None)

    def on_press(self):
        if self.state == 'normal':
            self.olb.csc_del_output_btn.disabled = True
            self.olb.csc_del_output_btn.opacity = 0
            self.olb.csc_del_output_btn.obj = None
        else:
            self.olb.csc_del_output_btn.disabled = False
            self.olb.csc_del_output_btn.opacity = 1
            self.olb.csc_del_output_btn.obj = self.output_obj


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


# ----- DEL and ADD Button Class ------------------------------------------------------------------------------------- #
class AddButton(Button):
    input_obj = ObjectProperty(None, allownone=True)
    module_obj = ObjectProperty(None, allownone=True)

    def confirm_connection(self):
        if self.input_obj and self.module_obj and self.csc_output_list.list_output:
            if GV.DB_CONNECTIONLIST.find({'inputID': self.input_obj['_id'], 'moduleID': self.module_obj['_id']}).count() > 0:
                #GV.DB_CONNECTIONLIST.update_one({'inputID': self.input_obj['_id'], 'moduleID': self.module_obj['_id']}, "$set": {'outputList': self.csc_output_list.list_output})
                pass
            else:
                GV.DB_CONNECTIONLIST.insert_one({'inputID': self.input_obj['_id'],
                                                 'moduleID': self.module_obj['_id'],
                                                 'outputList': self.csc_output_list.list_output})


class DelButton(Button):
    obj = ObjectProperty(None, allownone=True)

    def delete_output(self):
        if self.obj is not None:
            self.csc_output_list.list_output.remove(self.obj)
        self.csc_output_list.update_output()
        self.csc_output_list.write_notification(color=GV.RGBA_ERROR, msg='Output Deleted !!!')
        self.clear_btn()

    def clear_btn(self):
        self.disabled = True
        self.opacity = 0
        self.obj = None

    def delete_module(self):
        if self.obj is not None:
            self.csc_module_list.list_module.remove(self.obj)
        self.csc_module_list.update_module()
        self.csc_module_list.csc_output_list.write_notification(color=GV.RGBA_ERROR, msg='Module Deleted !!!')
        self.clear_btn()