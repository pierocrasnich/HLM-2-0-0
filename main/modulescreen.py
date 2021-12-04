from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner, SpinnerOption
import utility.gvar as GV
from kivy.utils import get_color_from_hex

Builder.load_file('main/classi/module.kv')


# ----- DashScreen Main Class ---------------------------------------------------------------------------------------- #
class ModuleScreen(Screen):
    mccm = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.ms_container.msc_module_container.update_library()

    def on_pre_leave(self, *args):
        self.ms_container.msc_module_container.clear_library()


# ----- Dashboard Container Layout ----------------------------------------------------------------------------------- #
class DashContainer(RelativeLayout):
    pass


# ----- Module Library Container ------------------------------------------------------------------------------------- #
class ModuleLibraryStack(StackLayout):

    def __init__(self, **kwargs):
        super(ModuleLibraryStack, self).__init__(**kwargs)
        self.module_label = None

    def populate_container(self):
        for item in GV.DB_MODULECONFIG.find({}):
            self.module_label = ModuleLabel(text=item['name'], obj=item)
            self.add_widget(self.module_label)

    def clear_library(self):
        self.clear_widgets()

    def update_library(self):
        self.clear_library()
        self.populate_container()


# ----- Module Label for library ------------------------------------------------------------------------------------- #
class ModuleLabel(ButtonBehavior, Label):
    obj = ObjectProperty(None)

    def on_press(self):
        if self.obj['name'] != self.parent.msc_module_map_name.text:
            self.parent.mscmm_image.source = GV.DIR_IMAGES + str(self.obj['bit']) + '.png'
            self.parent.msc_module_map.enable_label()
            self.parent.msc_module_map_name.text = self.obj['name']
            self.parent.msc_module_map.update_container(self.obj)
            self.parent.msc_module_del_btn.obj = self.obj
            self.parent.msc_module_edit_btn.obj = self.obj
        else:
            self.parent.msc_module_map.disable_label()
            self.parent.msc_module_map.clear_container()
            self.parent.msc_module_del_btn.obj = None
            self.parent.msc_module_edit_btn.obj = None


# ----- Module Map Container ----------------------------------------------------------------------------------------- #
class ModuleMapContainer(RelativeLayout):

    def clear_container(self):
        self.mscmm_widget.clear_widgets()

    def update_container(self, obj):
        self.clear_container()
        self.populate_container(obj)

    def populate_container(self, obj):
        max_height = 815
        for bit in range(obj['bit']):
            if obj['rules'][bit]['function']:
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['bit']), pos=(25, max_height))
                self.mscmm_widget.add_widget( self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['SX'])[0], pos=(540, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['SX'])[1:7], pos=(580, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.color_widget = ColorWidget(
                    color_bk=(get_color_from_hex(obj['rules'][bit]['SX'][1:7])),
                    pos=(635, max_height + 2))
                self.mscmm_widget.add_widget(self.mscmm_widget.color_widget)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['SX'])[7], pos=(675, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['SX'])[8], pos=(725, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['DX'])[0], pos=(830, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['DX'])[1:7], pos=(870, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.color_widget = ColorWidget(
                    color_bk=(get_color_from_hex(obj['rules'][bit]['DX'][1:7])),
                    pos=(925, max_height + 2))
                self.mscmm_widget.add_widget(self.mscmm_widget.color_widget)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['DX'])[7], pos=(965, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=str(obj['rules'][bit]['DX'])[8], pos=(1015, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
                self.mscmm_widget.map_label = BitLabel(text=obj['rules'][bit]['function'], pos=(85, max_height))
                self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
            max_height -= 22
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['SX'])[0], pos=(80, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['SX'])[1:7], pos=(120, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.color_widget = ColorWidget(color_bk=(get_color_from_hex(obj['normal']['SX'][1:7])),
                                                     pos=(175, 22))
        self.mscmm_widget.add_widget(self.mscmm_widget.color_widget)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['SX'])[7], pos=(215, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['SX'])[8], pos=(265, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['DX'])[0], pos=(360, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['DX'])[1:7], pos=(400, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.color_widget = ColorWidget(color_bk=(get_color_from_hex(obj['normal']['DX'][1:7])),
                                                     pos=(455, 22))
        self.mscmm_widget.add_widget(self.mscmm_widget.color_widget)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['DX'])[7], pos=(495, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)
        self.mscmm_widget.map_label = BitLabel(text=str(obj['normal']['DX'])[8], pos=(545, 20))
        self.mscmm_widget.add_widget(self.mscmm_widget.map_label)

    def disable_label(self):
        self.mscmm_image.opacity = 0
        self.mscmm_image.source = ''
        self.msc_bit_label.opacity = 0
        self.msc_function_label.opacity = 0
        self.msc_sx_label.opacity = 0
        self.msc_dx_label.opacity = 0
        self.msc_sx_color_label.opacity = 0
        self.msc_dx_color_label.opacity = 0
        self.msc_sx_flash_label.opacity = 0
        self.msc_dx_flash_label.opacity = 0
        self.msc_sx_power_label.opacity = 0
        self.msc_dx_power_label.opacity = 0
        self.msc_sx_normal_label.opacity = 0
        self.msc_dx_normal_label.opacity = 0
        self.msc_module_map_name.text = ''

    def enable_label(self):
        self.mscmm_image.opacity = 1
        self.msc_bit_label.opacity = 1
        self.msc_function_label.opacity = 1
        self.msc_sx_label.opacity = 1
        self.msc_dx_label.opacity = 1
        self.msc_sx_color_label.opacity = 1
        self.msc_dx_color_label.opacity = 1
        self.msc_sx_flash_label.opacity = 1
        self.msc_dx_flash_label.opacity = 1
        self.msc_sx_power_label.opacity = 1
        self.msc_dx_power_label.opacity = 1
        self.msc_sx_normal_label.opacity = 1
        self.msc_dx_normal_label.opacity = 1


# ----- Add Module Button -------------------------------------------------------------------------------------------- #
class AddModuleBtn(Button):

    def add_module(self):
        if self.msc_module_container.disabled:
            self.msc_module_container.disabled = False
            self.mscmm_module.disabled = True
            self.mscmm_module.opacity = 0
        else:
            self.msc_module_container.disabled = True
            self.msc_module_map.clear_container()
            self.msc_module_map.disable_label()
            self.mscmm_module.disabled = False
            self.mscmm_module.opacity = 1


# ----- Edit Module Button ------------------------------------------------------------------------------------------- #
class EditModuleBtn(Button):
    obj = ObjectProperty(None, allownone=True)

    def edit_module(self):
        if self.obj is not None:
            self.msc_module_container.disabled = True
            self.msc_module_map.clear_container()
            self.msc_module_map.disable_label()
            self.mscmm_module.disabled = False
            self.msc_module_add_btn.disabled = True
            self.mscmm_module.opacity = 1
            self.mscmmm_save.obj = self.obj
            self.mscmmm_save.bit = self.obj['bit']
            self.mscmmm_cancel.obj = self.obj
            self.mscmmm_cancel.disabled = False
            self.mscmmm_bit_container1.obj = self.obj
            self.mscmmm_bit_container8.obj = self.obj
            self.mscmmm_bit_container16.obj = self.obj
            self.mscmmm_bit_container32.obj = self.obj
            self.mscmmm_name.text = self.obj['name']
            self.mscmmm_system.text = self.obj['system']
            self.mscmmm_bit.text = str(self.obj['bit'])
            if self.obj['bit'] == 1:
                self.mscmmm_bit_container1.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container1.compile_bit()
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, -5000)
                self.mscmmm_bit_container16.pos = (5, -5000)
                self.mscmmm_bit_container32.pos = (5, -5000)
            elif self.obj['bit'] == 8:
                self.mscmmm_bit_container1.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container1.compile_bit()
                self.mscmmm_bit_container8.update_bit()
                self.mscmmm_bit_container8.populate_bit()
                self.mscmmm_bit_container8.compile_bit()
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, 5)
                self.mscmmm_bit_container16.pos = (5, -5000)
                self.mscmmm_bit_container32.pos = (5, -5000)
            elif self.obj['bit'] == 16:
                self.mscmmm_bit_container1.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container1.compile_bit()
                self.mscmmm_bit_container8.update_bit()
                self.mscmmm_bit_container8.populate_bit()
                self.mscmmm_bit_container8.compile_bit()
                self.mscmmm_bit_container16.update_bit()
                self.mscmmm_bit_container16.populate_bit()
                self.mscmmm_bit_container16.compile_bit()
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, 5)
                self.mscmmm_bit_container16.pos = (5, 5)
                self.mscmmm_bit_container32.pos = (5, -5000)
            else:
                self.mscmmm_bit_container1.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container1.compile_bit()
                self.mscmmm_bit_container8.update_bit()
                self.mscmmm_bit_container8.populate_bit()
                self.mscmmm_bit_container8.compile_bit()
                self.mscmmm_bit_container16.update_bit()
                self.mscmmm_bit_container16.populate_bit()
                self.mscmmm_bit_container16.compile_bit()
                self.mscmmm_bit_container32.update_bit()
                self.mscmmm_bit_container32.populate_bit()
                self.mscmmm_bit_container32.compile_bit()
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, 5)
                self.mscmmm_bit_container16.pos = (5, 5)
                self.mscmmm_bit_container32.pos = (5, 5)


