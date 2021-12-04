from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty, ObjectProperty
import utility.gvar as GV
from bson import ObjectId
import json
from pymodbus.client.sync import ModbusSerialClient
from datetime import datetime
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.behaviors import FocusBehavior
from utility.TCPServer import create_server
from utility.udpServer import create_server_udp
import threading

Builder.load_file('main/classi/testing.kv')


# ----- Classe del LAYOUT principale --------------------------------------------------------------------------------- #
class TestingScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.ts_container.tsc_output_table.get_list()

    def on_pre_leave(self, *args):
        self.ts_container.tsc_output_table.del_list()


class TestingContainer(RelativeLayout):
    pass


# ----- Classe del contenitore degli OUTPUT da testare --------------------------------------------------------------- #
class OutputTestingListBox(GridLayout):
    child_sx = ObjectProperty(None, allownone=True)
    child_dx = ObjectProperty(None, allownone=True)
    child_both = ObjectProperty(None, allownone=True)

    def del_list(self):
        self.clear_widgets()
        self.tsc_name.text = '???'
        self.tsc_address.text = '???'
        self.tsc_plc.text = '???'
        self.tsc_com.text = '???'
        self.tsc_handles.text = '???'
        if self.tsc_start_btn.text == 'Stop Test':
            self.tsc_start_btn.start_test()
        self.tsc_start_btn.disabled = True
        self.tsc_start_btn.opacity = 0

    def get_list(self):
        number = 0
        for item in GV.DB_OUTPUTLIST.find({'port': {'$gt': 0}}):
            self.layout = OutputTestingRow(obj_box=item, group='row')
            self.layout.add_widget(OutputTestLabel(text=str(number), size=(80, 30)))
            self.layout.add_widget(OutputTestLabel(text=item['name'], size=(150, 30)))
            self.layout.add_widget(OutputTestLabel(text=item['description'], size=(300, 30)))
            self.layout.add_widget(OutputTestLabel(text=item['plc'], size=(150, 30)))
            self.layout.add_widget(OutputTestLabel(text=str(item['port']), size=(150, 30)))
            self.layout.add_widget(OutputCheckBox(group='test', obj_box=item, name='SX', disabled=True))
            self.layout.add_widget(LabelCheckBox(text='SX', size=(110, 30)))
            self.layout.add_widget(OutputCheckBox(group='test', obj_box=item, name='DX', disabled=True))
            self.layout.add_widget(LabelCheckBox(text='DX', size=(110, 30)))
            self.layout.add_widget(OutputCheckBox(group='test', obj_box=item, name='BOTH', disabled=True))
            self.layout.add_widget(LabelCheckBox(text='BOTH', size=(110, 30)))
            self.add_widget(self.layout)
            number += 1


# ----- Classe layout contenente le linee degli OUTPUT da testare ---------------------------------------------------- #
class OutputTestingRow(ToggleButtonBehavior, BoxLayout):
    obj_box = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(OutputTestingRow, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = 1, None
        self.height = 30

    def on_press(self):
        if self.state == 'down':
            self.parent.tsc_name.text = self.obj_box['name']
            self.parent.tsc_address.text = self.obj_box['address']
            self.parent.tsc_plc.text = self.obj_box['plc']
            self.parent.tsc_com.text = str(self.obj_box['port'])
            if self.parent.child_sx is not None:
                self.parent.child_sx.disabled = True
                self.parent.child_dx.disabled = True
                self.parent.child_both.disabled = True
                self.parent.child_sx.active = False
                self.parent.child_dx.active = False
                self.parent.child_both.active = False
                self.parent.tsc_handles.text = '???'
                self.parent.tsc_start_btn.disabled = True
                self.parent.tsc_start_btn.opacity = 0
            for child in self.children:
                if child.name == 'SX':
                    child.disabled = False
                    self.parent.child_sx = child
                if child.name == 'DX':
                    child.disabled = False
                    self.parent.child_dx = child
                if child.name == 'BOTH':
                    child.disabled = False
                    self.parent.child_both = child
        else:
            self.parent.tsc_name.text = '???'
            self.parent.tsc_address.text = '???'
            self.parent.tsc_plc.text = '???'
            self.parent.tsc_com.text = '???'
            for child in self.children:
                if child.name == 'SX':
                    child.disabled = True
                    child.active = False
                if child.name == 'DX':
                    child.disabled = True
                    child.active = False
                if child.name == 'BOTH':
                    child.disabled = True
                    child.active = False
            self.parent.child_sx = None
            self.parent.child_dx = None
            self.parent.child_both = None
            self.parent.tsc_handles.text = '???'
            self.parent.tsc_start_btn.disabled = True
            self.parent.tsc_start_btn.opacity = 0


# ----- Classe dei pulsanti generati all'interno della riga output --------------------------------------------------- #
class LabelCheckBox(Label):
    name = StringProperty('')
    pass


class OutputCheckBox(CheckBox):
    obj_box = ObjectProperty(None)
    name = StringProperty('')

    def on_press(self):
        if self.active:
            self.parent.parent.tsc_handles.text = self.name
            self.parent.parent.tsc_start_btn.disabled = False
            self.parent.parent.tsc_start_btn.opacity = 1
        else:
            self.parent.parent.tsc_handles.text = '???'
            self.parent.parent.tsc_start_btn.disabled = True
            self.parent.parent.tsc_start_btn.opacity = 0


class OutputTestLabel(Label):
    name = StringProperty('')
    pass


# ----- Classe per i pulsanti di test degli output ------------------------------------------------------------------- #
class StartTestingButton(Button):

    def start_test(self):
        if self.text == 'Start Test':
            self.text = 'Stop Test'
            self.tsc_output_table.disabled = True
            self.create_command(on=True)
        else:
            self.text = 'Start Test'
            self.tsc_output_table.disabled = False
            self.create_command(on=False)

    def create_command(self, on):
        if self.tsc_handles.text == 'SX':
            hl = '1'
        if self.tsc_handles.text == 'DX':
            hl = '2'
        if self.tsc_handles.text == 'BOTH':
            hl = '0'
        if on:
            send_command = GV.BEGIN + self.tsc_address.text + GV.TEST + hl + GV.END
            print(send_command)
        else:
            send_command = GV.BEGIN + self.tsc_address.text + GV.OFF + GV.END
        message = create_server_udp(plc=self.tsc_plc.text, com=self.tsc_com.text, msg=send_command)
        while message[0].decode(GV.FORMAT) != (self.tsc_com.text + send_command):
            message = create_server_udp(plc=self.tsc_plc.text, com=self.tsc_com.text, msg=send_command)