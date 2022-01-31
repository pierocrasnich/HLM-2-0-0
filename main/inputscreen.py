from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

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
        Clock.schedule_once(self.isc_search.init)

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
            print('update name---->', self.isc_edit_box.isceb_sys.text)
            # self.iscc_system_spn.text = self.isc_edit_box.isceb_sys.text

    def cancel_update(self):
        self.isc_edit_box.disabled = True
        self.isc_edit_box.opacity = 0


# ----- Contenitore della lista degli INPUT -------------------------------------------------------------------------- #
class ListInput(GridLayout):
    def __init__(self, **kwargs):
        super(ListInput, self).__init__(**kwargs)
        self.system_select = ''
        self.list_input = []
        self.list_page_row = 20
        self.list_page_min = 0
        self.list_page_max = self.list_page_min + self.list_page_row
        self.layout = None

    def update_list(self, systems):
        self.clear_list()
        self.get_list(systems=systems)

    def clear_list(self):
        self.clear_widgets()

    def get_list_next(self):
        if self.list_page_max >= len(self.list_input):
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

    def get_list(self, systems):
        # print(systems)
        if self.system_select != systems:
            self.list_page_min = 0
            self.system_select = systems

        self.list_input = []
        if systems == 'ALL':
            data = GV.DB_INPUTLIST.find().sort('register', ASCENDING)
        else:
            data = GV.DB_INPUTLIST.find({'system': systems}).sort('register', ASCENDING)
        for inp in data:
            self.list_input.append(inp)
        self.draw_table()

    def draw_table(self):
        self.clear_list()
        if self.list_page_min + self.list_page_row > len(self.list_input):
            page_max = str(len(self.list_input))
        else:
            page_max = str(self.list_page_max)
        page_min = str(self.list_page_min)
        page_tot = str(len(self.list_input))
        self.isc_list_pageCount.text = 'from ' + page_min + ' to ' + page_max + ' of ' + page_tot

        count_input = self.list_page_min + 1
        for input_item in self.list_input[self.list_page_min:self.list_page_max]:
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


# Search OBJECT button
class SearchSelectMenuInput(GridLayout):
    pass


class SearchSelectBtnInput(Button):
    container = ObjectProperty(None)
    search_btn = ObjectProperty(None)

    def updateTextInput(self, instance):
        instance.search_btn.isc_search_text.text = instance.text
        self.container.clear_widgets()


class BtnSearchInput(GridLayout):

    def __init__(self, **kwargs):
        super(BtnSearchInput, self).__init__(**kwargs)
        self.list_data = []
        self.new_list_search = []
        self.search_menu = SearchSelectMenuInput()
        # self.search_menu.pos = (self.x, self.y - 270)

    def init(self, instance):
        for dataRow in self.isc_list_table.list_input:
            self.list_data.append(dataRow)
        self.new_list_search = list(map(lambda x: x['name'], self.list_data))

    def search(self):
        if self.isc_search_text.text != '':
            index_element = self.new_list_search.index(self.isc_search_text.text)
            self.isc_list_table.list_page_min = index_element
            self.isc_list_table.list_page_max = self.isc_list_table.list_page_min + self.isc_list_table.list_page_row
            self.isc_list_table.draw_table()
            self.isc_search_text.text = ''
        else:
            return

    def searchInput(self):
        self.search_menu.isc_search_list.clear_widgets()
        self.is_container.remove_widget(self.search_menu)
        text_search = self.isc_search_text.text
        name_result = []

        for word in self.new_list_search:
            name_find = word.find(text_search)
            if name_find == 0:
                name_result.append(word)
        name_result = list(dict.fromkeys(name_result))

        if len(name_result) != 0 and text_search != '':
            for name_value in name_result:
                search_select = SearchSelectBtnInput()
                search_select.text = name_value
                search_select.size = 250, 30
                search_select.search_btn = self
                search_select.container = self.search_menu.isc_search_list
                self.search_menu.isc_search_list.add_widget(search_select)

        self.search_menu.pos = (self.x + 10, self.y - 290)
        self.is_container.add_widget(self.search_menu)