# ----- Del Module Button -------------------------------------------------------------------------------------------- #
class DelModuleBtn(Button):
    obj = ObjectProperty(None, allownone=True)

    def del_module(self):
        if self.obj is not None:
            GV.DB_MODULECONFIG.delete_one({'_id': self.obj['_id']})
            GV.DB_CONNECTIONLIST.delete_many({'moduleID': self.obj['_id']})
            msg_color = 'success'
            msg_text = 'Remove module ' + self.obj['name'] + ' success'
            self.parent.parent.mccm.mm_notification.notification_msg(msg_color, msg_text)
        self.obj = None
        self.msc_module_map.disable_label()
        self.msc_module_map.clear_container()
        self.msc_module_edit_btn.obj = None
        self.msc_module_container.update_library()


# ----- ModuleMapLabel Defaul Label ---------------------------------------------------------------------------------- #
class ModuleMapLabel(Label):
    pass


# ----- Color Widget ------------------------------------------------------------------------------------------------- #
class ColorWidget(RelativeLayout):
    color_bk = ListProperty([0, 0, 0, 0])


# ----- Label Object for rules register ------------------------------------------------------------------------------ #
class BitLabel(Label):
    pass


# ---- Module Add/Edit Label ----------------------------------------------------------------------------------------- #
class ModuleEditLabel(Label):
    pass


# ----- Module TextInput Name ---------------------------------------------------------------------------------------- #
class ModuleEditTextInput(TextInput):

    def on_text_validate(self):
        name_module = [item['name'] for item in GV.DB_MODULECONFIG.find({})]
        if self.text in name_module:
            self.text = ''
        else:
            self.mscmmm_system.disabled = False
            self.disabled = True
            self.mscmmm_cancel.disabled = False
            self.text = self.text.upper()

    def on_focus(self, instance, value):
        if not value:
            self.on_text_validate()


# ----- Class Text Input for function -------------------------------------------------------------------------------- #
class FunctionTextInput(TextInput):

    def on_text_validate(self):
        self.text = self.text.upper()

    def on_focus(self, instance, value):
        if not value:
            self.on_text_validate()


# ----- Class Text Input for Color ----------------------------------------------------------------------------------- #
class ColorTextInput(TextInput):
    pat = ListProperty(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])

    def on_text_validate(self):
        if len(self.text) > 6:
            self.text = self.text[:6]
        elif len(self.text) < 6:
            self.text = '000000'
        self.text = self.text.upper()
        for i in range(len(self.text)):
            if self.text[i] not in self.pat:
                self.text = '000000'
                break
        if self.text != '000000':
            self.background_color = get_color_from_hex(self.text)
        else:
            self.background_color = [1, 1, 1, 1]

    def on_focus(self, instance, value):
        if not value:
            self.on_text_validate()


# ----- Module Add/Edit Spinner -------------------------------------------------------------------------------------- #
class ModuleEditSpinner(Spinner):

    def __init__(self, **kwargs):
        super(ModuleEditSpinner, self).__init__(**kwargs)
        self.option_cls = ModuleEditSpinnerOption

    def enable_bit(self):
        if self.text == 'DI':
            self.mscmmm_bit.values = ['1']
        else:
            self.mscmmm_bit.values = GV.REG_TYPE
        self.mscmmm_bit.disabled = False
        self.disabled = True

    def load_module_interface(self):
        if self.text != 'Bit...':
            if self.text == '1':
                self.mscmmm_bit_container1.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, -5000)
                self.mscmmm_bit_container16.pos = (5, -5000)
                self.mscmmm_bit_container32.pos = (5, -5000)
            elif self.text == '8':
                self.mscmmm_bit_container8.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container8.populate_bit()
                self.mscmmm_bit_container8.pos = (5, 5)
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container16.pos = (5, -5000)
                self.mscmmm_bit_container32.pos = (5, -5000)
            elif self.text == '16':
                self.mscmmm_bit_container16.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container8.populate_bit()
                self.mscmmm_bit_container16.populate_bit()
                self.mscmmm_bit_container16.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, 5)
                self.mscmmm_bit_container1.pos = (5, 5)
                self.mscmmm_bit_container32.pos = (5, -5000)
            else:
                self.mscmmm_bit_container32.update_bit()
                self.mscmmm_bit_container1.populate_bit()
                self.mscmmm_bit_container8.populate_bit()
                self.mscmmm_bit_container16.populate_bit()
                self.mscmmm_bit_container32.populate_bit()
                self.mscmmm_bit_container32.pos = (5, 5)
                self.mscmmm_bit_container8.pos = (5, 5)
                self.mscmmm_bit_container16.pos = (5, 5)
                self.mscmmm_bit_container1.pos = (5, 5)
            self.disabled = True
            self.mscmmm_save.bit = int(self.text)
            self.mscmmm_save.disabled = False
            self.mscmmm_save.opacity = 1


class ModuleEditSpinnerOption(SpinnerOption):
    pass


class ModuleEditBitSpinner(Spinner):
    ref = NumericProperty(None, allownone=True)
    data = StringProperty('')

    def __init__(self, **kwargs):
        super(ModuleEditBitSpinner, self).__init__(**kwargs)
        self.option_cls = ModuleEditBitSpinnerOption


class ModuleEditBitSpinnerOption(SpinnerOption):
    pass


# ----- Relative Layout Module Edit Bit Container 1 BIT -------------------------------------------------------------- #
class ModuleEditBitContainer1(RelativeLayout):
    obj = ObjectProperty(None, allownone=True)
    flash = ListProperty()
    power = ListProperty()

    def reset_bit(self):
        self.sx_normal.text = ''
        self.dx_normal.text = ''
        self.sx_flash.text = '...'
        self.dx_flash.text = '...'
        self.sx_power.text = '...'
        self.dx_power.text = '...'
        self.function0.text = ''
        self.sx_color0.text = ''
        self.sx_flash0.text = '...'
        self.sx_power0.text = '...'
        self.dx_color0.text = ''
        self.dx_flash0.text = '...'
        self.dx_power0.text = '...'

    def compile_bit(self):
        self.sx_normal.text = str(self.obj['normal']['SX'])[1:7]
        self.dx_normal.text = str(self.obj['normal']['DX'])[1:7]
        self.sx_flash.text = self.return_flash(str(self.obj['normal']['SX'])[7])
        self.dx_flash.text = self.return_flash(str(self.obj['normal']['DX'])[7])
        self.sx_power.text = self.return_power(str(self.obj['normal']['SX'])[8])
        self.dx_power.text = self.return_power(str(self.obj['normal']['DX'])[8])
        self.function0.text = self.obj['rules'][0]['function']
        self.sx_color0.text = str(self.obj['rules'][0]['SX'])[1:7]
        self.sx_flash0.text = self.return_flash(str(self.obj['rules'][0]['SX'])[7])
        self.sx_power0.text = self.return_power(str(self.obj['rules'][0]['SX'])[8])
        self.dx_color0.text = str(self.obj['rules'][0]['DX'])[1:7]
        self.dx_flash0.text = self.return_flash(str(self.obj['rules'][0]['DX'])[7])
        self.dx_power0.text = self.return_power(str(self.obj['rules'][0]['DX'])[8])
        self.return_color()

    def return_color(self):
        self.sx_normal.background_color = get_color_from_hex(str(self.obj['normal']['SX'])[1:7])
        self.dx_normal.background_color = get_color_from_hex(str(self.obj['normal']['DX'])[1:7])
        self.sx_color0.background_color = get_color_from_hex(str(self.obj['rules'][0]['SX'])[1:7])
        self.dx_color0.background_color = get_color_from_hex(str(self.obj['rules'][0]['DX'])[1:7])

    def return_flash(self, value):
        for item in GV.HL_FLASH:
            if item['value'] == value:
                return item['type']

    def return_power(self, value):
        for item in GV.HL_POWER:
            if item['value'] == value:
                return item['type']

    def update_bit(self):
        self.populate_bit()

    def populate_bit(self):
        self.flash = [item['type'] for item in GV.HL_FLASH]
        self.power = [item['type'] for item in GV.HL_POWER]


