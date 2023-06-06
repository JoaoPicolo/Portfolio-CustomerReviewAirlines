import pandas as pd

from code.data.dataframe_merger import DataframeMerger

class TestDataframeMerger:
    def test_verify_columns_match(self, dataframe_paths):
        """ Tests if dataframes have the same columns """
        merger = DataframeMerger(dataframe_paths)
        fst_df, scd_df = pd.read_csv(dataframe_paths[0]), pd.read_csv(dataframe_paths[1])
        
        matching = merger.verify_columns_match(fst_df, scd_df)
        assert matching == True


    def test_sort_dataframe_columns(self, dataframe_paths):
        """ Tests if columns are being correctly sorted """
        merger = DataframeMerger(dataframe_paths)
        fst_df = pd.read_csv(dataframe_paths[0])

        dataframe = merger.sort_dataframe_columns(fst_df)
        columns = [*dataframe.columns]
        assert sorted(columns) == columns

    
    def test_merge_dataframes(self, dataframe_paths):
        """ Tests if columns are being correctly sorted """
        merger = DataframeMerger(dataframe_paths)
        merged = merger.merge_dataframes(ignore_columns=["id"])
        assert isinstance(merged, pd.DataFrame)

