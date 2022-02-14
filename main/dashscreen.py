

from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.stencilview import StencilView
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.clock import Clock

from datetime import datetime
from pymongo import ASCENDING
from pymongo.errors import PyMongoError
from threading import Timer
from bson import ObjectId

import utility.gvar as GV

Builder.load_file('main/classi/dashboard.kv')

# -- Load OBJECT Library --------------------------------------------------------------------------------------------- #
from object.objectLibrary import ObjPLCM, ObjPLCZ, ObjHL, ObjBntRotate
Builder.load_file('object/objectLibrary.kv')


# ----- DashScreen Main Class ---------------------------------------------------------------------------------------- #
class DashScreen(Screen):
    mccm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DashScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.db_status, GV.PLC_ALIVE)
        GV.OBJ_CHANGE_THREAD = Timer(5, self.change_status)
        GV.OBJ_CHANGE_THREAD.setDaemon(True)
        GV.OBJ_CHANGE_THREAD.start()

    def on_enter(self, *args):
        self.dsc_deck_scatter.init_deck()
        Clock.schedule_once(self.dsc_obj_search.init)

    def on_leave(self, *args):
        pass

    def change_status(self):
        pipeline = [
            {'$match': {
                'operationType': 'replace'
            }},
        ]
        try:
            for document in GV.DB.objectList.watch(pipeline=pipeline, full_document='updateLookup'):
                #  Update FAULT list status
                self.dsc_list_fault.update_list(document)
                #  Change OBJECT status
                for obj in self.dsc_deck_scatter.obj_containers[document['fullDocument']['deck']].children:
                    if obj.id == ObjectId(document['fullDocument']['_id']):
                        obj.set_status(document['fullDocument'])
                        break
        except PyMongoError:
            print(PyMongoError)

    def db_status(self, istance):
        if GV.DB is None:
            self.dsc_database_check.color_fill = GV.RGBA_ERROR
        elif 'outputList' not in GV.DB.list_collection_names():
            self.dsc_database_check.color_fill = GV.RGBA_ERROR
        elif 'inputList' not in GV.DB.list_collection_names():
            self.dsc_database_check.color_fill = GV.RGBA_ERROR
        elif 'objectList' not in GV.DB.list_collection_names():
            self.dsc_database_check.color_fill = GV.RGBA_ERROR
        elif 'moduleConfig' not in GV.DB.list_collection_names():
            self.dsc_database_check.color_fill = GV.RGBA_ERROR
        elif 'connectionList' not in GV.DB.list_collection_names():
            self.dsc_database_check.color_fill = GV.RGBA_ERROR
        else:
            self.dsc_database_check.color_fill = GV.RGBA_SUCCESS


# ----- Dashboard Deck Layout ----------------------------------------------------------------------------------- #
# Deck Stencil View Class Container
class DeckStencilView(StencilView):

     def on_touch_down(self, touch):
         if not self.collide_point(touch.x, touch.y):
             return
         return super(DeckStencilView, self).on_touch_down(touch)


