import os
from typing import List

import pandas as pd

from utils.arguments import get_parser
from utils.csv_handler import CSVHandler

def main():
    args = get_parser()
    csv_handler = CSVHandler()
    
    dataframe = csv_handler.load_csv("../data/processed/reviews.csv")
    sub = dataframe[dataframe["cabin_staff_service"] >= 0]
    print(sub["cabin_staff_service"].mean())

    exit(0)
    
    files: List[str] = []
    if os.path.isdir(args.input):
        files = [args.input + "/" + f for f in os.listdir(args.input)]
    elif os.path.isfile(args.input):
        files.append(args.input)

    columns_to_ignore = ["id", "header", "content", "date_flown", "route"]

    table = None
    for file in files:
        # Reads df and sort its columns to make debug easier
        dataframe = csv_handler.load_csv(path=file)
        dataframe = dataframe.drop(columns_to_ignore, axis="columns")
        dataframe = dataframe.reindex(sorted(dataframe.columns), axis=1)

        # Will merge by column name, so ignore type for now
        dataframe = dataframe.astype("object")

        if table is not None:
            table_columns = set(table.columns)
            dataframe_columns = set(dataframe.columns)
            difference = [*table_columns.symmetric_difference(dataframe_columns)]
            if len(difference) > 0:
                print(f"Dataframes do not match columns. Symmetric difference is: {difference}")
                exit(0)

            table = pd.merge(table, dataframe, on=None, how="outer")
        else:
            table = dataframe

    csv_handler.save_to_csv(table, path=args.output)
        

if __name__ == "__main__":
    main()