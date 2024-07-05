import json
from data_define import Data


class DataReader:

    def read_data(self):
        pass


class TextFile(DataReader):
    path = None

    def __init__(self, path):
        self.path = path

    def read_data(self):
        f_handle = open(self.path, 'r', encoding='utf-8')

        record_list = []
        for line in f_handle.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Data(data_list[0], data_list[1], data_list[2], data_list[3])
            record_list.append(record)

        f_handle.close()
        return record_list


class JsonFile(DataReader):
    path = None

    def __init__(self, path):
        self.path = path

    def read_data(self):
        f_handle = open(self.path, 'r', encoding='utf-8')

        record_list = []
        for line in f_handle.readlines():
            data_dict = json.loads(line)
            record = Data(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)

        f_handle.close()
        return record_list


