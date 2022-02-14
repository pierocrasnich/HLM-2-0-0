import time

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import  ListProperty, ObjectProperty,  NumericProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

from bson import ObjectId
import utility.gvar as GV


class ObjPLCM(Button):
    scatter_obj = ObjectProperty(None)
    obj_widget = ObjectProperty(None)
    obj_data = ObjectProperty(None)
    rotate_btn = ObjectProperty(None)
    color_fill = ListProperty([])
    angle_obj = NumericProperty(0)
    tooltip_show = False
    status_obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ObjPLCM, self).__init__(**kwargs)
        self.tooltip = ObjTooltip()
        Clock.unschedule(self.close_tooltip)

    def set_status(self, status):
        self.status_obj = status

        if self.status_obj['status'] == "":
            self.color_fill = GV.OBJ_RGB_NO_DATA
        elif self.status_obj['status'] == "0":
            self.color_fill = GV.OBJ_RGB_NORMAL
        elif self.status_obj['status'] == "1":
            self.color_fill = GV.OBJ_RGB_FAULT
        else:
            self.color_fill = GV.OBJ_RGB_NO_DATA

    def on_press(self):
        self.scatter_obj.do_translation = (False, False)
        if not self.tooltip_show:
            self.display_tooltip()

    def on_touch_move(self, touch):
        if GV.OBJ_MODIFY:
            if touch.grab_current is self:
                self.x = touch.x - 25
                self.y = touch.y - 25
                self.rotate_btn.x = self.x + 55
                self.rotate_btn.y = self.y + 40
                self.tooltip.x = self.x + 25
                self.tooltip.y = self.y + 55
        else:
            return

    def on_release(self):
        self.scatter_obj.do_translation = (True, True)
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj_data['_id'])}, {'$set': {'posX': self.x, 'posY': self.y}})

    def rotate_obj(self, instance):
        cursor = GV.DB_OBJECTLIST.find_one({'_id': ObjectId(self.obj_data['_id'])})
        angle_set = cursor['rotate']
        if angle_set == 0:
            self.angle_obj = 90
        elif angle_set == 90:
            self.angle_obj = 180
        elif angle_set == 180:
            self.angle_obj = 270
        elif angle_set == 270:
            self.angle_obj = 0
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj_data['_id'])}, {'$set': {'rotate': self.angle_obj}})

    def close_tooltip(self, *args):
        self.obj_widget.remove_widget(self.tooltip)
        self.tooltip_show = False

    def display_tooltip(self, *args):
        time.sleep(.5)
        self.tooltip_show = True
        self.tooltip.pos = (self.x + 7, self.y + 55)
        self.tooltip.text = self.obj_data['name']
        self.obj_widget.add_widget(self.tooltip)
        Clock.schedule_once(self.close_tooltip, 3)


class ObjPLCZ(Button):
    scatter_obj = ObjectProperty(None)
    obj_widget = ObjectProperty(None)
    obj_data = ObjectProperty(None)
    rotate_btn = ObjectProperty(None)
    color_fill = ListProperty([])
    angle_obj = NumericProperty(0)
    tooltip_show = False
    status_obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ObjPLCZ, self).__init__(**kwargs)
        self.tooltip = ObjTooltip()
        Clock.unschedule(self.close_tooltip)

    def set_status(self, status):
        self.status_obj = status

        if self.status_obj['status'] == "":
            self.color_fill = GV.OBJ_RGB_NO_DATA
        elif self.status_obj['status'] == "0":
            self.color_fill = GV.OBJ_RGB_NORMAL
        elif self.status_obj['status'] == "1":
            self.color_fill = GV.OBJ_RGB_FAULT
        else:
            self.color_fill = GV.OBJ_RGB_NO_DATA

    def on_press(self):
        self.scatter_obj.do_translation = (False, False)
        if not self.tooltip_show:
            self.display_tooltip()

    def on_touch_move(self, touch):
        if GV.OBJ_MODIFY:
            if touch.grab_current is self:
                self.x = touch.x - 25
                self.y = touch.y - 25
                self.rotate_btn.x = self.x + 55
                self.rotate_btn.y = self.y + 40
                self.tooltip.x = self.x + 25
                self.tooltip.y = self.y + 55
        else:
            return

    def on_release(self):
        self.scatter_obj.do_translation = (True, True)
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj_data['_id'])}, {'$set': {'posX': self.x, 'posY': self.y}})

    def rotate_obj(self, instance):
        cursor = GV.DB_OBJECTLIST.find_one({'_id': ObjectId(self.obj_data['_id'])})
        angle_set = cursor['rotate']
        if angle_set == 0:
            self.angle_obj = 90
        elif angle_set == 90:
            self.angle_obj = 180
        elif angle_set == 180:
            self.angle_obj = 270
        elif angle_set == 270:
            self.angle_obj = 0
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj_data['_id'])}, {'$set': {'rotate': self.angle_obj}})

    def close_tooltip(self, *args):
        self.obj_widget.remove_widget(self.tooltip)
        self.tooltip_show = False
        Clock.unschedule(self.close_tooltip)

    def display_tooltip(self, *args):
        time.sleep(.5)
        self.tooltip_show = True
        self.tooltip.pos = (self.x + 7, self.y + 55)
        self.tooltip.text = self.obj_data['name']
        self.obj_widget.add_widget(self.tooltip)
        Clock.schedule_once(self.close_tooltip, 3)


