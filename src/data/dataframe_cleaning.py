import re

import pandas as pd

class DatafremeCleaner():
    def __init__(self, dataframe: pd.DataFrame):
        """ Useful methods for dataframe cleaning. """
        self.dataframe = dataframe


    def get_dataframe(self):
        """ Returns the current dataframe manipulated by this class. """
        return self.dataframe


    def standardize_headers(self):
        """ Standardizes the dataframe's header using snake case. """
        new_columns = { col: re.sub(r"\s+", '_', col.lower()) for col in self.dataframe.columns }
        self.dataframe = self.dataframe.rename(columns=new_columns)


    def series_clean(self, series_name: str, value: str):
        """ Removes a given value from a categorical Series.

        Since this method is used on categorical values, it also
        capitalized the Series to make it look cleaner.

        Arguments:
        series_name: Name of the Series to be updated.
        value: Value to be removed.
        """
        self.dataframe[series_name] = self.dataframe[series_name].str.strip(value)
        self.dataframe[series_name] = self.dataframe[series_name].str.capitalize()


    def split_series(self, ori_series: str, new_series: str, separator: str):
        """ Splits a categorical Series using a given separator.
        
        This method looks for the given separator until it finds its
        first occurence, then splits. The original Series will contain
        its original value followed by the separator, and the new Series
        will contain the value before the separator.

        Arguments:
        ori_series: Original Series name.
        new_series: Name to be given to the new Series.
        separator: Separator to be used as split condition.
        """
        split_series = self.dataframe[ori_series].str.split(pat=separator, n=1, expand=True)
        self.dataframe[new_series] = split_series[0]
        self.dataframe[ori_series] = split_series[1]


    def categorical_to_bool(self, series_name: str, true_value: str):
        """ Given a true value, converts a categorical Series to Boolean.
        
        Arguments:
        series_name: Name of the Serie to be updated.
        true_value: Value to be used on comparison.
        """
        true_value = true_value.lower()
        self.dataframe[series_name] = self.dataframe[series_name].str.lower()

        true_array = self.dataframe[series_name].str.contains(true_value)
        self.dataframe[series_name] = true_array


    def fill_na(self, fill_value: str):
        """ Fills NaN values in the whole dataframe with a given value.

        Note: By the end of this process, all columns will be of type categorical.
        
        Arguments:
        fill_value: Value to be used on filling.
        """
        for col in self.dataframe:
            self.dataframe[col] = self.dataframe[col].astype("str")

        self.dataframe = self.dataframe.replace("nan", fill_value)
        self.dataframe = self.dataframe.replace("None", fill_value)


    def strip_categorical_columns(self):
        """ Strips blank spaces from categorical columns. """
        for col in self.dataframe:
            if self.dataframe[col].dtype.name == "object":
                self.dataframe[col] = self.dataframe[col].str.strip()


    def clean_dataframe(self):
        """ Cleans the given dataframe. """
        self.standardize_headers()

        self.series_clean(series_name="header", value='"')

        self.split_series(ori_series="content", new_series="verified_trip", separator='|')
        self.series_clean(series_name="content", value='"')

        self.categorical_to_bool(series_name="verified_trip", true_value="Trip Verified")
        self.categorical_to_bool(series_name="recommended", true_value="Yes")

        self.fill_na(fill_value="Not informed")

        self.strip_categorical_columns()

