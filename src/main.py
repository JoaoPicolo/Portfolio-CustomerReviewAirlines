from datetime import datetime

from utils.arguments import get_parser
from data.csv_handler import CSVHandler
from data.dataframe_cleaning import DatafremeCleaner
from scrapers.scrapers import AirlineWebScraper

def main():
    args = get_parser()

    csv_handler = CSVHandler()
    
    # Scraps the web
    scraper = AirlineWebScraper("https://www.airlinequality.com/airline-reviews/british-airways/", "British Airways")
    dataframe = scraper.get_reviews_table(1, 36, 100)

    # Cleans the dataframe
    cleaner = DatafremeCleaner(dataframe)
    cleaner.clean_dataframe()

    now = datetime.now()
    csv_handler.save_to_csv(cleaner.get_dataframe(), path=f"{args.output}/ba-review-{now}.csv")

if __name__ == "__main__":
    main()