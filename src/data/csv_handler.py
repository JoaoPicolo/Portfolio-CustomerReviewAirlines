import pandas as pd

class CSVHandler():
    def __init__(self):
        """ Input/Output Handler class. """

    def load_csv(self, path: str):
        """ Loads the .csv path into a pandas dataframe.

        Parameters:
        path: Path to the .csv file

        Returns:
        dataframe: Returns the created pandas dataframe.
        """
        dataframe = pd.read_csv(path)
        return dataframe
    

    def save_to_csv(self, dataframe: pd.DataFrame, path: str):
        """ Saves the dataframe in the provided path as a .csv file.

        Parameters:
        dataframe: Dataframe to be saved.
        path: Path to the .csv file.
        """
        dataframe.to_csv(path, index=False)
