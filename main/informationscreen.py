
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty

import json
import os
import tarfile
import shutil


from datetime import datetime


# -- Import Personal Utility ------------------------------------------------------------------------------------------#
import utility.gvar as GV
from classi.usbFind import UsbFind


# ----------------------------- Main Class Screen -------------------------------------------------------------------- #
class ProjectScreen(Screen):
    mccm = ObjectProperty(None)


class ProjectContainer(RelativeLayout):
    information_project = StringProperty()
    information_version = StringProperty()
    information_date = StringProperty()
    information_eng = StringProperty()

    def __init__(self, **kwargs):
        super(ProjectContainer, self).__init__(**kwargs)
        self.build()
        self.file = []
        self.usb_detect = UsbFind()

    def build(self):
        with open(GV.DIR_JSON + 'information.json') as json_file:
            data = json.load(json_file)
            self.information_project = "Project Number:" + data['Info']['project']
            self.information_version = 'Version: ' + data['Info']['version']
            self.information_date = 'Date: ' + data['Info']['date']
            self.information_eng = 'Eng.: ' + data['Info']['eng']

    def create_report(self):
        self.remove_widget(self.usb_detect)
        self.add_widget(self.usb_detect)
        self.create_backup()

    def create_backup(self):

        db_list = 'rs0/'
        for server in GV.DB_SERVER:
            db_list += server['server'] + ':' + server['port'] + ','
        mongo_dump = "mongodump" + " --host " + db_list[:-1] + " --db " + GV.DB_NAME + " --out " + GV.DIR_BACKUP + "/db"
        os.system(mongo_dump)

        self.file = datetime.now().strftime("%Y%m%d_%H%M") + '_Report.tar.bz2'
        report = tarfile.open(GV.DIR_BACKUP + self.file, 'w:bz2')
        report.add(GV.DIR_DB + 'log/db.log')
        report.add(GV.DIR_DB + 'log/db0.log')
        report.add(GV.DIR_JSON)
        report.add(GV.DIR_BACKUP + "/db")
        report.close()
        shutil.rmtree(GV.DIR_BACKUP + "/db", ignore_errors=True)

        notification = self.parent.mccm.mm_notification
        logger = self.parent.mccm.mm_logger
        self.usb_detect.find_usb(self.file, notification, logger)