# ----- Relative Layout Module Edit Bit Container 8 BIT -------------------------------------------------------------- #
class ModuleEditBitContainer8(RelativeLayout):
    obj = ObjectProperty(None, allownone=True)
    flash = ListProperty()
    power = ListProperty()

    def reset_bit(self):
        self.function1.text = ''
        self.sx_color1.text = ''
        self.sx_flash1.text = '...'
        self.sx_power1.text = '...'
        self.dx_color1.text = ''
        self.dx_flash1.text = '...'
        self.dx_power1.text = '...'
        self.function2.text = ''
        self.sx_color2.text = ''
        self.sx_flash2.text = '...'
        self.sx_power2.text = '...'
        self.dx_color2.text = ''
        self.dx_flash2.text = '...'
        self.dx_power2.text = '...'
        self.function3.text = ''
        self.sx_color3.text = ''
        self.sx_flash3.text = '...'
        self.sx_power3.text = '...'
        self.dx_color3.text = ''
        self.dx_flash3.text = '...'
        self.dx_power3.text = '...'
        self.function4.text = ''
        self.sx_color4.text = ''
        self.sx_flash4.text = '...'
        self.sx_power4.text = '...'
        self.dx_color4.text = ''
        self.dx_flash4.text = '...'
        self.dx_power4.text = '...'
        self.function5.text = ''
        self.sx_color5.text = ''
        self.sx_flash5.text = '...'
        self.sx_power5.text = '...'
        self.dx_color5.text = ''
        self.dx_flash5.text = '...'
        self.dx_power5.text = '...'
        self.function6.text = ''
        self.sx_color6.text = ''
        self.sx_flash6.text = '...'
        self.sx_power6.text = '...'
        self.dx_color6.text = ''
        self.dx_flash6.text = '...'
        self.dx_power6.text = '...'
        self.function7.text = ''
        self.sx_color7.text = ''
        self.sx_flash7.text = '...'
        self.sx_power7.text = '...'
        self.dx_color7.text = ''
        self.dx_flash7.text = '...'
        self.dx_power7.text = '...'

    def compile_bit(self):
        self.function1.text = str(self.obj['rules'][1]['function'])
        self.sx_color1.text = str(self.obj['rules'][1]['SX'])[1:7]
        self.sx_flash1.text = self.return_flash(str(self.obj['rules'][1]['SX'])[7])
        self.sx_power1.text = self.return_power(str(self.obj['rules'][1]['SX'])[8])
        self.dx_color1.text = str(self.obj['rules'][1]['DX'])[1:7]
        self.dx_flash1.text = self.return_flash(str(self.obj['rules'][1]['DX'])[7])
        self.dx_power1.text = self.return_power(str(self.obj['rules'][1]['DX'])[8])
        self.function2.text = str(self.obj['rules'][2]['function'])
        self.sx_color2.text = str(self.obj['rules'][2]['SX'])[1:7]
        self.sx_flash2.text = self.return_flash(str(self.obj['rules'][2]['SX'])[7])
        self.sx_power2.text = self.return_power(str(self.obj['rules'][2]['SX'])[8])
        self.dx_color2.text = str(self.obj['rules'][2]['DX'])[1:7]
        self.dx_flash2.text = self.return_flash(str(self.obj['rules'][2]['DX'])[7])
        self.dx_power2.text = self.return_power(str(self.obj['rules'][2]['DX'])[8])
        self.function3.text = str(self.obj['rules'][3]['function'])
        self.sx_color3.text = str(self.obj['rules'][3]['SX'])[1:7]
        self.sx_flash3.text = self.return_flash(str(self.obj['rules'][3]['SX'])[7])
        self.sx_power3.text = self.return_power(str(self.obj['rules'][3]['SX'])[8])
        self.dx_color3.text = str(self.obj['rules'][3]['DX'])[1:7]
        self.dx_flash3.text = self.return_flash(str(self.obj['rules'][3]['DX'])[7])
        self.dx_power3.text = self.return_power(str(self.obj['rules'][3]['DX'])[8])
        self.function4.text = str(self.obj['rules'][4]['function'])
        self.sx_color4.text = str(self.obj['rules'][4]['SX'])[1:7]
        self.sx_flash4.text = self.return_flash(str(self.obj['rules'][4]['SX'])[7])
        self.sx_power4.text = self.return_power(str(self.obj['rules'][4]['SX'])[8])
        self.dx_color4.text = str(self.obj['rules'][4]['DX'])[1:7]
        self.dx_flash4.text = self.return_flash(str(self.obj['rules'][4]['DX'])[7])
        self.dx_power4.text = self.return_power(str(self.obj['rules'][4]['DX'])[8])
        self.function5.text = str(self.obj['rules'][5]['function'])
        self.sx_color5.text = str(self.obj['rules'][5]['SX'])[1:7]
        self.sx_flash5.text = self.return_flash(str(self.obj['rules'][5]['SX'])[7])
        self.sx_power5.text = self.return_power(str(self.obj['rules'][5]['SX'])[8])
        self.dx_color5.text = str(self.obj['rules'][5]['DX'])[1:7]
        self.dx_flash5.text = self.return_flash(str(self.obj['rules'][5]['DX'])[7])
        self.dx_power5.text = self.return_power(str(self.obj['rules'][5]['DX'])[8])
        self.function6.text = str(self.obj['rules'][6]['function'])
        self.sx_color6.text = str(self.obj['rules'][6]['SX'])[1:7]
        self.sx_flash6.text = self.return_flash(str(self.obj['rules'][6]['SX'])[7])
        self.sx_power6.text = self.return_power(str(self.obj['rules'][6]['SX'])[8])
        self.dx_color6.text = str(self.obj['rules'][6]['DX'])[1:7]
        self.dx_flash6.text = self.return_flash(str(self.obj['rules'][6]['DX'])[7])
        self.dx_power6.text = self.return_power(str(self.obj['rules'][6]['DX'])[8])
        self.function7.text = str(self.obj['rules'][7]['function'])
        self.sx_color7.text = str(self.obj['rules'][7]['SX'])[1:7]
        self.sx_flash7.text = self.return_flash(str(self.obj['rules'][7]['SX'])[7])
        self.sx_power7.text = self.return_power(str(self.obj['rules'][7]['SX'])[8])
        self.dx_color7.text = str(self.obj['rules'][7]['DX'])[1:7]
        self.dx_flash7.text = self.return_flash(str(self.obj['rules'][7]['DX'])[7])
        self.dx_power7.text = self.return_power(str(self.obj['rules'][7]['DX'])[8])
        self.return_color()

    def return_color(self):
        self.sx_color1.background_color = get_color_from_hex(str(self.obj['rules'][1]['SX'])[1:7])
        self.dx_color1.background_color = get_color_from_hex(str(self.obj['rules'][1]['DX'])[1:7])
        self.sx_color2.background_color = get_color_from_hex(str(self.obj['rules'][2]['SX'])[1:7])
        self.dx_color2.background_color = get_color_from_hex(str(self.obj['rules'][2]['DX'])[1:7])
        self.sx_color3.background_color = get_color_from_hex(str(self.obj['rules'][3]['SX'])[1:7])
        self.dx_color3.background_color = get_color_from_hex(str(self.obj['rules'][3]['DX'])[1:7])
        self.sx_color4.background_color = get_color_from_hex(str(self.obj['rules'][4]['SX'])[1:7])
        self.dx_color4.background_color = get_color_from_hex(str(self.obj['rules'][4]['DX'])[1:7])
        self.sx_color5.background_color = get_color_from_hex(str(self.obj['rules'][5]['SX'])[1:7])
        self.dx_color5.background_color = get_color_from_hex(str(self.obj['rules'][5]['DX'])[1:7])
        self.sx_color6.background_color = get_color_from_hex(str(self.obj['rules'][6]['SX'])[1:7])
        self.dx_color6.background_color = get_color_from_hex(str(self.obj['rules'][6]['DX'])[1:7])
        self.sx_color7.background_color = get_color_from_hex(str(self.obj['rules'][7]['SX'])[1:7])
        self.dx_color7.background_color = get_color_from_hex(str(self.obj['rules'][7]['DX'])[1:7])


    def return_flash(self, value):
        for item in GV.HL_FLASH:
            if item['value'] == value:
                return item['type']

    def return_power(self, value):
        for item in GV.HL_POWER:
            if item['value'] == value:
                return item['type']

    def update_bit(self):
        self.populate_bit()

    def populate_bit(self):
        self.flash = [item['type'] for item in GV.HL_FLASH]
        self.power = [item['type'] for item in GV.HL_POWER]


