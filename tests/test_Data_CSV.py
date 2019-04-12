from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Misc import Misc
from pbx_gs_python_utils.utils.Files import Files

from graphresolver.Data_CSV import Data_CSV


class test_Data_CSV(TestCase):

    def setUp(self):
        self.data_csv = Data_CSV()

    def test__init__(self):
        assert Files.exists(self.data_csv.data_folder)

    def test_csv_files(self):
        files = self.data_csv.csv_files()
        assert set(files) == { 'Resolver_Data.csv','Extract_AD.csv', 'Extract_DT.csv','Extract_Landesk.csv', 'Extract_AV.csv', 'Extract_Deskplan.csv'}
        for file in files.values():
            assert Files.exists(file)

    def test_csv_file_raw_data(self):
        data = self.data_csv.csv_file_raw_data('Extract_AD.csv')
        assert len(data.split('\n')) == 12

    def test_csv_2_dict(self):
        data = self.data_csv.csv_2_dict('Extract_AD.csv')
        assert len(data)       == 11
        assert data[0]['Name'] ==  'DESKTOP-8JFN77A'