#  Deck Scatter Object 3140x1100 dimension
class DeckScatter(Scatter):

    def __init__(self, **kwargs):
        super(DeckScatter, self).__init__(**kwargs)
        self.deck_show = 0
        self.deck_name = ''
        self.deck_file = ''
        self.deck_number = len(GV.DECK_CONF)
        self.scale = 0.5
        self.delta_x = 340  # Scatter img scale 0.5 width 2250 - 1570 Stencil scale 0.5 view width / 2
        self.delta_y = 75  # Scatter img scale 0.5 height 600 - 450 Stencil scale 0.5 view height / 2
        self.pos = (0 - self.delta_x, 0 - self.delta_y)
        self.deck_image = None
        self.show_RGB = False
        self.show_legend = False
        self.legend = LegendModal()
        self.loader_bar = None
        self.loader_bar_setting = None
        self.obj_containers = []
        self.modify_containers = []
        Clock.schedule_once(self.init_obj)

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 1.6:
                    self.scale *= 1.05
            elif touch.button == 'scrollup':
                if self.scale > .35:
                    self.scale *= 0.95
        else:
            super(DeckScatter, self).on_touch_down(touch)

    # Deck
    def init_deck(self):

        self.deck_name = GV.DECK_CONF[self.deck_show]['name']
        self.deck_file = GV.DIR_DECKS + GV.DECK_CONF[self.deck_show]['file']
        self.remove_widget(self.deck_image)
        self.deck_image = Image(source=self.deck_file,
                                size_hint=(None, None),
                                size=(4500, 1200),
                                allow_stretch=True)
        self.deck_image.id = 'Image_dwg'
        self.add_widget(self.deck_image, canvas='before')
        self.dsc_dk_label.text = self.deck_name

        for child in self.children:

            if child.id == 'Modify_container_' + str(self.deck_show):
                if GV.OBJ_MODIFY:
                    child.pos = (0, 0)
                else:
                    child.pos = (10000, 0)
            elif child.id == 'Obj_container_' + str(self.deck_show):
                child.pos = (0, 0)
            elif child.id == 'Image_dwg':
                child.pos = (0, 0)
            else:
                child.pos = (10000, 0)

    def deck_up(self):
        if self.deck_show == self.deck_number - 1:
            return
        else:
            self.deck_show += 1
            self.dsc_dk_label.text = self.deck_name
            self.init_deck()

    def deck_down(self):
        if self.deck_show == 0:
            return
        else:
            self.deck_show -= 1
            self.dsc_dk_label.text = self.deck_name
            self.init_deck()

    def deck_select(self, instance):
        deck_menu = DeckMenu()
        deck_menu.scatter_obj = self
        deck_menu.init()
        self.mccm_dash.ds_container.add_widget(deck_menu)
        self.mccm_dash.dsc_dk_label.disabled = True

    def default_zoom(self, instance):
        self.scale = 0.5
        self.pos = (0 - self.delta_x, 0 - self.delta_y)

    def zoom_plus(self, instance):
        if self.scale > 1.6:
            return
        else:
            self.scale *= 1.05

    def zoom_minus(self, instance):
        if self.scale < .35:
            return
        else:
            self.scale *= 0.95

    # OBJECT
    def init_obj(self, instance):

        for count, dk in enumerate(GV.DECK_CONF):
            obj_container = RelativeLayout(size_hint=(1, 1))
            obj_container.id = 'Obj_container_' + str(count)
            self.obj_containers.append(obj_container)
            self.add_widget(obj_container)
            modify_container = RelativeLayout(size_hint=(1, 1))
            modify_container.id = 'Modify_container_' + str(count)
            modify_container.pos = (10000, 0)
            self.modify_containers.append(modify_container)
            self.add_widget(modify_container)
            if count != self.deck_show:
                obj_container.pos = (10000, 0)
            else:
                obj_container.pos = (0, 0)
        self.generate_obj()

    def generate_obj(self):
        if 'objectList' in GV.DB.list_collection_names():
            obj_list = list(GV.DB_OBJECTLIST.find({}))
        else:
            return
        for obj_data in obj_list:
            self.update_obj(obj_data)

    def update_obj_deck(self, obj_data, old_deck):
        for child in self.obj_containers[old_deck].children:
            if child.id == obj_data['_id']:
                self.obj_containers[old_deck].remove_widget(child)
                break
        for child in self.modify_containers[old_deck].children:
            if child.id == 'Mod_' + str(obj_data['_id']):
                self.modify_containers[old_deck].remove_widget(child)
                break
        self.update_obj(obj_data)

    def update_obj(self, obj_data):
        if obj_data['system'] == 'PLCM':
            obj = ObjPLCM()
            obj.id = ObjectId(obj_data['_id'])
        elif obj_data['system'] == 'PLCZ':
            obj = ObjPLCZ()
            obj.id = ObjectId(obj_data['_id'])
        else:
            obj = ObjHL()
            obj.id = ObjectId(obj_data['_id'])
        rotate_btn = ObjBntRotate()
        rotate_btn.id = 'Mod_' + str(obj_data['_id'])
        rotate_btn.obj = obj
        rotate_btn.pos = (obj_data['posX'] + 35, obj_data['posY'] + 30)
        #  Object
        obj.scatter_obj = self
        obj.rotate_btn = rotate_btn
        obj.obj_data = obj_data
        obj.angle_obj = obj_data['rotate']
        obj.pos = (obj_data['posX'], obj_data['posY'])
        obj.obj_widget = self.obj_containers[obj_data['deck']]
        obj.set_status(obj_data)
        self.obj_containers[obj_data['deck']].remove_widget(obj)
        self.obj_containers[obj_data['deck']].add_widget(obj)
        self.modify_containers[obj_data['deck']].add_widget(rotate_btn)

    def obj_modify(self, instance):
        if GV.OBJ_MODIFY:
            GV.OBJ_MODIFY = False
            instance.color_fill = GV.RGBA_BORDER
        else:
            GV.OBJ_MODIFY = True
            instance.color_fill = GV.RGBA_ORANGE
        self.init_deck()

    def obj_RGB(self, instance):
        if GV.OBJ_RGB:
            GV.OBJ_RGB = False
            instance.color_fill = GV.RGBA_BORDER
        else:
            GV.OBJ_RGB = True
            instance.color_fill = GV.RGBA_ORANGE
        for container in self.obj_containers:
            for obj in container.children:
                if obj.obj_data['system'] == 'HL':
                    obj.show_rgb()

    def legend_show(self, instance):
        if self.show_legend:
            instance.color_fill = GV.RGBA_BORDER
            self.show_legend = False
            self.parent.remove_widget(self.legend)
        else:
            instance.color_fill = GV.RGBA_ORANGE
            self.parent.add_widget(self.legend)

            self.show_legend = True

    def clear_obj(self):
        for elm in self.children:
            if elm.id != 'Image_dwg':
                elm.clear_widgets()