# ----- Relative Layout Module Edit Bit Container 16 BIT ------------------------------------------------------------- #
class ModuleEditBitContainer16(RelativeLayout):
    obj = ObjectProperty(None, allownone=True)
    flash = ListProperty()
    power = ListProperty()

    def reset_bit(self):
        self.function8.text = ''
        self.sx_color8.text = ''
        self.sx_flash8.text = '...'
        self.sx_power8.text = '...'
        self.dx_color8.text = ''
        self.dx_flash8.text = '...'
        self.dx_power8.text = '...'
        self.function9.text = ''
        self.sx_color9.text = ''
        self.sx_flash9.text = '...'
        self.sx_power9.text = '...'
        self.dx_color9.text = ''
        self.dx_flash9.text = '...'
        self.dx_power9.text = '...'
        self.function10.text = ''
        self.sx_color10.text = ''
        self.sx_flash10.text = '...'
        self.sx_power10.text = '...'
        self.dx_color10.text = ''
        self.dx_flash10.text = '...'
        self.dx_power10.text = '...'
        self.function11.text = ''
        self.sx_color11.text = ''
        self.sx_flash11.text = '...'
        self.sx_power11.text = '...'
        self.dx_color11.text = ''
        self.dx_flash11.text = '...'
        self.dx_power11.text = '...'
        self.function12.text = ''
        self.sx_color12.text = ''
        self.sx_flash12.text = '...'
        self.sx_power12.text = '...'
        self.dx_color12.text = ''
        self.dx_flash12.text = '...'
        self.dx_power12.text = '...'
        self.function13.text = ''
        self.sx_color13.text = ''
        self.sx_flash13.text = '...'
        self.sx_power13.text = '...'
        self.dx_color13.text = ''
        self.dx_flash13.text = '...'
        self.dx_power13.text = '...'
        self.function14.text = ''
        self.sx_color14.text = ''
        self.sx_flash14.text = '...'
        self.sx_power14.text = '...'
        self.dx_color14.text = ''
        self.dx_flash14.text = '...'
        self.dx_power14.text = '...'
        self.function15.text = ''
        self.sx_color15.text = ''
        self.sx_flash15.text = '...'
        self.sx_power15.text = '...'
        self.dx_color15.text = ''
        self.dx_flash15.text = '...'
        self.dx_power15.text = '...'

    def compile_bit(self):
        self.function8.text = str(self.obj['rules'][8]['function'])
        self.sx_color8.text = str(self.obj['rules'][8]['SX'])[1:7]
        self.sx_flash8.text = self.return_flash(str(self.obj['rules'][8]['SX'])[7])
        self.sx_power8.text = self.return_power(str(self.obj['rules'][8]['SX'])[8])
        self.dx_color8.text = str(self.obj['rules'][8]['DX'])[1:7]
        self.dx_flash8.text = self.return_flash(str(self.obj['rules'][8]['DX'])[7])
        self.dx_power8.text = self.return_power(str(self.obj['rules'][8]['DX'])[8])
        self.function9.text = str(self.obj['rules'][9]['function'])
        self.sx_color9.text = str(self.obj['rules'][9]['SX'])[1:7]
        self.sx_flash9.text = self.return_flash(str(self.obj['rules'][9]['SX'])[7])
        self.sx_power9.text = self.return_power(str(self.obj['rules'][9]['SX'])[8])
        self.dx_color9.text = str(self.obj['rules'][9]['DX'])[1:7]
        self.dx_flash9.text = self.return_flash(str(self.obj['rules'][9]['DX'])[7])
        self.dx_power9.text = self.return_power(str(self.obj['rules'][9]['DX'])[8])
        self.function10.text = str(self.obj['rules'][10]['function'])
        self.sx_color10.text = str(self.obj['rules'][10]['SX'])[1:7]
        self.sx_flash10.text = self.return_flash(str(self.obj['rules'][10]['SX'])[7])
        self.sx_power10.text = self.return_power(str(self.obj['rules'][10]['SX'])[8])
        self.dx_color10.text = str(self.obj['rules'][10]['DX'])[1:7]
        self.dx_flash10.text = self.return_flash(str(self.obj['rules'][10]['DX'])[7])
        self.dx_power10.text = self.return_power(str(self.obj['rules'][10]['DX'])[8])
        self.function11.text = str(self.obj['rules'][11]['function'])
        self.sx_color11.text = str(self.obj['rules'][11]['SX'])[1:7]
        self.sx_flash11.text = self.return_flash(str(self.obj['rules'][11]['SX'])[7])
        self.sx_power11.text = self.return_power(str(self.obj['rules'][11]['SX'])[8])
        self.dx_color11.text = str(self.obj['rules'][11]['DX'])[1:7]
        self.dx_flash11.text = self.return_flash(str(self.obj['rules'][11]['DX'])[7])
        self.dx_power11.text = self.return_power(str(self.obj['rules'][11]['DX'])[8])
        self.function12.text = str(self.obj['rules'][12]['function'])
        self.sx_color12.text = str(self.obj['rules'][12]['SX'])[1:7]
        self.sx_flash12.text = self.return_flash(str(self.obj['rules'][12]['SX'])[7])
        self.sx_power12.text = self.return_power(str(self.obj['rules'][12]['SX'])[8])
        self.dx_color12.text = str(self.obj['rules'][12]['DX'])[1:7]
        self.dx_flash12.text = self.return_flash(str(self.obj['rules'][12]['DX'])[7])
        self.dx_power12.text = self.return_power(str(self.obj['rules'][12]['DX'])[8])
        self.function13.text = str(self.obj['rules'][13]['function'])
        self.sx_color13.text = str(self.obj['rules'][13]['SX'])[1:7]
        self.sx_flash13.text = self.return_flash(str(self.obj['rules'][13]['SX'])[7])
        self.sx_power13.text = self.return_power(str(self.obj['rules'][13]['SX'])[8])
        self.dx_color13.text = str(self.obj['rules'][13]['DX'])[1:7]
        self.dx_flash13.text = self.return_flash(str(self.obj['rules'][13]['DX'])[7])
        self.dx_power13.text = self.return_power(str(self.obj['rules'][13]['DX'])[8])
        self.function14.text = str(self.obj['rules'][14]['function'])
        self.sx_color14.text = str(self.obj['rules'][14]['SX'])[1:7]
        self.sx_flash14.text = self.return_flash(str(self.obj['rules'][14]['SX'])[7])
        self.sx_power14.text = self.return_power(str(self.obj['rules'][14]['SX'])[8])
        self.dx_color14.text = str(self.obj['rules'][14]['DX'])[1:7]
        self.dx_flash14.text = self.return_flash(str(self.obj['rules'][14]['DX'])[7])
        self.dx_power14.text = self.return_power(str(self.obj['rules'][14]['DX'])[8])
        self.function15.text = str(self.obj['rules'][15]['function'])
        self.sx_color15.text = str(self.obj['rules'][15]['SX'])[1:7]
        self.sx_flash15.text = self.return_flash(str(self.obj['rules'][15]['SX'])[7])
        self.sx_power15.text = self.return_power(str(self.obj['rules'][15]['SX'])[8])
        self.dx_color15.text = str(self.obj['rules'][15]['DX'])[1:7]
        self.dx_flash15.text = self.return_flash(str(self.obj['rules'][15]['DX'])[7])
        self.dx_power15.text = self.return_power(str(self.obj['rules'][15]['DX'])[8])
        self.return_color()

    def return_color(self):
        self.sx_color8.background_color = get_color_from_hex(str(self.obj['rules'][8]['SX'])[1:7])
        self.dx_color8.background_color = get_color_from_hex(str(self.obj['rules'][8]['DX'])[1:7])
        self.sx_color9.background_color = get_color_from_hex(str(self.obj['rules'][9]['SX'])[1:7])
        self.dx_color9.background_color = get_color_from_hex(str(self.obj['rules'][9]['DX'])[1:7])
        self.sx_color10.background_color = get_color_from_hex(str(self.obj['rules'][10]['SX'])[1:7])
        self.dx_color10.background_color = get_color_from_hex(str(self.obj['rules'][10]['DX'])[1:7])
        self.sx_color11.background_color = get_color_from_hex(str(self.obj['rules'][11]['SX'])[1:7])
        self.dx_color11.background_color = get_color_from_hex(str(self.obj['rules'][11]['DX'])[1:7])
        self.sx_color12.background_color = get_color_from_hex(str(self.obj['rules'][12]['SX'])[1:7])
        self.dx_color12.background_color = get_color_from_hex(str(self.obj['rules'][12]['DX'])[1:7])
        self.sx_color13.background_color = get_color_from_hex(str(self.obj['rules'][13]['SX'])[1:7])
        self.dx_color13.background_color = get_color_from_hex(str(self.obj['rules'][13]['DX'])[1:7])
        self.sx_color14.background_color = get_color_from_hex(str(self.obj['rules'][14]['SX'])[1:7])
        self.dx_color14.background_color = get_color_from_hex(str(self.obj['rules'][14]['DX'])[1:7])
        self.sx_color15.background_color = get_color_from_hex(str(self.obj['rules'][15]['SX'])[1:7])
        self.dx_color15.background_color = get_color_from_hex(str(self.obj['rules'][15]['DX'])[1:7])

    def return_flash(self, value):
        for item in GV.HL_FLASH:
            if item['value'] == value:
                return item['type']

    def return_power(self, value):
        for item in GV.HL_POWER:
            if item['value'] == value:
                return item['type']

    def update_bit(self):
        self.populate_bit()

    def populate_bit(self):
        self.flash = [item['type'] for item in GV.HL_FLASH]
        self.power = [item['type'] for item in GV.HL_POWER]


