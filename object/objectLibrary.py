from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.graphics import Line, Rectangle, Ellipse, Color, Triangle, Rotate, Point, Bezier, Quad, Mesh
from kivy.properties import StringProperty, ListProperty, ObjectProperty, BooleanProperty, NumericProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.clock import Clock

from bson import ObjectId

import utility.gvar as GV


class ObjPLCM(Button):
    scatter_obj = ObjectProperty(None)
    obj_data = ObjectProperty(None)
    rotate_btn = ObjectProperty(None)
    angle_obj = NumericProperty(0)
    tooltip_show = False

    def __init__(self, **kwargs):
        super(ObjPLCM, self).__init__(**kwargs)
        self.tooltip = ObjTooltip()

    def on_press(self):
        self.scatter_obj.do_translation = (False, False)
        if not self.tooltip_show:
            self.display_tooltip()
            self.tooltip_show = True

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
        cursor = GV.DB_OBJECTLIST.find_one({'_id': ObjectId(instance.obj_data['_id'])})
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
        self.scatter_obj.remove_widget(self.tooltip)
        self.tooltip_show = False

    def display_tooltip(self, *args):
        self.tooltip.pos = (self.x + 7, self.y + 55)
        self.tooltip.text = self.obj_data['name']
        self.scatter_obj.add_widget(self.tooltip)
        Clock.schedule_once(self.close_tooltip, 3)


class ObjPLCZ(Button):
    scatter_obj = ObjectProperty(None)
    obj_data = ObjectProperty(None)
    rotate_btn = ObjectProperty(None)
    angle_obj = NumericProperty(0)
    tooltip_show = False

    def __init__(self, **kwargs):
        super(ObjPLCZ, self).__init__(**kwargs)
        self.tooltip = ObjTooltip()

    def on_press(self):
        self.scatter_obj.do_translation = (False, False)
        if not self.tooltip_show:
            self.display_tooltip()
            self.tooltip_show = True

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
        cursor = GV.DB_OBJECTLIST.find_one({'_id': ObjectId(instance.obj_data['_id'])})
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
        self.scatter_obj.remove_widget(self.tooltip)
        self.tooltip_show = False

    def display_tooltip(self, *args):
        self.tooltip.pos = (self.x + 7, self.y + 55)
        self.tooltip.text = self.obj_data['name']
        self.scatter_obj.add_widget(self.tooltip)
        Clock.schedule_once(self.close_tooltip, 3)


class ObjHL(Button):
    scatter_obj = ObjectProperty(None)
    obj_data = ObjectProperty(None)
    rotate_btn = ObjectProperty(None)
    angle_obj = NumericProperty(0)
    tooltip_show = False

    def __init__(self, **kwargs):
        super(ObjHL, self).__init__(**kwargs)
        self.tooltip = ObjTooltip()

    def on_press(self):
        self.scatter_obj.do_translation = (False, False)
        if not self.tooltip_show:
            self.display_tooltip()
            self.tooltip_show = True

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
        cursor = GV.DB_OBJECTLIST.find_one({'_id': ObjectId(instance.obj_data['_id'])})
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
        self.scatter_obj.remove_widget(self.tooltip)
        self.tooltip_show = False

    def display_tooltip(self, *args):
        self.tooltip.pos = (self.x + 15, self.y + 55)
        self.tooltip.text = self.obj_data['name']
        self.scatter_obj.add_widget(self.tooltip)
        Clock.schedule_once(self.close_tooltip, 3)


class ObjBntRotate(Button):
    obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ObjBntRotate, self).__init__(**kwargs)


class ObjTooltip(Label):
    pass


class ObjectApp(App):
    def build(self):
        return ObjHL()


if __name__ == '__main__':
    ObjectApp().run()