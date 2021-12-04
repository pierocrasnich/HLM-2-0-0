from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from bson import ObjectId
import utility.gvar as GV
from classi.csv import ExportConnectButton, ImportConnectButton, ImportDialog
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from pymongo import ASCENDING, DESCENDING

# ----- Import Style widget file ------------------------------------------------------------------------------------- #
Builder.load_file('main/classi/input.kv')


# ----- Classe principale dello Screen INPUT ------------------------------------------------------------------------- #
class InputScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.is_container.isc_list_table.update_list(systems='ALL')
        self.is_container.iscc_system_spn.populate_values()

    def on_pre_leave(self, *args):
        self.is_container.isc_list_table.clear_list()


class InputContainer(RelativeLayout):

    def update_name(self):
        # validate form
        name_list = [item['name'] for item in GV.DB_INPUTLIST.find({}, {'name': 1})]

        if self.isc_edit_box.isceb_name.text == '':
            msg_color = 'error'
            msg_text = 'Missing name !!!'
            self.mccm_input.mccm.mm_notification.notification_msg(msg_color, msg_text)
            return

        if self.isc_edit_box.isceb_name.text != self.isc_edit_box.name_set:
            if self.isc_edit_box.isceb_name.text in name_list:
                msg_color = 'error'
                msg_text = 'Name just present!!!'
                self.mccm_input.mccm.mm_notification.notification_msg(msg_color, msg_text)
                return

        if GV.DB is not None:
            GV.DB_INPUTLIST.update_one({'_id': ObjectId(self.isc_edit_box.isceb_obj_id.text)},
                              {'$set': {'name': self.isc_edit_box.isceb_name.text, 'description': self.isc_edit_box.isceb_descr.text}})
            self.isc_edit_box.disabled = True
            self.isc_edit_box.opacity = 0
            msg_color = 'success'
            msg_text = 'Input ' + self.isc_edit_box.isceb_name.text + ' save !!!'
            self.mccm_input.mccm.mm_notification.notification_msg(msg_color, msg_text)
            self.isc_list_table.update_list(systems=self.isc_edit_box.isceb_sys.text)
            self.iscc_system_spn.text = self.isc_edit_box.isceb_sys.text

    def cancel_update(self):
        self.isc_edit_box.disabled = True
        self.isc_edit_box.opacity = 0


# ----- Contenitore della lista degli INPUT -------------------------------------------------------------------------- #
class ListInput(GridLayout):
    def __init__(self, **kwargs):
        super(ListInput, self).__init__(**kwargs)
        self.list_input = None
        self.layout = None

    def update_list(self, systems):
        self.clear_list()
        self.get_list(systems=systems)

    def clear_list(self):
        self.clear_widgets()

    def get_list(self, systems):
        if systems == 'ALL':
            self.list_input = GV.DB_INPUTLIST.find().sort('register', ASCENDING)
        else:
            self.list_input = GV.DB_INPUTLIST.find({'system': systems}).sort('register', ASCENDING)
        count_input = 1
        for input_item in self.list_input:
            self.layout = InputBoxRow()
            self.layout.id = str(input_item['_id'])
            self.layout.obj = str(count_input)
            self.layout.orientation = 'horizontal'
            self.layout.size_hint = (1, None)
            self.layout.height = 30
            self.layout.group = 'input'
            self.layout.add_widget(LabelInput(text=str(count_input), size=(50, 30), obj=str(input_item['_id'])))
            self.layout.add_widget(LabelInput(text=str(input_item['register']), size=(100, 30), obj=str(input_item['_id'])))
            self.layout.add_widget(LabelInput(text=str(input_item['bit']), size=(50, 30), obj=str(input_item['_id'])))
            self.layout.add_widget(LabelInput(text=str(input_item['system']), size=(150, 30), obj=str(input_item['_id'])))
            self.layout.add_widget(LabelInput(text=str(input_item['name']), size=(150, 30), obj=str(input_item['_id'])))
            self.layout.add_widget(LabelInput(text=str(input_item['description']), size=(600, 30), obj=str(input_item['_id'])))
            self.add_widget(self.layout)
            count_input += 1


# ----- Layout contenente lo spinner per la selezione SYSTEM degli INPUT --------------------------------------------- #
class SelectInputContainer(FloatLayout):
    pass


# ----- System Spinner and class option ------------------------------------------------------------------------------ #
class SelectSystemSpinner(Spinner):

    def __init__(self, **kwargs):
        super(SelectSystemSpinner, self).__init__(**kwargs)
        self.option_cls = SelectSystemSpinnerOption

    def populate_values(self):
        list_system = GV.DB_INPUTLIST.distinct('system')
        list_system.insert(0, 'ALL')
        self.values = list_system
        # self.values = GV.INPUT_TYPE

    def selected_text(self, value):
        self.isc_list_table.update_list(systems=value)


class SelectSystemSpinnerOption(SpinnerOption):
    pass


# ----- Input Label Widget ------------------------------------------------------------------------------------------- #
class LabelInput(Label):
    obj = ObjectProperty(None)


# ----- Input Row Widget --------------------------------------------------------------------------------------------- #
class InputBoxRow(ToggleButtonBehavior, BoxLayout):
    obj = ObjectProperty(None)

    def on_press(self):
        if self.state == 'normal':
            self.parent.isc_edit_box.disabled = True
            self.parent.isc_edit_box.opacity = 0
        else:
            self.parent.isc_edit_box.disabled = False
            self.parent.isc_edit_box.opacity = 1
            edit_data = GV.DB_INPUTLIST.find({'_id': ObjectId(self.id)})
            self.parent.isc_edit_box.isceb_num.text = self.obj
            self.parent.isc_edit_box.isceb_obj_id.text = str(edit_data[0]['_id'])
            self.parent.isc_edit_box.isceb_sys.text = edit_data[0]['system']
            self.parent.isc_edit_box.isceb_plc.text = str(edit_data[0]['register'])
            self.parent.isc_edit_box.isceb_bit.text = str(edit_data[0]['bit'])
            self.parent.isc_edit_box.isceb_name.text = edit_data[0]['name']
            self.parent.isc_edit_box.isceb_descr.text = edit_data[0]['description']
            self.parent.isc_edit_box.name_set = edit_data[0]['name']