# ----- Relative Layout Module Edit Bit Container 32 BIT ------------------------------------------------------------- #
class ModuleEditBitContainer32(RelativeLayout):
    obj = ObjectProperty(None, allownone=True)
    flash = ListProperty()
    power = ListProperty()

    def reset_bit(self):
        self.function16.text = ''
        self.sx_color16.text = ''
        self.sx_flash16.text = '...'
        self.sx_power16.text = '...'
        self.dx_color16.text = ''
        self.dx_flash16.text = '...'
        self.dx_power16.text = '...'
        self.function17.text = ''
        self.sx_color17.text = ''
        self.sx_flash17.text = '...'
        self.sx_power17.text = '...'
        self.dx_color17.text = ''
        self.dx_flash17.text = '...'
        self.dx_power17.text = '...'
        self.function18.text = ''
        self.sx_color18.text = ''
        self.sx_flash18.text = '...'
        self.sx_power18.text = '...'
        self.dx_color18.text = ''
        self.dx_flash18.text = '...'
        self.dx_power18.text = '...'
        self.function19.text = ''
        self.sx_color19.text = ''
        self.sx_flash19.text = '...'
        self.sx_power19.text = '...'
        self.dx_color19.text = ''
        self.dx_flash19.text = '...'
        self.dx_power19.text = '...'
        self.function20.text = ''
        self.sx_color20.text = ''
        self.sx_flash20.text = '...'
        self.sx_power20.text = '...'
        self.dx_color20.text = ''
        self.dx_flash20.text = '...'
        self.dx_power20.text = '...'
        self.function21.text = ''
        self.sx_color21.text = ''
        self.sx_flash21.text = '...'
        self.sx_power21.text = '...'
        self.dx_color21.text = ''
        self.dx_flash21.text = '...'
        self.dx_power21.text = '...'
        self.function22.text = ''
        self.sx_color22.text = ''
        self.sx_flash22.text = '...'
        self.sx_power22.text = '...'
        self.dx_color22.text = ''
        self.dx_flash22.text = '...'
        self.dx_power22.text = '...'
        self.function23.text = ''
        self.sx_color23.text = ''
        self.sx_flash23.text = '...'
        self.sx_power23.text = '...'
        self.dx_color23.text = ''
        self.dx_flash23.text = '...'
        self.dx_power23.text = '...'
        self.function24.text = ''
        self.sx_color24.text = ''
        self.sx_flash24.text = '...'
        self.sx_power24.text = '...'
        self.dx_color24.text = ''
        self.dx_flash24.text = '...'
        self.dx_power24.text = '...'
        self.function25.text = ''
        self.sx_color25.text = ''
        self.sx_flash25.text = '...'
        self.sx_power25.text = '...'
        self.dx_color25.text = ''
        self.dx_flash25.text = '...'
        self.dx_power25.text = '...'
        self.function26.text = ''
        self.sx_color26.text = ''
        self.sx_flash26.text = '...'
        self.sx_power26.text = '...'
        self.dx_color26.text = ''
        self.dx_flash26.text = '...'
        self.dx_power26.text = '...'
        self.function27.text = ''
        self.sx_color27.text = ''
        self.sx_flash27.text = '...'
        self.sx_power27.text = '...'
        self.dx_color27.text = ''
        self.dx_flash27.text = '...'
        self.dx_power27.text = '...'
        self.function28.text = ''
        self.sx_color28.text = ''
        self.sx_flash28.text = '...'
        self.sx_power28.text = '...'
        self.dx_color28.text = ''
        self.dx_flash28.text = '...'
        self.dx_power28.text = '...'
        self.function29.text = ''
        self.sx_color29.text = ''
        self.sx_flash29.text = '...'
        self.sx_power29.text = '...'
        self.dx_color29.text = ''
        self.dx_flash29.text = '...'
        self.dx_power29.text = '...'
        self.function30.text = ''
        self.sx_color30.text = ''
        self.sx_flash30.text = '...'
        self.sx_power30.text = '...'
        self.dx_color30.text = ''
        self.dx_flash30.text = '...'
        self.dx_power30.text = '...'
        self.function31.text = ''
        self.sx_color31.text = ''
        self.sx_flash31.text = '...'
        self.sx_power31.text = '...'
        self.dx_color31.text = ''
        self.dx_flash31.text = '...'
        self.dx_power31.text = '...'

    def compile_bit(self):
        self.function16.text = str(self.obj['rules'][16]['function'])
        self.sx_color16.text = str(self.obj['rules'][16]['SX'])[1:7]
        self.sx_flash16.text = self.return_flash(str(self.obj['rules'][16]['SX'])[7])
        self.sx_power16.text = self.return_power(str(self.obj['rules'][16]['SX'])[8])
        self.dx_color16.text = str(self.obj['rules'][16]['DX'])[1:7]
        self.dx_flash16.text = self.return_flash(str(self.obj['rules'][16]['DX'])[7])
        self.dx_power16.text = self.return_power(str(self.obj['rules'][16]['DX'])[8])
        self.function17.text = str(self.obj['rules'][17]['function'])
        self.sx_color17.text = str(self.obj['rules'][17]['SX'])[1:7]
        self.sx_flash17.text = self.return_flash(str(self.obj['rules'][17]['SX'])[7])
        self.sx_power17.text = self.return_power(str(self.obj['rules'][17]['SX'])[8])
        self.dx_color17.text = str(self.obj['rules'][17]['DX'])[1:7]
        self.dx_flash17.text = self.return_flash(str(self.obj['rules'][17]['DX'])[7])
        self.dx_power17.text = self.return_power(str(self.obj['rules'][17]['DX'])[8])
        self.function18.text = str(self.obj['rules'][18]['function'])
        self.sx_color18.text = str(self.obj['rules'][18]['SX'])[1:7]
        self.sx_flash18.text = self.return_flash(str(self.obj['rules'][18]['SX'])[7])
        self.sx_power18.text = self.return_power(str(self.obj['rules'][18]['SX'])[8])
        self.dx_color18.text = str(self.obj['rules'][18]['DX'])[1:7]
        self.dx_flash18.text = self.return_flash(str(self.obj['rules'][18]['DX'])[7])
        self.dx_power18.text = self.return_power(str(self.obj['rules'][18]['DX'])[8])
        self.function19.text = str(self.obj['rules'][19]['function'])
        self.sx_color19.text = str(self.obj['rules'][19]['SX'])[1:7]
        self.sx_flash19.text = self.return_flash(str(self.obj['rules'][19]['SX'])[7])
        self.sx_power19.text = self.return_power(str(self.obj['rules'][19]['SX'])[8])
        self.dx_color19.text = str(self.obj['rules'][19]['DX'])[1:7]
        self.dx_flash19.text = self.return_flash(str(self.obj['rules'][19]['DX'])[7])
        self.dx_power19.text = self.return_power(str(self.obj['rules'][19]['DX'])[8])
        self.function20.text = str(self.obj['rules'][20]['function'])
        self.sx_color20.text = str(self.obj['rules'][20]['SX'])[1:7]
        self.sx_flash20.text = self.return_flash(str(self.obj['rules'][20]['SX'])[7])
        self.sx_power20.text = self.return_power(str(self.obj['rules'][20]['SX'])[8])
        self.dx_color20.text = str(self.obj['rules'][20]['DX'])[1:7]
        self.dx_flash20.text = self.return_flash(str(self.obj['rules'][20]['DX'])[7])
        self.dx_power20.text = self.return_power(str(self.obj['rules'][20]['DX'])[8])
        self.function21.text = str(self.obj['rules'][21]['function'])
        self.sx_color21.text = str(self.obj['rules'][21]['SX'])[1:7]
        self.sx_flash21.text = self.return_flash(str(self.obj['rules'][21]['SX'])[7])
        self.sx_power21.text = self.return_power(str(self.obj['rules'][21]['SX'])[8])
        self.dx_color21.text = str(self.obj['rules'][21]['DX'])[1:7]
        self.dx_flash21.text = self.return_flash(str(self.obj['rules'][21]['DX'])[7])
        self.dx_power21.text = self.return_power(str(self.obj['rules'][21]['DX'])[8])
        self.function22.text = str(self.obj['rules'][22]['function'])
        self.sx_color22.text = str(self.obj['rules'][22]['SX'])[1:7]
        self.sx_flash22.text = self.return_flash(str(self.obj['rules'][22]['SX'])[7])
        self.sx_power22.text = self.return_power(str(self.obj['rules'][22]['SX'])[8])
        self.dx_color22.text = str(self.obj['rules'][22]['DX'])[1:7]
        self.dx_flash22.text = self.return_flash(str(self.obj['rules'][22]['DX'])[7])
        self.dx_power22.text = self.return_power(str(self.obj['rules'][22]['DX'])[8])
        self.function23.text = str(self.obj['rules'][23]['function'])
        self.sx_color23.text = str(self.obj['rules'][23]['SX'])[1:7]
        self.sx_flash23.text = self.return_flash(str(self.obj['rules'][23]['SX'])[7])
        self.sx_power23.text = self.return_power(str(self.obj['rules'][23]['SX'])[8])
        self.dx_color23.text = str(self.obj['rules'][23]['DX'])[1:7]
        self.dx_flash23.text = self.return_flash(str(self.obj['rules'][23]['DX'])[7])
        self.dx_power23.text = self.return_power(str(self.obj['rules'][23]['DX'])[8])
        self.function24.text = str(self.obj['rules'][24]['function'])
        self.sx_color24.text = str(self.obj['rules'][24]['SX'])[1:7]
        self.sx_flash24.text = self.return_flash(str(self.obj['rules'][24]['SX'])[7])
        self.sx_power24.text = self.return_power(str(self.obj['rules'][24]['SX'])[8])
        self.dx_color24.text = str(self.obj['rules'][24]['DX'])[1:7]
        self.dx_flash24.text = self.return_flash(str(self.obj['rules'][24]['DX'])[7])
        self.dx_power24.text = self.return_power(str(self.obj['rules'][24]['DX'])[8])
        self.function25.text = str(self.obj['rules'][25]['function'])
        self.sx_color25.text = str(self.obj['rules'][25]['SX'])[1:7]
        self.sx_flash25.text = self.return_flash(str(self.obj['rules'][25]['SX'])[7])
        self.sx_power25.text = self.return_power(str(self.obj['rules'][25]['SX'])[8])
        self.dx_color25.text = str(self.obj['rules'][25]['DX'])[1:7]
        self.dx_flash25.text = self.return_flash(str(self.obj['rules'][25]['DX'])[7])
        self.dx_power25.text = self.return_power(str(self.obj['rules'][25]['DX'])[8])
        self.function26.text = str(self.obj['rules'][26]['function'])
        self.sx_color26.text = str(self.obj['rules'][26]['SX'])[1:7]
        self.sx_flash26.text = self.return_flash(str(self.obj['rules'][26]['SX'])[7])
        self.sx_power26.text = self.return_power(str(self.obj['rules'][26]['SX'])[8])
        self.dx_color26.text = str(self.obj['rules'][26]['DX'])[1:7]
        self.dx_flash26.text = self.return_flash(str(self.obj['rules'][26]['DX'])[7])
        self.dx_power26.text = self.return_power(str(self.obj['rules'][26]['DX'])[8])
        self.function27.text = str(self.obj['rules'][27]['function'])
        self.sx_color27.text = str(self.obj['rules'][27]['SX'])[1:7]
        self.sx_flash27.text = self.return_flash(str(self.obj['rules'][27]['SX'])[7])
        self.sx_power27.text = self.return_power(str(self.obj['rules'][27]['SX'])[8])
        self.dx_color27.text = str(self.obj['rules'][27]['DX'])[1:7]
        self.dx_flash27.text = self.return_flash(str(self.obj['rules'][27]['DX'])[7])
        self.dx_power27.text = self.return_power(str(self.obj['rules'][27]['DX'])[8])
        self.function28.text = str(self.obj['rules'][28]['function'])
        self.sx_color28.text = str(self.obj['rules'][28]['SX'])[1:7]
        self.sx_flash28.text = self.return_flash(str(self.obj['rules'][28]['SX'])[7])
        self.sx_power28.text = self.return_power(str(self.obj['rules'][28]['SX'])[8])
        self.dx_color28.text = str(self.obj['rules'][28]['DX'])[1:7]
        self.dx_flash28.text = self.return_flash(str(self.obj['rules'][28]['DX'])[7])
        self.dx_power28.text = self.return_power(str(self.obj['rules'][28]['DX'])[8])
        self.function29.text = str(self.obj['rules'][29]['function'])
        self.sx_color29.text = str(self.obj['rules'][29]['SX'])[1:7]
        self.sx_flash29.text = self.return_flash(str(self.obj['rules'][29]['SX'])[7])
        self.sx_power29.text = self.return_power(str(self.obj['rules'][29]['SX'])[8])
        self.dx_color29.text = str(self.obj['rules'][29]['DX'])[1:7]
        self.dx_flash29.text = self.return_flash(str(self.obj['rules'][29]['DX'])[7])
        self.dx_power29.text = self.return_power(str(self.obj['rules'][29]['DX'])[8])
        self.function30.text = str(self.obj['rules'][30]['function'])
        self.sx_color30.text = str(self.obj['rules'][30]['SX'])[1:7]
        self.sx_flash30.text = self.return_flash(str(self.obj['rules'][30]['SX'])[7])
        self.sx_power30.text = self.return_power(str(self.obj['rules'][30]['SX'])[8])
        self.dx_color30.text = str(self.obj['rules'][30]['DX'])[1:7]
        self.dx_flash30.text = self.return_flash(str(self.obj['rules'][30]['DX'])[7])
        self.dx_power30.text = self.return_power(str(self.obj['rules'][30]['DX'])[8])
        self.function31.text = str(self.obj['rules'][31]['function'])
        self.sx_color31.text = str(self.obj['rules'][31]['SX'])[1:7]
        self.sx_flash31.text = self.return_flash(str(self.obj['rules'][31]['SX'])[7])
        self.sx_power31.text = self.return_power(str(self.obj['rules'][31]['SX'])[8])
        self.dx_color31.text = str(self.obj['rules'][31]['DX'])[1:7]
        self.dx_flash31.text = self.return_flash(str(self.obj['rules'][31]['DX'])[7])
        self.dx_power31.text = self.return_power(str(self.obj['rules'][31]['DX'])[8])
        self.return_color()

    def return_color(self):
        self.sx_color16.background_color = get_color_from_hex(str(self.obj['rules'][16]['SX'])[1:7])
        self.dx_color16.background_color = get_color_from_hex(str(self.obj['rules'][16]['DX'])[1:7])
        self.sx_color17.background_color = get_color_from_hex(str(self.obj['rules'][17]['SX'])[1:7])
        self.dx_color17.background_color = get_color_from_hex(str(self.obj['rules'][17]['DX'])[1:7])
        self.sx_color18.background_color = get_color_from_hex(str(self.obj['rules'][18]['SX'])[1:7])
        self.dx_color18.background_color = get_color_from_hex(str(self.obj['rules'][18]['DX'])[1:7])
        self.sx_color19.background_color = get_color_from_hex(str(self.obj['rules'][19]['SX'])[1:7])
        self.dx_color19.background_color = get_color_from_hex(str(self.obj['rules'][19]['DX'])[1:7])
        self.sx_color20.background_color = get_color_from_hex(str(self.obj['rules'][20]['SX'])[1:7])
        self.dx_color20.background_color = get_color_from_hex(str(self.obj['rules'][20]['DX'])[1:7])
        self.sx_color21.background_color = get_color_from_hex(str(self.obj['rules'][21]['SX'])[1:7])
        self.dx_color21.background_color = get_color_from_hex(str(self.obj['rules'][21]['DX'])[1:7])
        self.sx_color22.background_color = get_color_from_hex(str(self.obj['rules'][22]['SX'])[1:7])
        self.dx_color22.background_color = get_color_from_hex(str(self.obj['rules'][22]['DX'])[1:7])
        self.sx_color23.background_color = get_color_from_hex(str(self.obj['rules'][23]['SX'])[1:7])
        self.dx_color23.background_color = get_color_from_hex(str(self.obj['rules'][23]['DX'])[1:7])
        self.sx_color24.background_color = get_color_from_hex(str(self.obj['rules'][24]['SX'])[1:7])
        self.dx_color24.background_color = get_color_from_hex(str(self.obj['rules'][24]['DX'])[1:7])
        self.sx_color25.background_color = get_color_from_hex(str(self.obj['rules'][25]['SX'])[1:7])
        self.dx_color25.background_color = get_color_from_hex(str(self.obj['rules'][25]['DX'])[1:7])
        self.sx_color26.background_color = get_color_from_hex(str(self.obj['rules'][26]['SX'])[1:7])
        self.dx_color26.background_color = get_color_from_hex(str(self.obj['rules'][26]['DX'])[1:7])
        self.sx_color27.background_color = get_color_from_hex(str(self.obj['rules'][27]['SX'])[1:7])
        self.dx_color27.background_color = get_color_from_hex(str(self.obj['rules'][27]['DX'])[1:7])
        self.sx_color28.background_color = get_color_from_hex(str(self.obj['rules'][28]['SX'])[1:7])
        self.dx_color28.background_color = get_color_from_hex(str(self.obj['rules'][28]['DX'])[1:7])
        self.sx_color29.background_color = get_color_from_hex(str(self.obj['rules'][29]['SX'])[1:7])
        self.dx_color29.background_color = get_color_from_hex(str(self.obj['rules'][29]['DX'])[1:7])
        self.sx_color30.background_color = get_color_from_hex(str(self.obj['rules'][30]['SX'])[1:7])
        self.dx_color30.background_color = get_color_from_hex(str(self.obj['rules'][30]['DX'])[1:7])
        self.sx_color31.background_color = get_color_from_hex(str(self.obj['rules'][31]['SX'])[1:7])
        self.dx_color31.background_color = get_color_from_hex(str(self.obj['rules'][31]['DX'])[1:7])

    def return_flash(self, value):
        for item in GV.HL_FLASH:
            if item['value'] == value:
                return item['type']

    def return_power(self, value):
        for item in GV.HL_POWER:
            if item['value'] == value:
                return item['type']

    def update_bit(self):
        self.populate_bit()

    def populate_bit(self):
        self.flash = [item['type'] for item in GV.HL_FLASH]
        self.power = [item['type'] for item in GV.HL_POWER]


