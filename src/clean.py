from utils.arguments import get_parser, get_files_list
from utils.csv_handler import CSVHandler
from data.dataframe_cleaning import DataframeCleaner

def main():
    args = get_parser()
    csv_handler = CSVHandler()
    
    files = get_files_list(args.input)
    for file in files:
        dataframe = csv_handler.load_csv(path=file)

        cleaner = DataframeCleaner(dataframe)
        cleaner.clean_dataframe()

        path = file.replace("raw", "interim")
        csv_handler.save_to_csv(cleaner.get_dataframe(), path=path)

if __name__ == "__main__":
    main()