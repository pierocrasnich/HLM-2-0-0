from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner, SpinnerOption
from bson import ObjectId
import utility.gvar as GV
from classi.csv import ExportConnectButton, ImportConnectButton, ImportDialog, ImportConnectButton, ExportObjectButton
from kivy.utils import get_color_from_hex
from pymongo import ASCENDING, DESCENDING

Builder.load_file('main/classi/object.kv')


# ----- DashScreen Main Class ---------------------------------------------------------------------------------------- #
class ObjectScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.obsc_list_table.get_list()

    def on_pre_leave(self, *args):
        pass


# ----- Dashboard Container Layout ----------------------------------------------------------------------------------- #
class ObjectContainer(RelativeLayout):
    pass


class ListObject(GridLayout):

    def __init__(self, **kwargs):
        super(ListObject, self).__init__(**kwargs)
        self.list_object = []
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
        if self.list_page_max >= len(self.list_object):
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
        self.list_object = []

        for hl in GV.DB_OBJECTLIST.find({}).sort('address', ASCENDING):
            self.list_object.append(hl)
        self.draw_table()

    def draw_table(self):
        self.clear_list()
        self
        if self.list_page_min + self.list_page_row > len(self.list_object):
            page_max = str(len(self.list_object))
        else:
            page_max = str(self.list_page_max)
        page_min = str(self.list_page_min)
        page_tot = str(len(self.list_object))
        self.obsc_list_pageCount.text = 'from ' + page_min + ' to ' + page_max + ' of ' + page_tot
        hl_count = self.list_page_min + 1
        for hl in self.list_object[self.list_page_min:self.list_page_max]:
            obj_row = ObjectBoxRow()
            obj_row.count = str(hl_count)
            obj_row.obj = hl
            obj_row.scatter_obj = self.mccm_object.mccm.mccm_dash.dsc_deck_scatter
            obj_row.init()
            self.add_widget(obj_row)
            hl_count += 1


class LabelObject(Label):
    obj = ObjectProperty(None)


# ----- Row Container for Label Output ------------------------------------------------------------------------------- #
class ObjectBoxRow(BoxLayout):
    obj = ObjectProperty(None)
    count = StringProperty(None)
    scatter_obj = ObjectProperty()
    obj_widget = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ObjectBoxRow, self).__init__(**kwargs)
        # Deck dropdown menu
        count = 0
        for elm in GV.DECK_CONF:
            deck_sel = Button(
                text=elm['name'],
                size_hint=(None, None),
                size=(200,40),
                color=GV.RGBA_ORANGE,
                background_color=(0, 0, 0, 0)
            )
            deck_sel.dk_n = count
            deck_sel.bind(on_release=lambda deck_sel: self.obsc_row_deck_dropdown.select(deck_sel.text))
            deck_sel.bind(on_release=lambda deck_sel: self.set_deck(deck_sel.dk_n))
            self.obsc_row_deck_dropdown.add_widget(deck_sel)
            count +=1

    def init(self):
        self.obsc_row_count.text = self.count
        self.obsc_row_system.text = self.obj['system']
        self.obsc_row_name.text = self.obj['system']
        self.obsc_row_address.text = self.obj['address']
        self.obsc_row_deck.text = str(GV.DECK_CONF[self.obj['deck']]['name'])
        self.obsc_row_posx.text = str(round(self.obj['posX'], 1))
        self.obsc_row_posy.text = str(round(self.obj['posY'], 1))
        self.obsc_row_rotate.text = str(self.obj['rotate'])

    def set_deck(self, deck_set):
        old_deck = self.obj['deck']
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj['_id'])}, {'$set': {'deck': deck_set}})
        self.obj['deck'] = deck_set
        self.scatter_obj.update_obj_deck(self.obj, old_deck)