# ----- Save Button Module Edit container ---------------------------------------------------------------------------- #
class ModuleEditSaveBtn(Button):
    obj = ObjectProperty(None, allownone=True)
    bit = NumericProperty(0)

    def save_bit(self):
        name = self.mscmmm_name.text
        system = self.mscmmm_system.text
        bit = int(self.mscmmm_bit.text)
        sx_normal = "&" + self.return_color(self.mscmmm_bit_container1.sx_normal.text) \
                    + self.return_flash(self.mscmmm_bit_container1.sx_flash.text) \
                    + self.return_power(self.mscmmm_bit_container1.sx_power.text)
        dx_normal = "&" + self.return_color(self.mscmmm_bit_container1.dx_normal.text) \
                    + self.return_flash(self.mscmmm_bit_container1.dx_flash.text) \
                    + self.return_power(self.mscmmm_bit_container1.dx_power.text)
        normal = {"SX": sx_normal, "DX": dx_normal}
        rules = []
        if self.bit == 1:
            self.create_rules1(rules)
        elif self.bit == 8:
            self.create_rules1(rules)
            self.create_rules8(rules)
        elif self.bit == 16:
            self.create_rules1(rules)
            self.create_rules8(rules)
            self.create_rules16(rules)
        else:
            self.create_rules1(rules)
            self.create_rules8(rules)
            self.create_rules16(rules)
            self.create_rules32(rules)
        if self.obj is None:
            GV.DB_MODULECONFIG.insert_one(
                {"name": name, "system": system, "bit": bit, "normal": normal, "rules": rules})
        else:
            GV.DB_MODULECONFIG.update_one({'id': self.obj['_id']},
                                          {'$set': {"name": name, "normal": normal, "rules": rules}})
            self.obj = None
        self.disabled = True
        self.bit = 0
        self.opacity = 0
        msg_color = 'success'
        msg_text = 'Add module ' + name + ' success'
        self.mccm_module.mccm.mm_notification.notification_msg(msg_color, msg_text)

        self.mscmmm_cancel.init_mscmmm()

    def create_rules1(self, rules):     # ----- RULES for 1 BIT ------------------------------------------------------ #
        function1 = self.mscmmm_bit_container1.function0.text
        sx1 = "&" + self.return_color(self.mscmmm_bit_container1.sx_color0.text) \
              + self.return_flash(self.mscmmm_bit_container1.sx_flash0.text) \
              + self.return_power(self.mscmmm_bit_container1.sx_power0.text)
        dx1 = "&" + self.return_color(self.mscmmm_bit_container1.dx_color0.text) \
              + self.return_flash(self.mscmmm_bit_container1.dx_flash0.text) \
              + self.return_power(self.mscmmm_bit_container1.dx_power0.text)
        rules.append({"bit": 0, "function": function1, "SX": sx1, "DX": dx1})
        return rules

    def create_rules8(self, rules):     # ----- RULES for 8 BIT ------------------------------------------------------ #
        function8 = self.mscmmm_bit_container8.function1.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color1.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash1.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power1.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color1.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash1.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power1.text)
        rules.append({"bit": 1, "function": function8, "SX": sx8, "DX": dx8})
        function8 = self.mscmmm_bit_container8.function2.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color2.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash2.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power2.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color2.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash2.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power2.text)
        rules.append({"bit": 2, "function": function8, "SX": sx8, "DX": dx8})
        function8 = self.mscmmm_bit_container8.function3.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color3.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash3.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power3.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color3.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash3.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power3.text)
        rules.append({"bit": 3, "function": function8, "SX": sx8, "DX": dx8})
        function8 = self.mscmmm_bit_container8.function4.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color4.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash4.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power4.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color4.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash4.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power4.text)
        rules.append({"bit": 4, "function": function8, "SX": sx8, "DX": dx8})
        function8 = self.mscmmm_bit_container8.function5.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color5.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash5.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power5.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color5.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash5.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power5.text)
        rules.append({"bit": 5, "function": function8, "SX": sx8, "DX": dx8})
        function8 = self.mscmmm_bit_container8.function6.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color6.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash6.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power6.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color6.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash6.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power6.text)
        rules.append({"bit": 6, "function": function8, "SX": sx8, "DX": dx8})
        function8 = self.mscmmm_bit_container8.function7.text
        sx8 = "&" + self.return_color(self.mscmmm_bit_container8.sx_color7.text) \
              + self.return_flash(self.mscmmm_bit_container8.sx_flash7.text) \
              + self.return_power(self.mscmmm_bit_container8.sx_power7.text)
        dx8 = "&" + self.return_color(self.mscmmm_bit_container8.dx_color7.text) \
              + self.return_flash(self.mscmmm_bit_container8.dx_flash7.text) \
              + self.return_power(self.mscmmm_bit_container8.dx_power7.text)
        rules.append({"bit": 7, "function": function8, "SX": sx8, "DX": dx8})
        return rules

    def create_rules16(self, rules):    # ----- RULES for 16 BIT ----------------------------------------------------- #
        function16 = self.mscmmm_bit_container16.function8.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color8.text) \
              + self.return_flash(self.mscmmm_bit_container16.sx_flash8.text) \
              + self.return_power(self.mscmmm_bit_container16.sx_power8.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color8.text) \
              + self.return_flash(self.mscmmm_bit_container16.dx_flash8.text) \
              + self.return_power(self.mscmmm_bit_container16.dx_power8.text)
        rules.append({"bit": 8, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function9.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color9.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash9.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power9.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color9.text) \
               + self.return_flash(self.mscmmm_bit_container16.dx_flash9.text) \
               + self.return_power(self.mscmmm_bit_container16.dx_power9.text)
        rules.append({"bit": 9, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function10.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color10.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash10.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power10.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color10.text) \
               + self.return_flash(self.mscmmm_bit_container16.dx_flash10.text) \
               + self.return_power(self.mscmmm_bit_container16.dx_power10.text)
        rules.append({"bit": 10, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function11.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color11.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash11.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power11.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color11.text) \
               + self.return_flash(self.mscmmm_bit_container16.dx_flash11.text) \
               + self.return_power(self.mscmmm_bit_container16.dx_power11.text)
        rules.append({"bit": 11, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function12.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color12.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash12.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power12.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color12.text) \
               + self.return_flash(self.mscmmm_bit_container16.dx_flash12.text) \
               + self.return_power(self.mscmmm_bit_container16.dx_power12.text)
        rules.append({"bit": 12, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function13.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color13.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash13.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power13.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color13.text) \
               + self.return_flash(self.mscmmm_bit_container16.dx_flash13.text) \
               + self.return_power(self.mscmmm_bit_container16.dx_power13.text)
        rules.append({"bit": 13, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function14.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color14.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash14.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power14.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.dx_color14.text) \
               + self.return_flash(self.mscmmm_bit_container16.dx_flash14.text) \
               + self.return_power(self.mscmmm_bit_container16.dx_power14.text)
        rules.append({"bit": 14, "function": function16, "SX": sx16, "DX": dx16})
        function16 = self.mscmmm_bit_container16.function15.text
        sx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color15.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash15.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power15.text)
        dx16 = "&" + self.return_color(self.mscmmm_bit_container16.sx_color15.text) \
               + self.return_flash(self.mscmmm_bit_container16.sx_flash15.text) \
               + self.return_power(self.mscmmm_bit_container16.sx_power15.text)
        rules.append({"bit": 15, "function": function16, "SX": sx16, "DX": dx16})
        return rules

    def create_rules32(self, rules):    # ----- RULES for 32 BIT ----------------------------------------------------- #
        function32 = self.mscmmm_bit_container32.function16.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color16.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash16.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power16.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color16.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash16.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power16.text)
        rules.append({"bit": 16, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function17.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color17.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash17.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power17.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color17.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash17.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power17.text)
        rules.append({"bit": 17, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function18.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color18.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash18.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power18.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color18.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash18.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power18.text)
        rules.append({"bit": 18, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function19.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color19.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash19.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power19.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color19.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash19.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power19.text)
        rules.append({"bit": 19, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function20.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color20.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash20.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power20.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color20.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash20.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power20.text)
        rules.append({"bit": 20, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function21.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color21.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash21.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power21.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color21.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash21.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power21.text)
        rules.append({"bit": 21, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function22.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color22.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash22.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power22.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color22.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash22.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power22.text)
        rules.append({"bit": 22, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function23.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color23.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash23.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power23.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color23.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash23.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power23.text)
        rules.append({"bit": 23, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function24.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color24.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash24.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power24.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color24.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash24.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power24.text)
        rules.append({"bit": 24, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function25.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color25.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash25.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power25.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color25.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash25.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power25.text)
        rules.append({"bit": 25, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function26.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color26.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash26.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power26.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color26.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash26.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power26.text)
        rules.append({"bit": 26, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function27.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color27.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash27.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power27.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color27.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash27.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power27.text)
        rules.append({"bit": 27, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function28.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color28.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash28.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power28.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color28.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash28.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power28.text)
        rules.append({"bit": 28, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function29.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color29.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash29.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power29.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color29.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash29.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power29.text)
        rules.append({"bit": 29, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function30.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color30.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash30.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power30.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color30.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash30.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power30.text)
        rules.append({"bit": 30, "function": function32, "SX": sx32, "DX": dx32})
        function32 = self.mscmmm_bit_container32.function31.text
        sx32 = "&" + self.return_color(self.mscmmm_bit_container32.sx_color31.text) \
               + self.return_flash(self.mscmmm_bit_container32.sx_flash31.text) \
               + self.return_power(self.mscmmm_bit_container32.sx_power31.text)
        dx32 = "&" + self.return_color(self.mscmmm_bit_container32.dx_color31.text) \
               + self.return_flash(self.mscmmm_bit_container32.dx_flash31.text) \
               + self.return_power(self.mscmmm_bit_container32.dx_power31.text)
        rules.append({"bit": 31, "function": function32, "SX": sx32, "DX": dx32})
        return rules

    def return_color(self, value):
        if value == '':
            return '000000'
        else:
            return value

    def return_flash(self, value):
        if value == '...':
            return '0'
        else:
            for item in GV.HL_FLASH:
                if item['type'] == value:
                    return item['value']

    def return_power(self, value):
        if value == '...':
            return 'F'
        else:
            for item in GV.HL_POWER:
                if item['type'] == value:
                    return item['value']


# ---- Cancel button inside Module Bit Container --------------------------------------------------------------------- #
class ModuleEditCancelBtn(Button):
    obj = ObjectProperty(None, allownone=True)

    def delete_data(self):
        self.mscmmm_save.bit = 0
        self.mscmmm_save.disabled = True
        self.mscmmm_save.opacity = 0
        self.init_mscmmm()

    def init_mscmmm(self):
        self.mscmmm_name.text = ''
        self.mscmmm_name.disabled = False
        self.mscmmm_system.disabled = True
        self.mscmmm_system.text = 'System...'
        self.mscmmm_bit.disabled = True
        self.mscmmm_bit.text = 'Bit...'
        self.mscmmm_bit_container1.pos = 5, -5000
        self.mscmmm_bit_container8.pos = 5, -5000
        self.mscmmm_bit_container16.pos = 5, -5000
        self.mscmmm_bit_container32.pos = 5, -5000
        self.mscmmm_bit_container1.reset_bit()
        self.mscmmm_bit_container8.reset_bit()
        self.mscmmm_bit_container16.reset_bit()
        self.mscmmm_bit_container32.reset_bit()
        self.mscmm_module.disabled = True
        self.mscmm_module.opacity = 0
        self.msc_module_container.disabled = False
        self.disabled = True
        self.msc_module_container.update_library()
