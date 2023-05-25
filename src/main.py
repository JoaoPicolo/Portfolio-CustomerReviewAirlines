from datetime import datetime

from data.csv_handler import CSVHandler
from scrapers.scrapers import AirlineWebScraper

def main():
    io_handler = CSVHandler()
    
    scraper = AirlineWebScraper("https://www.airlinequality.com/airline-reviews/british-airways/", "British Airways")
    dataframe = scraper.get_reviews_table(1, 36, 100)
    

    now = datetime.now()
    io_handler.save_to_csv(dataframe, path=f"../data/raw/ba-review_{now}.csv")

if __name__ == "__main__":
    main()