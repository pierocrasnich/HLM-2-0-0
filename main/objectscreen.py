from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
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
from kivy.utils import get_color_from_hex

Builder.load_file('main/classi/object.kv')


# ----- DashScreen Main Class ---------------------------------------------------------------------------------------- #
class ObjectScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.obs_container.init()

    def on_pre_leave(self, *args):
        pass


# ----- Dashboard Container Layout ----------------------------------------------------------------------------------- #
class ObjectContainer(RelativeLayout):

    def __init__(self, **kwargs):
        super(ObjectContainer, self).__init__(**kwargs)

    def init(self):
        self.obsc_list_table.clear_widgets()
        list_obj = GV.DB_OBJECTLIST.find({})
        count = 1
        for obj in list_obj:
            obj_row = ObjectBoxRow()
            obj_row.count = str(count)
            obj_row.obj = obj
            obj_row.init()
            self.obsc_list_table.add_widget(obj_row)
            count += 1


# ----- Row Container for Label Output ------------------------------------------------------------------------------- #
class ObjectBoxRow(BoxLayout):
    obj = ObjectProperty(None)
    count = StringProperty(None)

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
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj['_id'])}, {'$set': {'deck': deck_set}})



