import csv

from pbx_gs_python_utils.utils.Files import Files

class Data_CSV:
    def __init__(self):
        self.data_folder = Files.path_combine(__file__,'../../data')

    def csv_files(self):
        files = {}
        for file_path in Files.find(self.data_folder + '/*'):
            file_name = Files.file_name(file_path)
            files[file_name] = file_path
        return files

    def csv_file_raw_data(self, file_name):
        file_path = self.csv_files().get(file_name)
        return Files.contents(file_path)

    def csv_2_dict(self, file_name):
        file_path = self.csv_files().get(file_name)
        out_dict = {}
        with open(file_path) as csv_records:
            reader = csv.DictReader(csv_records)
            for i, row in enumerate(reader):
                out_dict[i] = row
        return out_dict
