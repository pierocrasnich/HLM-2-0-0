
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore

import os
import csv
from bson import ObjectId
from fpdf import FPDF
from fpdf.html import hex2dec
from sys import platform as _platform, exc_info
from datetime import datetime

import utility.gvar as GV
from classi.usbFind import UsbFind

Builder.load_file('./classi/csv.kv')


# ########################################### PDF HEADER FOOTER ###################################################### #

class PDF(FPDF):

    def header(self):
        self.image(GV.DIR_IMAGES + 'pdf/HeaderPDF.jpg', w=0, h=19, type='JPG', link='')
        self.set_font('Arial', 'B', 18)
        self.cell(40, 15, self.title + ' configuration', 0, 0, 'L')
        self.set_font('Arial', '', 8)
        file_info = JsonStore(GV.DIR_JSON + GV.FILE_INFO)
        project = 'project: ' + file_info['Info']['project']
        self.cell(0, 5, project, 0, 1, 'R')
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cell(0, 5, date, 0, 1, 'R')
        self.set_line_width(0.5)
        self.set_draw_color(140, 0, 0)
        self.line(10, 42, 200, 42)
        self.ln(5)
        for count, head_tab in enumerate(self.table_header):
            self.set_font('Arial', 'B', 12)
            self.set_fill_color(200, 200, 200)
            self.cell(self.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-20)
        self.set_line_width(0.5)
        self.set_draw_color(140, 0, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.set_font('Arial', 'I', 8)
        img = GV.DIR_IMAGES + 'pdf/FooterPDF.jpg'
        self.image(img, x=self.get_x(), y=self.get_y() + 1, w=0,  h=15, type='JPG', link='')
        self.cell(0, 5, 'Page %s' % self.page_no() + '/{nb}', 0,0, 'R')


# ########################################### EXPORT BUTTON ########################################################## #
class ExportPdfButton(Button):
    module_select = StringProperty()

    def __init__(self, **kwargs):
        super(ExportPdfButton, self).__init__(**kwargs)
        self.usb_detect = UsbFind()
        self.pdf = []
        self.pdf_file_name = ''

    @staticmethod
    def color_set(color_set):
        if color_set == '000000':
            set_color = '#FFFFFF'
        else:
            set_color = '#' + color_set
        return set_color

    @staticmethod
    def return_flash(flash_set):
        for item in GV.HL_FLASH:
            if item['value'] == flash_set:
                return item['type']

    def export_pdf_module(self):
        self.mccm_connect.add_widget(self.usb_detect)

        self.pdf_file_name = datetime.now().strftime("%Y%m%d_%H%M") + '_' + self.module_select + '_module.pdf'
        self.pdf = PDF('P', 'mm', 'A4')
        self.pdf.set_title(self.module_select + '  module ')
        self.pdf.table_header = []
        self.pdf.table_size = []
        self.pdf.add_page()

        result = GV.DB_MODULECONFIG.find({'name': self.module_select}, {'_id': False})
        self.pdf.table_header = ['#', 'system', 'name', 'bit', 'function', 'SX', 'flash', 'pwr', 'DX', 'flash', 'pwr']
        self.pdf.table_size = [10, 25, 25, 13, 39, 13, 13, 13, 13,  13, 13]  # tot 190 mm

        for count, head_tab in enumerate(self.pdf.table_header):
            self.pdf.set_font('Arial', 'B', 12)
            self.pdf.set_fill_color(200, 200, 200)
            self.pdf.cell(self.pdf.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.pdf.ln(5)
        self.pdf.set_font("Arial", size=9)
        self.pdf.set_fill_color(255, 255, 255)

        for item in list(result):
            self.pdf.cell(self.pdf.table_size[0], 5, '1', fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[1], 5, format(item['system']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[2], 5, format(item['name']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[3], 5, format(item['bit']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[4], 5, 'normal', fill=True, ln=0, align='C')
            set_color = self.color_set(item['normal']['SX'][1:][:-2])
            self.pdf.set_fill_color(*hex2dec(set_color))
            self.pdf.cell(self.pdf.table_size[5], 5, format(item['normal']['SX'][1:][:-2]), fill=True, ln=0, align='C')
            self.pdf.set_fill_color(255, 255, 255)
            flash_value = self.return_flash(str(item['normal']['SX'][7:][:-1]))
            self.pdf.cell(self.pdf.table_size[6], 5, format(flash_value), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[7], 5, format(item['normal']['SX'][8:]), fill=True, ln=0, align='C')
            set_color = self.color_set(item['normal']['DX'][1:][:-2])
            self.pdf.set_fill_color(*hex2dec(set_color))
            self.pdf.cell(self.pdf.table_size[8], 5, format(item['normal']['DX'][1:][:-2]), fill=True, ln=0, align='C')
            self.pdf.set_fill_color(255, 255, 255)
            flash_value = self.return_flash(str(item['normal']['DX'][7:][:-1]))
            self.pdf.cell(self.pdf.table_size[9], 5, format(flash_value), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[10], 5, format(item['normal']['DX'][8:]), fill=True, ln=1, align='C')

            for rules in item['rules']:
                if rules['function'] != '':
                    func = rules['function'] + ' (bit ' + str(rules['bit']) + ')'
                    self.pdf.cell(self.pdf.table_size[0], 5, ' ', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[1], 5, ' ', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[2], 5, ' ', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[3], 5, '', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[4], 5, func, fill=True, ln=0, align='C')
                    set_color = self.color_set(rules['SX'][1:][:-2])
                    self.pdf.set_fill_color(*hex2dec(set_color))
                    self.pdf.cell(self.pdf.table_size[5], 5, format(rules['SX'][1:][:-2]), fill=True, ln=0, align='C')
                    self.pdf.set_fill_color(255, 255, 255)
                    flash_value = self.return_flash(str(rules['SX'][7:][:-1]))
                    self.pdf.cell(self.pdf.table_size[6], 5, format(flash_value), fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[7], 5, format(rules['SX'][8:]), fill=True, ln=0, align='C')
                    set_color = self.color_set(rules['DX'][1:][:-2])
                    self.pdf.set_fill_color(*hex2dec(set_color))
                    self.pdf.cell(self.pdf.table_size[6], 5, format(rules['DX'][1:][:-2]), fill=True, ln=0, align='C')
                    self.pdf.set_fill_color(255, 255, 255)
                    flash_value = self.return_flash(str(rules['DX'][7:][:-1]))
                    self.pdf.cell(self.pdf.table_size[9], 5, format(flash_value), fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[10], 5, format(rules['DX'][8:]), fill=True, ln=1, align='C')

        self.pdf.alias_nb_pages()
        self.pdf.output(GV.DIR_BACKUP + self.pdf_file_name)

        notification = self.mccm_connect.mccm.mm_notification
        logger = self.mccm_connect.mccm.mm_logger
        self.usb_detect.find_usb(self.pdf_file_name, notification, logger)


class ExportObjectButton(Button):
    exportList = StringProperty()

    def __init__(self, **kwargs):
        super(ExportObjectButton, self).__init__(**kwargs)
        self.usb_detect = UsbFind()
        self.output_file_name = 'ObjectList'

    def export_csv(self):
        self.parent.add_widget(self.usb_detect)
        result = GV.DB_OBJECTLIST.find({})
        self.output_file_name = datetime.now().strftime("%Y%m%d_%H%M") + '_' + self.exportList + 'List.csv'
        with open(GV.DIR_BACKUP + self.output_file_name, 'w') as export_file:
            # Object List export CSV ####################
            if self.exportList == 'object':
                fields = ['system', 'address', 'name', 'deck', 'posX', 'posY', 'rotate']
                file = csv.DictWriter(export_file, fieldnames=fields)
                file.writeheader()
                for answers_module in result:
                    file.writerow({'system': answers_module['system'],
                                   'address': answers_module['address'],
                                   'name': answers_module['name'],
                                   'deck': answers_module['deck'],
                                   'posX': answers_module['posX'],
                                   'posY': answers_module['posY'],
                                   'rotate': answers_module['rotate']
                                   })
        self.save_file()

    def save_file(self):
        notification = self.parent.parent.mccm.mm_notification
        logger = self.parent.parent.mccm.mm_logger
        self.usb_detect.find_usb(self.output_file_name, notification, logger)


class ExportConnectButton(Button):
    exportList = StringProperty()

    def __init__(self, **kwargs):
        super(ExportConnectButton, self).__init__(**kwargs)
        self.usb_detect = UsbFind()
        self.pdf = []
        self.output_file_name = ''

    @staticmethod
    def color_set(color_set):
        if color_set == '000000':
            set_color = '#FFFFFF'
        else:
            set_color = '#' + color_set
        return set_color

    @staticmethod
    def return_flash(flash_set):
        for item in GV.HL_FLASH:
            if item['value'] == flash_set:
                return item['type']

    def export_csv(self):
        self.parent.add_widget(self.usb_detect)

        if self.exportList == 'input':
            result = GV.DB_INPUTLIST.find({})
        elif self.exportList == 'output':
            result = GV.DB_OUTPUTLIST.find({})
        elif self.exportList == 'object':
            result = GV.DB_OBJECTLIST.find({})

        self.output_file_name = datetime.now().strftime("%Y%m%d_%H%M") + '_' + self.exportList + 'List.csv'
        with open(GV.DIR_BACKUP + self.output_file_name, 'w') as export_file:
            # Input List export CSV ####################
            if self.exportList == 'input':
                fields = ['register', 'bit', 'system', 'name', 'description']
                file = csv.DictWriter(export_file, fieldnames=fields)
                file.writeheader()
                for answers_module in result:
                    file.writerow({'register': answers_module['register'],
                                   'bit': answers_module['bit'],
                                   'system': answers_module['system'],
                                   'name': answers_module['name'],
                                   'description': answers_module['description']
                                   })
            # Output List export CSV ####################
            elif self.exportList == 'output':
                fields = ['system', 'address', 'plc', 'port',  'name', 'description']
                file = csv.DictWriter(export_file, fieldnames=fields)
                file.writeheader()
                for answers_module in result:
                    file.writerow({'system': answers_module['system'],
                                   'address': answers_module['address'],
                                   'plc': answers_module['plc'],
                                   'port': answers_module['port'],
                                   'name': answers_module['name'],
                                   'description': answers_module['description']
                                   })
            # Object List export CSV ####################
            elif self.exportList == 'object':
                fields = ['system', 'address', 'plc', 'port', 'name', 'description']
                file = csv.DictWriter(export_file, fieldnames=fields)
                file.writeheader()
                for answers_module in result:
                    file.writerow({'system': answers_module['system'],
                                   'name': answers_module['name'],
                                   'address': answers_module['address'],
                                   'deck': answers_module['deck'],
                                   'posX': answers_module['posX'],
                                   'posY': answers_module['posY'],
                                   'rotate': answers_module['rotate']
                                   })
        self.save_file()

    def export_pdf(self):

        self.parent.add_widget(self.usb_detect)
        self.output_file_name = datetime.now().strftime("%Y%m%d_%H%M") + '_' + self.exportList + 'List.pdf'
        self.pdf = PDF('P', 'mm', 'A4')
        self.pdf.set_title(self.exportList)

        self.pdf.table_header = []
        self.pdf.table_size = []
        self.pdf.add_page()

        if self.exportList == 'input':
            result = GV.DB_INPUTLIST.find({}, {'_id': False})
            self.pdf.table_header = ['#', 'system', 'name', 'register', 'bit', 'description']
            self.pdf.table_size = [10, 25, 20, 25, 10, 100]  # tot 190 mm
            self.pdf_input_output(result)
        elif self.exportList == 'output':
            result = GV.DB_OUTPUTLIST.find({}, {'_id': False})
            self.pdf.table_header = ['#', 'system', 'name', 'address', 'plc', 'port', 'description']
            self.pdf.table_size = [10, 25, 20, 25, 20, 15, 75]  # tot 190 mm
            self.pdf_input_output(result)
        elif self.exportList == 'modules':
            result = GV.DB_MODULECONFIG.find({}, {'_id': False})
            self.pdf.table_header = ['#', 'system', 'name', 'bit', 'function', 'SX', 'flash', 'pwr', 'DX', 'flash',
                                     'pwr']
            self.pdf.table_size = [10, 25, 25, 13, 39, 13, 13, 13, 13, 13, 13]  # tot 190 mm
            self.pdf_modules(result)
        elif self.exportList == 'connections':
            result = GV.DB_CONNECTIONLIST.find({}, {'_id': False})
            self.pdf.table_header = ['#',  'system', 'inputID', 'moduleID', 'outputList']
            self.pdf.table_size = [10, 30, 30, 30, 90]  # tot 190 mm
            self.pdf_connections(result)

        self.pdf.alias_nb_pages()
        self.pdf.output(GV.DIR_BACKUP + self.output_file_name)

    def pdf_input_output(self, result):
        for count, head_tab in enumerate(self.pdf.table_header):
            self.pdf.set_font('Arial', 'B', 12)
            self.pdf.set_fill_color(200, 200, 200)
            self.pdf.cell(self.pdf.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.pdf.ln(5)
        self.pdf.set_font("Arial", size=9)
        line_no = 1
        for item in list(result):
            # Line is Odd or Even
            if (line_no % 2) == 0:
                self.pdf.set_fill_color(230, 230, 230)
            else:
                self.pdf.set_fill_color(255, 255, 255)
            self.pdf.cell(self.pdf.table_size[0], 5, format(line_no), fill=True, ln=0, align='C')
            for count, value in enumerate(item):
                self.pdf.cell(self.pdf.table_size[count + 1], 5, format(item[self.pdf.table_header[count + 1]]), fill=True, ln=0, align='C')
            self.pdf.ln(5)
            line_no += 1
        self.save_file()

    def pdf_modules(self,  result):
        for count, head_tab in enumerate(self.pdf.table_header):
            self.pdf.set_font('Arial', 'B', 12)
            self.pdf.set_fill_color(200, 200, 200)
            self.pdf.cell(self.pdf.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.pdf.ln(5)
        self.pdf.set_font("Arial", size=9)
        line_no = 1
        for item in list(result):
            # Line is Odd or Even
            if (line_no % 2) == 0:
                set_color_base = '#E6E6E6'
            else:
                set_color_base = '#FFFFFF'

            self.pdf.set_fill_color(*hex2dec(set_color_base))
            self.pdf.cell(self.pdf.table_size[0], 5, format(line_no), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[1], 5, format(item['system']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[2], 5, format(item['name']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[3], 5, format(item['bit']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[4], 5, 'normal', fill=True, ln=0, align='C')
            set_color = self.color_set(item['normal']['SX'][1:][:-2])
            self.pdf.set_fill_color(*hex2dec(set_color))
            self.pdf.cell(self.pdf.table_size[5], 5, format(item['normal']['SX'][1:][:-2]), fill=True, ln=0, align='C')
            self.pdf.set_fill_color(*hex2dec(set_color_base))
            flash_value = self.return_flash(str(item['normal']['SX'][7:][:-1]))
            self.pdf.cell(self.pdf.table_size[6], 5, format(flash_value), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[7], 5, format(item['normal']['SX'][8:]), fill=True, ln=0, align='C')
            set_color = self.color_set(item['normal']['DX'][1:][:-2])
            self.pdf.set_fill_color(*hex2dec(set_color))
            self.pdf.cell(self.pdf.table_size[8], 5, format(item['normal']['DX'][1:][:-2]), fill=True, ln=0, align='C')
            self.pdf.set_fill_color(*hex2dec(set_color_base))
            flash_value = self.return_flash(str(item['normal']['DX'][7:][:-1]))
            self.pdf.cell(self.pdf.table_size[9], 5, format(flash_value), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[10], 5, format(item['normal']['DX'][8:]), fill=True, ln=1, align='C')

            for rules in item['rules']:
                if rules['function'] != '':
                    func = rules['function'] + ' (bit ' + str(rules['bit']) + ')'
                    self.pdf.cell(self.pdf.table_size[0], 5, ' ', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[1], 5, ' ', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[2], 5, ' ', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[3], 5, '', fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[4], 5, func, fill=True, ln=0, align='C')
                    set_color = self.color_set(rules['SX'][1:][:-2])
                    self.pdf.set_fill_color(*hex2dec(set_color))
                    self.pdf.cell(self.pdf.table_size[5], 5, format(rules['SX'][1:][:-2]), fill=True, ln=0, align='C')
                    self.pdf.set_fill_color(*hex2dec(set_color_base))
                    flash_value = self.return_flash(str(rules['SX'][7:][:-1]))
                    self.pdf.cell(self.pdf.table_size[6], 5, format(flash_value), fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[7], 5, format(rules['SX'][8:]), fill=True, ln=0, align='C')
                    set_color = self.color_set(rules['DX'][1:][:-2])
                    self.pdf.set_fill_color(*hex2dec(set_color))
                    self.pdf.cell(self.pdf.table_size[6], 5, format(rules['DX'][1:][:-2]), fill=True, ln=0, align='C')
                    self.pdf.set_fill_color(*hex2dec(set_color_base))
                    flash_value = self.return_flash(str(rules['DX'][7:][:-1]))
                    self.pdf.cell(self.pdf.table_size[9], 5, format(flash_value), fill=True, ln=0, align='C')
                    self.pdf.cell(self.pdf.table_size[10], 5, format(rules['DX'][8:]), fill=True, ln=1, align='C')
            line_no += 1
        self.save_file()

    def pdf_connections(self, result):
        for count, head_tab in enumerate(self.pdf.table_header):
            self.pdf.set_font('Arial', 'B', 12)
            self.pdf.set_fill_color(200, 200, 200)
            self.pdf.cell(self.pdf.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.pdf.ln(5)
        self.pdf.set_font("Arial", size=9)
        line_no = 1
        for item in list(result):
            # Line is Odd or Even
            if (line_no % 2) == 0:
                self.pdf.set_fill_color(230, 230, 230)
            else:
                self.pdf.set_fill_color(255, 255, 255)

            input_name = GV.DB_INPUTLIST.find({'_id': item['inputID']}, {'_id': 0, 'name': 1})
            module_name = GV.DB_MODULECONFIG.find({'_id': item['moduleID']}, {'_id': 0, 'name': 1})
            print (list(input_name), list(module_name))

            self.pdf.cell(self.pdf.table_size[0], 5, format(line_no), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[1], 5, format('system'), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[2], 5, format(item['inputID']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[3], 5, format(item['moduleID']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[4], 5, format(''), fill=True, ln=0, align='C')
            for output in item['outputList']:
                self.pdf.cell(self.pdf.table_size[0], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[1], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[2], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[3], 5, ' ', fill=True, ln=0, align='C')
                self.pdf.cell(self.pdf.table_size[4], 5, format(output['name']), fill=True, ln=1, align='C')
            line_no += 1
        self.save_file()

    def save_file(self):
        notification = self.parent.parent.mccm.mm_notification
        logger = self.parent.parent.mccm.mm_logger
        self.usb_detect.find_usb(self.output_file_name, notification, logger)


# ########################################### IMPORT BUTTON ########################################################## #

class ImportConnectButton(Button):
    importList = StringProperty()

    def import_csv(self):
        file_chooser = ImportDialog(self,
                                    importList=self.importList,
                                    notification=self.parent.parent.mccm.mm_notification,
                                    logger=self.parent.parent.mccm.mm_logger,
                                    )
        file_chooser.open()


class ImportObjectButton(Button):
    importList = StringProperty()

    def import_csv(self):
        file_chooser = ImportDialog(self,
                                    importList=self.importList,
                                    notification=self.parent.parent.mccm.mm_notification,
                                    logger=self.parent.parent.mccm.mm_logger,
                                    # table_object=self.obsc_list_table,
                                    )
        file_chooser.table_object = self.obsc_list_table
        file_chooser.open()


class ImportDialog(ModalView):
    importList = StringProperty()
    logger = ObjectProperty()
    notification = ObjectProperty()
    folder_path = StringProperty()
    table_object = ObjectProperty

    def __init__(self, instance, **kwargs):
        super(ImportDialog, self).__init__(**kwargs)
        if _platform == "linux" or _platform == "linux2":
            self.folder_path = './'
        elif _platform == "darwin":
            self.folder_path = '/Volumes'
        self.collection_target = []

    def import_collection_csv(self, *args):
        file = args[1][0]
        name_file = datetime.now().strftime("%Y%m%d_%H%M") + '_' + self.importList + 'List'
        if self.importList == 'input':
            self.collection_target = GV.DB_INPUTLIST
        elif self.importList == 'output':
            self.collection_target = GV.DB_OUTPUTLIST
        elif self.importList == 'object':
            self.collection_target = GV.DB_OBJECTLIST
        try:
            f = open(file, 'r')
            file_reader = csv.DictReader(f)
            self.populate_DB(file_reader)
            msg_color = 'success'
            msg_text = 'import ' + self.importList + ' list'
            logger_class = 'info'
            logger_text = 'Import file ' + name_file
            self.logger.logger_add(logger_class, logger_text)
        except OSError as err:
            msg_color = 'error'
            msg_text = "OS error: {0}".format(err)
        except:
            msg_color = 'error'
            msg_text = "Unexpected error:" + str(exc_info())
            # print(str(exc_info()))
        finally:
            self.notification.notification_msg(msg_color, msg_text)
            # os.system('rm ' + GV.DIR_BACKUP + str(name_file))

    def populate_DB(self,  file_reader):
        headers = file_reader.fieldnames
        if self.importList == 'output':
            self.collection_target.drop()
            for each in file_reader:
                row = {}
                for field in headers:
                    row[field] = each[field]
                self.collection_target.insert_one(row)
        elif self.importList == 'object':
            for each in file_reader:
                self.collection_target.update_one({'address': str(each['address'])},
                                                  {'$set': {'deck':  int(each['deck']),
                                                            'posX': float(each['posX']),
                                                            'posY': float(each['posY']),
                                                            'rotate': int(each['rotate']),
                                                            }})
            self.table_object.draw_table()
        else:
            self.collection_target.drop()
            for each in file_reader:
                row = {}
                for field in headers:
                    row[field] = each[field]
                self.collection_target.insert_one(row)


# ########################################### PRINT COMM DOC  BUTTON ################################################# #

class ComDocButton(Button):

    def __init__(self, **kwargs):
        super(ComDocButton, self).__init__(**kwargs)
        self.usb_detect = UsbFind()
        self.pdf = []
        self.output_file_name = ''

    def export_doc(self):
        self.pdf = PDFDoc()
        self.output_file_name = GV.DIR_BACKUP + 'Commissioning.pdf'
        self.pdf = PDF('P', 'mm', 'A4')
        self.first_page()

    def first_page(self):
        first = JsonStore(GV.FILE_INFO)
        print(first['Commissioning'])

    def export_input(self):
        pass

    def export_output(self):
        pass

    def export_module(self):
        pass

    def export_connections(self):
        pass


class PDFDoc(FPDF):

    def header(self):
        self.image(GV.DIR_IMAGES + 'pdf/HeaderPDF.jpg', w=0, h=19, type='JPG', link='')
        self.set_font('Arial', 'B', 18)
        self.cell(40, 15, self.title, 0, 0, 'L')
        self.set_font('Arial', '', 8)
        file_info = JsonStore(GV.DIR_JSON + GV.FILE_INFO)
        project = 'project: ' + file_info['Info']['project']
        self.cell(0, 5, project, 0, 1, 'R')
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cell(0, 5, date, 0, 1, 'R')
        self.set_line_width(0.5)
        self.set_draw_color(140, 0, 0)
        self.line(10, 42, 200, 42)
        self.ln(5)
        for count, head_tab in enumerate(self.table_header):
            self.set_font('Arial', 'B', 12)
            self.set_fill_color(200, 200, 200)
            self.cell(self.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-20)
        self.set_line_width(0.5)
        self.set_draw_color(140, 0, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.set_font('Arial', 'I', 8)
        img = GV.DIR_IMAGES + 'pdf/FooterPDF.jpg'
        self.image(img, x=self.get_x(), y=self.get_y() + 1, w=0,  h=15, type='JPG', link='')
        self.cell(0, 5, 'Page %s' % self.page_no() + '/{nb}', 0,0, 'R')