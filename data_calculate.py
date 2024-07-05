from data_define import Data
from data_reader import DataReader, TextFile, JsonFile


class DataCalculator:

    def data_calculate(self, jsFile, tFile):
        tf = TextFile.read_data(tFile)
        jf = JsonFile.read_data(jsFile)

        all_data = tf + jf

        data_dict = {}
        for data in all_data:
            if data.date in data_dict.keys():
                data_dict[data.date] += data.money
            else:
                data_dict[data.date] = data.money
        return data_dict






