from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

from bson import ObjectId
import utility.gvar as GV
from classi.csv import ExportConnectButton, ImportConnectButton, ImportDialog
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.lang import Builder
from pymongo import ASCENDING, DESCENDING

Builder.load_file('main/classi/output.kv')


# ----- Classe principale dello Screen OUTPUT ------------------------------------------------------------------------ #
class OutputScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.osc_list_table.get_list()
        Clock.schedule_once(self.osc_search.init)

    def on_pre_leave(self, *args):
        self.osc_list_table.clear_list()


class OutputContainer(RelativeLayout):

    def update_name(self):
        # validate form
        address_list = [item['address'] for item in GV.DB_OUTPUTLIST.find({}, {'address': 1})]

        if self.osc_edit_box.osceb_address.text == '' or self.osc_edit_box.osceb_address.text == '0000':
            msg_color = 'error'
            msg_text = 'Missing address !!!'
            self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
            return

        if len(self.osc_edit_box.osceb_address.text) != 4:
            msg_color = 'error'
            msg_text = 'Address 4 char (0000)!!!'
            self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
            return

        if int(self.osc_edit_box.osceb_address.text) <= int(GV.DOOR_DEFAULT) or \
                int(self.osc_edit_box.osceb_address.text) >= int(GV.DOOR_BROADCAST):
            msg_color = 'error'
            msg_text = 'Address Error!!!'
            self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
            return

        if self.osc_edit_box.osceb_plc.text == '':
            msg_color = 'error'
            msg_text = 'Missing PLC set !!!'
            self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
            return

        if self.osc_edit_box.osceb_plc_port.text == '' or self.osc_edit_box.osceb_plc_port.text == '0':
            msg_color = 'error'
            msg_text = 'Missing PLC port set !!!'
            self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
            return

        if self.osc_edit_box.osceb_address.text != self.osc_edit_box.obj['address']:
            if self.osc_edit_box.osceb_address.text in address_list:
                msg_color = 'error'
                msg_text = 'Address just present!!!'
                self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
                return
            else:
                self.save_mod()
        else:
            self.save_mod()

    def save_mod(self):
        hl_old = GV.DB_OUTPUTLIST.find_one({'_id': ObjectId(self.osc_edit_box.osceb_obj_id.text)})
        GV.DB_OUTPUTLIST.update_one({'_id': ObjectId(self.osc_edit_box.osceb_obj_id.text)},
                                    {'$set': {'address': self.osc_edit_box.osceb_address.text,
                                              'plc': self.osc_edit_box.osceb_plc.text,
                                              'port': int(self.osc_edit_box.osceb_plc_port.text),
                                              'name': self.osc_edit_box.osceb_name.text,
                                              'description': self.osc_edit_box.osceb_descr.text}})
        # Modify OBJECT in OBJECT list collection
        GV.DB_OBJECTLIST.update_one({'address': hl_old['address']},
                                    {'$set': {'address': self.osc_edit_box.osceb_address.text,
                                              'name': self.osc_edit_box.osceb_name.text}})
        # Remove doors from array "OutputList" of "connectionList"
        id_value = ObjectId(self.osc_edit_box.osceb_obj_id.text)
        GV.DB_CONNECTIONLIST.update({}, {"$pull": {"outputList": {"_id": id_value}}}, upsert=True)

        msg_color = 'success'
        msg_text = 'Output ' + self.osc_edit_box.osceb_address.text + ' save !!!'
        self.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
        self.osc_list_table.update_list()
        self.osc_edit_box.disabled = True
        self.osc_edit_box.opacity = 0

    def cancel_update(self):
        self.osc_edit_box.disabled = True
        self.osc_edit_box.opacity = 0
        self.parent.osc_edit_box.osceb_plc.text = '???'
        self.parent.osc_edit_box.osceb_plc_port.text = '???'
        self.parent.osc_edit_box.osceb_plc.values = []
        self.parent.osc_edit_box.osceb_plc_port.values = []


