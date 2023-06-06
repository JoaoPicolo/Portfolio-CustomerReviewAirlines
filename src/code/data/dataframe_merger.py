from typing import List

import pandas as pd

class DataframeMerger:
    def __init__(self, source_files: List[str]):
        """ Useful methods for dataframe merging. """
        self.source_files = source_files


    def verify_columns_match(self, main: pd.DataFrame, dataframe: pd.DataFrame):
        """ Verifies if two dataframes match columns.
        
        Arguments:
        main: The main dataframe to be merged to.
        dataframe: The dataframe to merge into the main.

        Returns:
        bool: True if the columns match, False otherwise.
        """
        main_columns = set(main.columns)
        dataframe_columns = set(dataframe.columns)
        difference = [*main_columns.symmetric_difference(dataframe_columns)]
        return len(difference) == 0


    def sort_dataframe_columns(self, dataframe: pd.DataFrame):
        """ Sorts the dataframe columns by header names.
        
        This is useful to match columns between dataframes.

        Arguments:
        dataframe: Dataframe to be sorted by column.

        Returns:
        dataframe: Sorted dataframe.
        """
        columns = dataframe.columns
        dataframe = dataframe.reindex(sorted(columns), axis="columns")
        return dataframe
    

    def merge_dataframes(self, ignore_columns: List[str]):
        """ Merge the dataframes.
        
        Merges the dataframes originated from the source_files
        provided when instantiating the object. 

        Arguments:
        ignore_columns: List of columns to ignore during merge.

        Returns:
        table: A dataframe containg all the merged files.
        """
        table = None
        for source in self.source_files:
            print(f"Will merge dataframe located at {source}")
            dataframe = pd.read_csv(source)
            dataframe = dataframe.drop(ignore_columns, axis="columns")

            # Will merge by column name, so ignores type
            dataframe = dataframe.astype("object")

            if table is not None:
                if not self.verify_columns_match(table, dataframe):
                    print(f"Error: Dataframes do not match columns")
                    exit(1)

                dataframe = self.sort_dataframe_columns(dataframe)
                table = pd.merge(table, dataframe, on=None, how="outer")
            else:
                table = self.sort_dataframe_columns(dataframe)

        return table


    