# Legend Popup
class LegendModal(BoxLayout):
    pass


# Search OBJECT button
class SearchSelectMenu(GridLayout):
    pass


class SearchSelectBtn(Button):
    container = ObjectProperty(None)
    search_btn = ObjectProperty(None)

    def updateTextInput(self, instance):
        instance.search_btn.dsc_obj_search_text.text = instance.text
        self.container.clear_widgets()


class BtnSearchObject(GridLayout):

    def __init__(self, **kwargs):
        super(BtnSearchObject, self).__init__(**kwargs)
        self.list_data = []
        self.new_list_search = []
        self.search_menu = SearchSelectMenu()
        self.search_menu.pos = (self.x, self.y - 270)

    def init(self, instance):
        collection_value = GV.DB_OBJECTLIST.find().sort("name", ASCENDING)
        for dataRow in collection_value:
            self.list_data.append(dataRow)
        self.new_list_search = list(map(lambda x: x['name'], self.list_data))

    def search(self):
        if self.dsc_obj_search_text.text != '':
            obj = GV.DB_OBJECTLIST.find_one({'name': self.dsc_obj_search_text.text})
            self.dsc_deck_scatter.deck_show = int(obj['deck'])
            self.dsc_deck_scatter.scale = 1
            self.dsc_deck_scatter.pos = (785 - obj['posX'], 225 - obj['posY'])
            self.dsc_deck_scatter.init_deck()
            self.dsc_deck_scatter.init_obj(None)
            for child in self.dsc_deck_scatter.obj_containers[int(obj['deck'])].children:
                if child.id == ObjectId(str(obj['_id'])):
                    child.display_tooltip()
                    break
            self.dsc_obj_search_text.text = ''
        else:
            return

    def searchInput(self):
        self.search_menu.dsc_obj_search_list.clear_widgets()
        self.ds_container.remove_widget(self.search_menu)
        text_search = self.dsc_obj_search_text.text
        name_result = []

        for word in self.new_list_search:
            name_find = word.find(text_search)
            if name_find == 0:
                name_result.append(word)
        name_result = list(dict.fromkeys(name_result))

        if len(name_result) != 0 and text_search != '':
            for name_value in name_result:
                search_select = SearchSelectBtn()
                search_select.text = name_value
                search_select.size = 250, 30
                search_select.search_btn = self
                search_select.container = self.search_menu.dsc_obj_search_list
                self.search_menu.dsc_obj_search_list.add_widget(search_select)

        self.search_menu.pos = (self.x + 10, self.y - 290)
        self.ds_container.add_widget(self.search_menu)


