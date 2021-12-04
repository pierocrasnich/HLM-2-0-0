# To use:
#
#   from classi.usbFind import UsbFind
#
#   usb_detect = UsbFind()
#   usb_detect.find_usb(self.file, notification, logger)
#
# In "notification" pass NotificationMSG Object
# In "logger" pass LoggerStatus Object

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ListProperty

import os
from sys import platform as _platform, exit, exc_info


import utility.gvar as GV
Builder.load_file('classi/usbFind.kv')


class UsbFind(BoxLayout):
    color_bk = ListProperty()

    def __init__(self, **kwargs):
        super(UsbFind, self).__init__(**kwargs)
        self.devices_list = []
        self.find_count = 0
        self.file = []
        self.cmd_unmount_usb = ''
        self.timeout_detect_usb = 10
        self.notification = []
        self.logger = []
        self.os_desktop = ''

        if _platform == "linux" or _platform == "linux2":
            device = os.popen('lsusb')
            self.cmd_unmount_usb = 'unmount '
            self.os_desktop = '/home/hlm/Desktop/'
            for item in device:
                self.devices_list.append(item)
        elif _platform == "darwin":
            device = os.popen('ls -a /Volumes')
            self.cmd_unmount_usb = 'diskutil unmount '
            self.os_desktop = '~/Desktop'
            for item in device:
                self.devices_list.append(item)

    def find_usb(self, file, notification, logger):
        self.notification = notification
        self.logger = logger
        self.color_bk = GV.RGBA_SUCCESS
        self.file = file
        self.find_count = 0
        Clock.schedule_interval(self.check_usb, 1)

    def check_usb(self, dt):
        if GV.EXPORT_DEVICE == 'USB':
            self.usb_msg_label.text = 'Connect USB in ' + str(self.timeout_detect_usb - self.find_count)
        elif GV.EXPORT_DEVICE == 'DESKTOP':
            cmd_text = 'mv ' + GV.DIR_BACKUP + str(self.file) + ' ' + self.os_desktop
            try:
                os.system(cmd_text)
            finally:
                msg_color = 'success'
                msg_text = 'Save file on Desktop'
                self.notification.notification_msg(msg_color, msg_text)
                Clock.unschedule(self.check_usb)
                self.parent.remove_widget(self)
                return

        if _platform == "linux" or _platform == "linux2":
            device = os.popen('lsusb')
            for item in device:
                if item not in self.devices_list:
                    device_detect = item
                    os.system('mount ' + item)
                    self.save_file(device_detect)
                    Clock.unschedule(self.check_usb)
        elif _platform == "darwin":
            device = os.popen('ls -a /Volumes')
            for item in device:
                if item not in self.devices_list:
                    device_detect = "/Volumes/" + item
                    self.save_file(device_detect)
                    Clock.unschedule(self.check_usb)

        if self.find_count == self.timeout_detect_usb:
            msg_color = 'error'
            msg_text = '!!! USB not detect !!!'
            self.notification.notification_msg(msg_color, msg_text)
            self.close_widget()
            Clock.unschedule(self.check_usb)

        self.find_count += 1

    def save_file(self, device):
        cmd_text = 'cp ' + GV.DIR_BACKUP + str(self.file) + ' ' + device + str(self.file)
        try:
            os.system(cmd_text)
            msg_color = 'success'
            msg_text = "export FILE " + self.file
            self.notification.notification_msg(msg_color, msg_text)
            msg_log_text = 'export FILE ' + str(self.file)
            self.logger.logger_add(msg_color, msg_log_text)
        except IOError as e:
            msg_color = 'error'
            msg_text = "Unable to copy file. %s" % e
            self.notification.notification_msg(msg_color, msg_text)
            exit(1)
        finally:
            os.system(self.cmd_unmount_usb + device)
            self.close_widget()

    def close_widget(self):
        # Remove file from BACKUP folder
        os.system('rm ' + GV.DIR_BACKUP + str(self.file))
        self.parent.remove_widget(self)