# ----- Contenitore della lista degli OUTPUT ------------------------------------------------------------------------- #
class ListOutput(GridLayout):

    def __init__(self, **kwargs):
        super(ListOutput, self).__init__(**kwargs)
        self.list_output = []
        self.list_page_row = 20
        self.list_page_min = 0
        self.list_page_max = self.list_page_min + self.list_page_row
        self.layout = None

    def update_list(self):
        self.clear_list()
        self.get_list()

    def clear_list(self):
        self.clear_widgets()

    def get_list_next(self):
        if self.list_page_max >= len(self.list_output):
            return
        else:
            self.list_page_min += self.list_page_row
            self.list_page_max += self.list_page_row
            self.draw_table()

    def get_list_prev(self):
        if self.list_page_min - self.list_page_row <= 0:
            self.list_page_min = 0
            self.list_page_max = self.list_page_row
            self.draw_table()
        else:
            self.list_page_min -= self.list_page_row
            self.list_page_max -= self.list_page_row
            self.draw_table()

    def get_list(self):
        errors = 0
        self.list_output = []
        for hl in GV.DB_OUTPUTLIST.find({}).sort('address', ASCENDING):
            # errors compile check
            if hl['address'] == '0000':  # address is empty or already present
                errors += 1
            if hl['plc'] == '':  # PLC empty
                errors += 1
            if hl['port'] == '' or hl['port'] == '0':  # port com empty
                errors += 1
            self.list_output.append(hl)

        self.osc_list_errors.text = 'Number of Errors: ' + str(errors)
        self.draw_table()

    def draw_table(self):
        self.clear_list()
        if self.list_page_min + self.list_page_row > len(self.list_output):
            page_max = str(len(self.list_output))
        else:
            page_max = str(self.list_page_max)
        page_min = str(self.list_page_min)
        page_tot = str(len(self.list_output))
        self.osc_list_pageCount.text = 'from ' + page_min + ' to ' + page_max + ' of ' + page_tot
        hl_count = self.list_page_min + 1
        for hl in self.list_output[self.list_page_min:self.list_page_max]:
            if hl['address'] == '0000':  # address is empty or already present
                add_c = GV.RGBA_ERROR
            else:
                add_c = 1, 1, 1, 0
            if hl['plc'] == '':  # PLC empty
                plc_c = GV.RGBA_ERROR
            else:
                plc_c = 1, 1, 1, 0
            if hl['port'] == '' or hl['port'] == '0':  # port com empty
                port_c = GV.RGBA_ERROR
            else:
                port_c = 1, 1, 1, 0

            self.layout = OutputBoxRow()
            self.layout.index = str(hl_count)
            self.layout.obj = hl
            self.layout.orientation = 'horizontal'
            self.layout.size_hint = (1, None)
            self.layout.height = 30
            self.layout.group = 'output'
            self.layout.add_widget(LabelOutput(text=str(hl_count), size=(50, 30), obj=hl))
            self.layout.add_widget(LabelOutput(text=str(hl['system']), size=(150, 30), obj=hl))
            self.layout.add_widget(LabelOutput(text=str(hl['address']), size=(150, 30), obj=hl, c_er=add_c))
            self.layout.add_widget(LabelOutput(text=str(hl['plc']), size=(100, 30), obj=hl, c_er=plc_c))
            self.layout.add_widget(LabelOutput(text=str(hl['port']), size=(100, 30), obj=hl, c_er=port_c))
            self.layout.add_widget(LabelOutput(text=str(hl['name']), size=(150, 30), obj=hl ))
            self.layout.add_widget(LabelOutput(text=str(hl['description']), size=(400, 30), obj=hl))
            self.add_widget(self.layout)
            hl_count += 1


# ----- Classe Label Output ------------------------------------------------------------------------------------------ #
class LabelOutput(Label):
    obj = ObjectProperty(None)
    c_er = ListProperty([1, 1, 1, 0])


