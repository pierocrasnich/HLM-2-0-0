from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

from threading import Thread
from pymongo import errors, DESCENDING
import time
from datetime import datetime

# -- Import Personal Utility ------------------------------------------------------------------------------------------#
import utility.gvar as GV
from classi.usbFind import UsbFind
from classi.csv import PDF


class LoggerConsoleLayout(BoxLayout):
    pass


class LoggerConsole(DragBehavior, Widget):
    sizeW = NumericProperty(700)
    sizeH = NumericProperty(400)

    def __init__(self, **kwargs):
        super(LoggerConsole, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self.change_logger = []
        self.thread_logger = []
        self.usb_detect = UsbFind()
        self.pdf = []
        self.output_file_name = ''

    def on_mouse_pos(self, *args):
        pass

    def close_console(self):
        self.pos = -5000, 50
        self.opacity = 0

    def clear_console(self):
        self.ids.console_list.data = []
        self.ids.console_list.refresh_from_data()

    def save_console(self):

        output_file_name = datetime.now().strftime("%Y%m%d_%H%M") + '_Log.pdf'
        self.pdf = PDF('P', 'mm', 'A4')
        self.pdf.set_title('LOG')

        self.pdf.table_header = []
        self.pdf.table_size = []
        self.pdf.add_page()

        self.pdf.table_header = ['Data', 'Class', 'Message']
        self.pdf.table_size = [40, 25, 125]  # tot 190 mm

        for count, head_tab in enumerate(self.pdf.table_header):
            self.pdf.set_font('Arial', 'B', 12)
            self.pdf.set_fill_color(200, 200, 200)
            self.pdf.cell(self.pdf.table_size[count], 5, format(head_tab), fill=True, border=0, ln=0, align='C')
        self.pdf.ln(5)
        self.pdf.set_font("Arial", size=9)

        line_no = 1
        for item in list(self.ids.console_list.data):
            # Line is Odd or Even
            if (line_no % 2) == 0:
                self.pdf.set_fill_color(230, 230, 230)
            else:
                self.pdf.set_fill_color(255, 255, 255)

            self.pdf.cell(self.pdf.table_size[0], 5, format(item['data_time']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[1], 5, format(item['event']), fill=True, ln=0, align='C')
            self.pdf.cell(self.pdf.table_size[2], 5, format(item['message']), fill=True, ln=1, align='L')
            line_no += 1

        self.pdf.alias_nb_pages()
        self.pdf.output(GV.DIR_BACKUP + output_file_name)

        notification = self.parent.mm_notification
        logger = self.parent.mm_logger
        self.parent.add_widget(self.usb_detect)
        self.usb_detect.find_usb(output_file_name, notification, logger)

    def minimize_console(self):
        self.size = (self.sizeW, 150)
        self.pos = (250, 50)

    def normal_console(self):
        self.size = (self.sizeW, self.sizeH)
        self.pos = (250, 50)

    def full_console(self):
        self.size = (1920, 1080)
        self.pos = (0, 0)

    def init_data(self):
        self.pos = (250, 50)
        self.change_logger = []
        records_log = GV.DB_LOGGER.find().sort('timestamp', DESCENDING)
        color_row = []
        for n_rows in records_log:
            data_time = n_rows['timestamp']
            event = n_rows['event']
            if event == 'success':
                color_row = GV.RGBA_SUCCESS
            elif event == 'info':
                color_row = GV.RGBA_WHITE50
            elif event == 'error':
                color_row = GV.RGBA_ERROR
            message = n_rows['message']
            self.ids.console_list.data.append({'color_row': color_row,
                                               'data_time': str(data_time),
                                               'event': '[ ' + str(event) + ' ]',
                                               'message': '- ' + str(message)
                                               })
        self.ids.console_list.refresh_from_data()
        self.thread_logger = Thread(target=self.watch_logger, daemon=True)
        self.thread_logger.start()

    def update_data(self, change):
        self.ids.console_list.data.append(change)
        self.ids.console_list.refresh_from_data()

    def watch_logger(self):
        if GV.DB:
            self.change_logger = GV.DB.logger.watch([
                {'$project': {
                    'fullDocument_id': '$fullDocument._id',
                    'active': '$fullDocument.active',
                    'present': '$fullDocument.present'
                    }
                }
            ], full_document='updateLookup')
            try:
                for change in self.change_logger:
                    self.update_data(change)
            except errors:
                print(errors)
        else:
            time.sleep(.5)
            self.watch_logger()