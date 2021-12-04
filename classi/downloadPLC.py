from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
import time
from pymongo import MongoClient, errors
from threading import Thread

# -- Import Personal Utility ------------------------------------------------------------------------------------------#
import utility.gvar as GV


class LabelMSG(Label):
    pass


class DownloadPLC(BoxLayout):
    obj = ObjectProperty()

    def __init__(self, **kwargs):
        super(DownloadPLC, self).__init__(**kwargs)
        self.connect_data = []

    def start_download(self):
        self.message_step('Start download')
        self.init_data()

    def init_data(self):
        pipeline = [
            {
                '$lookup':
                    {
                        'from': "inputList",
                        'localField': "inputID",
                        'foreignField': "_id",
                        'as': "input_data"
                    }
            },
            {
                '$unwind': "$input_data"
            },
            {
                '$lookup':
                    {
                        'from': "moduleConfig",
                        'localField': "moduleID",
                        'foreignField': "_id",
                        'as': "module_data"
                    }
            },
            {
                '$unwind': "$module_data"
            }
        ]
        cursor = GV.DB_CONNECTIONLIST.aggregate(pipeline)
        for item in list(cursor):
            output_list = []
            for output in item['outputList']:
                output_list.append(output['name'])

            data = {
                '_id': item['_id'],
                'register': item['input_data']['register'],
                'input_name': item['module_data']['name'],
                'module_name': item['module_data']['name'],
                'output_name': output_list
            }

            self.connect_data.append(data)
        self.message_step('Load data complete')
        self.create_file()

    def create_file(self):
        for item in self.connect_data:
            print(item)
        self.message_step('Create files complete')
        self.send_file()

    def send_file(self):
        self.message_step('------------')
        self.message_step(' download file')

        self.finish_download()

    def finish_download(self):
        self.parent.remove_widget(self)


    def message_step(self, msg):
        line = LabelMSG(text=msg)
        self.msg_list.add_widget(line)