class ObjHL(Button):
    scatter_obj = ObjectProperty(None)
    obj_widget = ObjectProperty(None)
    obj_data = ObjectProperty(None)
    rotate_btn = ObjectProperty(None)
    color_fill = ListProperty([])
    color_fill_sx = ListProperty([])
    color_fill_sx_off = NumericProperty()
    color_fill_dx = ListProperty([])
    color_fill_dx_off = NumericProperty()
    angle_obj = NumericProperty(0)
    tooltip_show = False
    status_obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ObjHL, self).__init__(**kwargs)
        self.tooltip = ObjTooltip()
        Clock.unschedule(self.close_tooltip)
        self.show_rgb()

    def set_status(self, status):
        self.status_obj = status
        color_sx = str(self.status_obj['colorSX'])
        color_dx = str(self.status_obj['colorDX'])
        self.color_fill_sx = get_color_from_hex('#' + color_sx)
        self.color_fill_dx = get_color_from_hex('#' + color_dx)

        if GV.OBJ_RGB:
            if color_sx == '000000':
                self.color_fill_sx_off = 0
            else:
                self.color_fill_sx_off = 1
            if color_dx == '000000':
                self.color_fill_dx_off = 0
            else:
                self.color_fill_dx_off = 1

        if self.status_obj['status'] == "":
            self.color_fill = GV.OBJ_RGB_NO_DATA
        elif self.status_obj['status'] == "0":
            self.color_fill = GV.OBJ_RGB_NORMAL
        elif self.status_obj['status'] == "1":
            self.color_fill = GV.OBJ_RGB_FAULT
        else:
            self.color_fill = GV.OBJ_RGB_NO_DATA

    def show_rgb(self):
        if GV.OBJ_RGB:
            if str(self.status_obj['colorDX']) != '000000':
                self.color_fill_dx_off = 1
            if str(self.status_obj['colorSX']) != '000000':
                self.color_fill_sx_off = 1
        else:
            self.color_fill_dx_off = 0
            self.color_fill_sx_off = 0

    def on_press(self):
        if not self.tooltip_show:
            self.display_tooltip()

    def close_tooltip(self, *args):
        self.obj_widget.remove_widget(self.tooltip)
        Clock.unschedule(self.close_tooltip)
        self.tooltip_show = False

    def display_tooltip(self, *args):
        time.sleep(.5)
        self.tooltip_show = True
        self.obj_widget.add_widget(self.tooltip)
        self.tooltip.pos = (self.x + 15, self.y + 55)
        self.tooltip.text = self.obj_data['name']
        Clock.schedule_once(self.close_tooltip, 3)

    def on_touch_move(self, touch):
        if GV.OBJ_MODIFY:
            if touch.grab_current is self:
                self.x = touch.x - 25
                self.y = touch.y - 25
                self.rotate_btn.x = self.x + 55
                self.rotate_btn.y = self.y + 40
                self.tooltip.x = self.x + 25
                self.tooltip.y = self.y + 55
        else:
            return

    def on_release(self):
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj_data['_id'])}, {'$set': {'posX': self.x, 'posY': self.y}})

    def rotate_obj(self, instance):
        cursor = GV.DB_OBJECTLIST.find_one({'_id': ObjectId(self.obj_data['_id'])})
        angle_set = cursor['rotate']
        if angle_set == 0:
            self.angle_obj = 90
        elif angle_set == 90:
            self.angle_obj = 180
        elif angle_set == 180:
            self.angle_obj = 270
        elif angle_set == 270:
            self.angle_obj = 0
        GV.DB_OBJECTLIST.update_one({'_id': ObjectId(self.obj_data['_id'])}, {'$set': {'rotate': self.angle_obj}})


class ObjBntRotate(Button):
    obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ObjBntRotate, self).__init__(**kwargs)

    def rotate_obj(self):
        self.obj.rotate_obj(self)


class ObjTooltip(Label):
    pass


class ObjectApp(App):
    def build(self):
        return ObjHL()


if __name__ == '__main__':
    ObjectApp().run()