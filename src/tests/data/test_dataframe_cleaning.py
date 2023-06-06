import re

import pandas as pd

from code.data.dataframe_cleaning import DataframeCleaner

class TestDataframeCleaner:
    def test_get_dataframe(self, random_dataframe):
        """ Test if dataframe is valid """
        cleaner = DataframeCleaner(random_dataframe)
        df = cleaner.get_dataframe()
        assert isinstance(df, pd.DataFrame)


    def test_drop_duplicates(self, random_dataframe):
        """ Test if duplicates are being dropped """    
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.drop_duplicates(["id"])
        df = cleaner.get_dataframe()
        duplicates = len(df["id"]) - len(df["id"].drop_duplicates())
        assert duplicates == 0


    def test_standardize_headers(self, random_dataframe):
        """ Test if headers are snake case """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.standardize_headers()
        df = cleaner.get_dataframe()

        snake_pattern = r"^[a-z][a-z0-9_&]*$"
        assert all(re.match(snake_pattern, item) for item in df.columns)

    
    def test_series_clean(self, random_dataframe):
        """ Test if trailling chars are being removed from Series """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.series_clean("header", '"')
        df = cleaner.get_dataframe()
        series = df["header"]

        assert not series.str.startswith('"').any()
        assert not series.str.endswith('"').any()

    
    def test_split_series(self, random_dataframe):
        """ Test if Series is being correctly split """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.split_series(ori_series="content", new_series="trip_verified", separator='|')
        df = cleaner.get_dataframe()

        assert df["content"] is not None
        assert df["trip_verified"] is not None


    def test_categorical_to_bool(self, random_dataframe):
        """ Test if categorical columns are being correctly converted """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.categorical_to_bool(series_name="Recommended", true_value="yes")
        df = cleaner.get_dataframe()

        assert df["Recommended"].dtype.name == "bool"


    def test_fill_nan(self, random_dataframe):
        """ Test if filling NaN is working """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.categorical_to_bool(series_name="Recommended", true_value="yes")
        cleaner.fill_nan(column_types=["object"], fill_value="NA")
        df = cleaner.get_dataframe()

        for col in df:
            if df[col].dtype.name == "object":
                assert df[col].isnull().sum() == 0


    def test_strip_categorical_columns(self, random_dataframe):
        """ Test if columns have an empty space in the start/end """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.categorical_to_bool(series_name="Recommended", true_value="yes")
        cleaner.strip_categorical_columns()
        df = cleaner.get_dataframe()

        for col in df:
            if df[col].dtype.name == "object":
                assert not df[col].str.startswith(' ').any()
                assert not df[col].str.endswith(' ').any()


    def test_clean_dataframe(self, random_dataframe):
        """ Test if the dataframe return is valid.

        All the functions applied in this function were
        already testest previously
        """
        cleaner = DataframeCleaner(random_dataframe)
        cleaner.clean_dataframe()
        df = cleaner.get_dataframe()
        assert isinstance(df, pd.DataFrame)

