from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from bson import ObjectId
import utility.gvar as gv
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder

import utility.gvar as GV



from pymongo import ASCENDING
from datetime import datetime
from classi.csv import PDF
from classi.usbFind import UsbFind

Builder.load_file('main/classi/list.kv')


# ----- Classe principale del layout SCREEN CONNECT LIST ------------------------------------------------------------- #
class ConnectListScreen(Screen):
    mccm = ObjectProperty(None)

    # def on_pre_enter(self, *args):
    #     self.cl_container.get_list()

    def on_enter(self, *args):
        self.cl_container.get_list()

    def on_pre_leave(self, *args):
        pass


class ConnectListContainer(RelativeLayout):

    def get_list(self):
        self.clc_list.refresh_list()


# ----- Classe per la generazione della lista delle connessioni presenti nel DB -------------------------------------- #


class ConnectionList(GridLayout):

    def __init__(self, **kwargs):
        super(ConnectionList, self).__init__(**kwargs)
        self.connect_list = []
        self.pdf = []
        self.usb_detect = UsbFind()

    def get_list(self):
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
                'system': item['input_data']['system'],
                'register': item['input_data']['register'],
                'input_name': item['input_data']['name'],
                'module_name': item['module_data']['name'],
                'output_name': output_list
                    }

            self.connect_list.append(data)
        self.show_list()

    def show_list(self):
        index_row = 0
        for item in self.connect_list:
            layout = ConnectListBoxRow()
            layout.id = item['_id']
            if (index_row % 2) == 0:
                layout.set_color = 1, 1, 1, .1
            else:
                layout.set_color = 1, 1, 1, .05
            output_name = str(item['output_name'])[1:-1].replace("'", "")
            layout.add_widget(LabelConnect(text=str(item['system']), width=200))
            layout.add_widget(LabelConnect(text=str(item['register']), width=250))
            layout.add_widget(LabelConnect(text=str(item['input_name']), width=250))
            layout.add_widget(LabelConnect(text=str(item['module_name']), width=250))
            layout.add_widget(LabelConnect(text=output_name, width=480, halign='left'))
            layout.add_widget(DelConnectButton())

            self.add_widget(layout)
            index_row += 1

    def refresh_list(self):
        self.clear_widgets()
        self.connect_list = []
        self.get_list()

    def export_pdf_connections(self):
        # self.parent.parent.add_widget(self.usb_detect)
        output_file_name = datetime.now().strftime("%Y%m%d_%H%M") + '_ConnectionsList.pdf'
        self.pdf = PDF('P', 'mm', 'A4')
        self.pdf.set_title('Connections List')

        self.pdf.table_header = ['#', 'system', 'inputID', 'moduleID', 'outputList']
        self.pdf.table_size = [10, 30, 60, 30, 60]  # tot 190 mm
        self.pdf.add_page()

        self.pdf.set_font("Arial", size=9)
        line_no = 1
        for item in list(self.connect_list):
            # Line is Odd or Even
            if (line_no % 2) == 0:
                self.pdf.set_fill_color(230, 230, 230)
            else:
                self.pdf.set_fill_color(255, 255, 255)

            self.pdf.cell(self.pdf.table_size[0], 5, format(line_no), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[1], 5, format('system'), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[2], 5, format(item['input_name']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[3], 5, format(item['module_name']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[4], 5, format(item['output_name'][0]), fill=True, ln=1, align='C')
            for output in item['output_name'][1:]:
                self.pdf.cell(self.pdf.table_size[0], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[1], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[2], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[3], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[4], 5, format(output), fill=True, ln=1, align='C')

            line_no += 1

        self.pdf.alias_nb_pages()
        self.pdf.output(GV.DIR_BACKUP + output_file_name)


# ----- Classe per la generazione delle righe contenenti le connessioni presenti nel DB ------------------------------ #


class ConnectListBoxRow(GridLayout):
    set_color = ListProperty([255/255, 0/255, 0/255, 1])


# ----- Classe Label contenenti le informazioni delle connessioni ---------------------------------------------------- #


class LabelConnect(Label):
    pass


# ----- Classe Pulsante per la cancellazione della riga nel database ------------------------------------------------- #


class DelConnectButton(AnchorLayout, Button):

    def on_press(self):
        collection = gv.DB_CONNECTIONLIST
        collection.delete_one({'_id': ObjectId(self.parent.id)})
        self.parent.parent.refresh_list()

