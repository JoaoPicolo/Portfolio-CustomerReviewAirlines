from utils.arguments import get_parser, get_files_list
from utils.csv_handler import CSVHandler
from data.dataframe_merger import DataframeMerger

def main():
    args = get_parser()

    files = get_files_list(args.input)
    merger = DataframeMerger(files)

    merged = merger.merge_dataframes(ignore_columns=[
        "id", "header", "content", "date_flown", "route"
    ])

    csv_handler = CSVHandler()
    csv_handler.save_to_csv(merged, path=args.output)
        

if __name__ == "__main__":
    main()