# ----- Row Container for Label Output ------------------------------------------------------------------------------- #
class OutputBoxRow(ToggleButtonBehavior, BoxLayout):
    obj = ObjectProperty(None)
    plc_set = StringProperty('')
    plc_select = ObjectProperty()
    comPort_set = NumericProperty(0)
    comPort_select = NumericProperty(0)
    plc_main_btn = ObjectProperty()
    plc_port_main_btn = ObjectProperty()

    def on_press(self):
        if self.state == 'normal':
            self.parent.osc_edit_box.disabled = True
            self.parent.osc_edit_box.opacity = 0
            self.parent.osc_edit_box.osceb_plc.text = '???'
            self.parent.osc_edit_box.osceb_plc_port.text = '???'
            self.parent.osc_edit_box.osceb_plc.values = []
            self.parent.osc_edit_box.osceb_plc_port.values = []
        else:
            self.parent.osc_edit_box.disabled = False
            self.parent.osc_edit_box.opacity = 1
            self.get_edit()

    def get_edit(self):
        edit_data = GV.DB_OUTPUTLIST.find_one({'_id': self.obj['_id']})
        self.parent.osc_edit_box.obj = edit_data
        self.parent.osc_edit_box.osceb_num.text = self.index
        self.parent.osc_edit_box.osceb_obj_id.text = str(edit_data['_id'])
        self.parent.osc_edit_box.osceb_sys.text = edit_data['system']
        self.parent.osc_edit_box.osceb_address.text = edit_data['address']
        self.parent.osc_edit_box.osceb_name.text = edit_data['name']
        self.parent.osc_edit_box.osceb_descr.text = edit_data['description']
        self.parent.osc_edit_box.osceb_plc.text = edit_data['plc']
        self.parent.osc_edit_box.osceb_plc_port.text = str(edit_data['port'])
        self.parent.osc_edit_box.osceb_plc.values = [item['name'] for item in GV.DB_PLCZONECONFIG.find({})]


# ----- Spinner and Option Class for PLC e Com Port ------------------------------------------------------------------ #
class OutputPLCSpinner(Spinner):

    def __init__(self, **kwargs):
        super(OutputPLCSpinner, self).__init__(**kwargs)
        self.option_cls = OutputPLCSpinnerOption

    def populate_com(self, name):
        for item in GV.DB_PLCZONECONFIG.find({}):
            if item['name'] == name:
                self.osceb_plc_port.values = [str(x) for x in range(1, item['ComPort'] + 1)]


class OutputPLCSpinnerOption(SpinnerOption):
    pass


# Search OBJECT button
class SearchSelectMenuOutput(GridLayout):
    pass


class SearchSelectBtnOutput(Button):
    container = ObjectProperty(None)
    search_btn = ObjectProperty(None)

    def updateTextInput(self, instance):
        instance.search_btn.osc_search_text.text = instance.text
        self.container.clear_widgets()


class BtnSearchOutput(GridLayout):

    def __init__(self, **kwargs):
        super(BtnSearchOutput, self).__init__(**kwargs)
        self.list_data = []
        self.new_list_search = []
        self.search_menu = SearchSelectMenuOutput()
        self.search_menu.pos = (self.x, self.y - 270)

    def init(self, instance):
        for dataRow in self.osc_list_table.list_output:
            self.list_data.append(dataRow)
        self.new_list_search = list(map(lambda x: x['name'], self.list_data))

    def search(self):
        if self.osc_search_text.text != '':
            index_element = self.new_list_search.index(self.osc_search_text.text)
            self.osc_list_table.list_page_min = index_element
            self.osc_list_table.list_page_max = self.osc_list_table.list_page_min + self.osc_list_table.list_page_row
            self.osc_list_table.draw_table()
            self.osc_search_text.text = ''
        else:
            return

    def searchInput(self):
        self.search_menu.osc_search_list.clear_widgets()
        self.os_container.remove_widget(self.search_menu)
        text_search = self.osc_search_text.text
        name_result = []

        for word in self.new_list_search:
            name_find = word.find(text_search)
            if name_find == 0:
                name_result.append(word)
        name_result = list(dict.fromkeys(name_result))

        if len(name_result) != 0 and text_search != '':
            for name_value in name_result:
                search_select = SearchSelectBtnOutput()
                search_select.text = name_value
                search_select.size = 250, 30
                search_select.search_btn = self
                search_select.container = self.search_menu.osc_search_list
                self.search_menu.osc_search_list.add_widget(search_select)

        self.search_menu.pos = (self.x + 10, self.y - 290)
        self.os_container.add_widget(self.search_menu)