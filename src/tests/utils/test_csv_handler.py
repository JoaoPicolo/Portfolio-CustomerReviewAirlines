import pandas as pd

from code.utils.csv_handler import CSVHandler

class TestCSVHandler:
    def test_load_csv(self, dataframe_paths):
        """ Tests if dataframes are being loaded """
        handler = CSVHandler()
        df = handler.load_csv(dataframe_paths[0])
        assert isinstance(df, pd.DataFrame)


    def test_save_csv(self, dataframe_paths):
        """ Tests if dataframes are being saved """
        handler = CSVHandler()
        dataframe = handler.load_csv(dataframe_paths[0])
        res = handler.save_to_csv(dataframe, dataframe_paths[0])
        assert res == None