# Deck menu select
class DeckMenu(GridLayout):
    scatter_obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DeckMenu, self).__init__(**kwargs)

    def init(self):
        count = 1
        for decks in GV.DECK_CONF:
            deck_sel = DeckMenuSelect(text=decks['name'])
            deck_sel.deck_index = count - 1
            deck_sel.scatter_obj = self.scatter_obj
            self.add_widget(deck_sel)
            count += 1
        self.x = 1400
        self.y = 950 - (count * 30)
        Clock.schedule_once(self.close, 5)

    def close(self, instance):
        Clock.unschedule(self.close)
        self.parent.remove_widget(self)
        self.scatter_obj.dsc_dk_label.disabled = False


class DeckMenuSelect(Button):
    deck_index = NumericProperty(None)
    scatter_obj = ObjectProperty(None)

    def deck_set(self):
        self.scatter_obj.deck_show = self.deck_index
        self.scatter_obj.init_deck()
        self.scatter_obj.init_obj(None)
        self.parent.close(None)


# ----- Container FAULT list ---------------------------------------------------------------------------------------- #
class FaultListLabel(Label):
    pass


class FaultListRow(ToggleButtonBehavior, BoxLayout):
    row_data = ObjectProperty(None)
    scatter_obj = ObjectProperty(None)

    def on_press(self):
        self.scatter_obj.deck_show = int(self.row_data['deck'])
        self.scatter_obj.scale = 1
        self.scatter_obj.pos = (785 - self.row_data['posX'], 225 - self.row_data['posY'])
        self.scatter_obj.init_deck()
        self.scatter_obj.init_obj(None)

        for child in self.scatter_obj.obj_containers[int(self.row_data['deck'])].children:
            if child.id == ObjectId(self.row_data['_id']):
                child.display_tooltip()
                break


class ListFault(BoxLayout):

    def __init__(self, **kwargs):
        super(ListFault, self).__init__(**kwargs)
        self.fault_value = '1'
        self.normal_value = '0'

        Clock.schedule_once(self.init)

    def init(self, instance):
        list_fault = GV.DB_OBJECTLIST.find({'status': self.fault_value})
        for row_data in list(list_fault):
            self.create_row(row_data)
            msg_color = 'error'
            msg_text = 'Device ' + row_data['name'] + ' in FAULT'
            self.mccm_dash.mccm.mm_notification.notification_msg(msg_color, msg_text)
        if len(self.children) <= 10:
            self.parent.do_scroll_y = False
        else:
            self.parent.do_scroll_y = True
        self.dsc_fault_number.text = 'Total faults: ' + str(len(self.children))

    def create_row(self, row_data):
        if row_data['name']:
            date_now = datetime.now()
            timestamp = date_now.strftime("%d/%m/%Y - %H:%M:%S")
        else:
            timestamp = ''
        list_row = FaultListRow()
        list_row.id = 'id_' + row_data['name']
        list_row.row_data = row_data
        list_row.scatter_obj = self.dsc_deck_scatter
        list_row.add_widget(FaultListLabel(text=str(timestamp), size=(298, 30)))
        list_row.add_widget(FaultListLabel(text=row_data['name'], size=(1282, 30)))
        self.add_widget(list_row, len(self.children))

    def update_list(self, document):
        id = 'id_' + str(document['fullDocument']['name'])
        status = document['fullDocument']['status']

        if status == self.fault_value:
            self.create_row(document['fullDocument'])
            msg_color = 'error'
            msg_text = 'Device ' + document['fullDocument']['name'] + ' in FAULT'
            self.mccm_dash.mccm.mm_notification.notification_msg(msg_color, msg_text)
        elif status == self.normal_value:
            for child in self.children:
                if child.id == id:
                    self.remove_widget(child)
                    msg_color = 'success'
                    msg_text = 'Device ' + document['fullDocument']['name'] + ' NORMAL'
                    self.mccm_dash.mccm.mm_notification.notification_msg(msg_color, msg_text)
                    break

        if len(self.children) <= 11:
            self.parent.do_scroll_y = False
        else:
            self.parent.do_scroll_y = True
        self.dsc_fault_number.text = 'Total faults: ' + str(len(self.children))










