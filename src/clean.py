from typing import List
from os import listdir

from utils.arguments import get_parser
from utils.csv_handler import CSVHandler
from data.dataframe_cleaning import DataframeCleaner

def main():
    args = get_parser()
    csv_handler = CSVHandler()
    
    files: List[str] = []
    if path.isdir(args.input):
        files = [args.input + f for f in listdir(args.input)]
    elif path.isfile(args.input):
        files.append(args.input)

    for file in files:
        dataframe = csv_handler.load_csv(path=file)
        cleaner = DataframeCleaner(dataframe)
        cleaner.clean_dataframe()
        path = file.replace("raw", "interim")
        csv_handler.save_to_csv(cleaner.get_dataframe(), path=path)

if __name__ == "__main__":
    main()