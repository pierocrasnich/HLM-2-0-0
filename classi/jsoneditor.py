from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore


class JsonEditorPopup(Popup):
    filename = StringProperty()
    json_file_read = StringProperty()
    obj = ObjectProperty(None)

    def __init__(self, obj, json_file, *args):
        super(JsonEditorPopup, self).__init__(*args)
        self.filename = json_file
        self.obj = obj
        self.read_file = JsonStore(self.filename)
        for items in self.read_file:
            self.json_file_read = '{\n\t"' + items + '": { \n'
            element = self.read_file.get(items)
            i = 0
            for key, value in element.items():
                self.json_file_read += '\t\t"' + key + '": '
                if isinstance(value, dict):
                    self.json_file_read += '{\n'
                    m = 0
                    for x, y in value.items():
                        self.json_file_read += '\t\t\t"' + str(x) + '": '
                        if isinstance(y, dict):
                            self.json_file_read += '{\n'
                            n = 0
                            for a, b in y.items():
                                self.json_file_read += '\t\t\t\t"' + str(a) +'": "' + str(b) + '"'
                                n += 1
                                if n == len(y):
                                    self.json_file_read += '\n'
                                else:
                                    self.json_file_read += ',\n'
                            self.json_file_read += '\t\t\t}'
                        else:
                            self.json_file_read += '"' + str(y) + '"'
                        m += 1
                        if m == len(value):
                            self.json_file_read += '\n'
                        else:
                            self.json_file_read += ',\n'
                    self.json_file_read += '\t\t}'
                else:
                    self.json_file_read += '"' + value + '"'
                i += 1
                if i == len(element):
                    self.json_file_read += '\n'
                else:
                    self.json_file_read += ',\n'
            self.json_file_read += '\t}\n}'

    def save(self, text_to_save):
        f = open(self.filename, "w")
        f.write(text_to_save)
        f.close()
        if self.filename == 'json/information.json':
            self.obj.update_info()
        else:
            self.obj.drop_collection(self.filename)