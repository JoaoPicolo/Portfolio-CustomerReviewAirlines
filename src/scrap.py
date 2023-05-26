from datetime import datetime

from utils.utils import to_snake_case
from utils.arguments import get_parser
from utils.csv_handler import CSVHandler
from parsers.json import AirlinesJSONParser
from scrapers.scrapers import AirlineWebScraper

def main():
    args = get_parser()
    csv_handler = CSVHandler()

    json_parser = AirlinesJSONParser()
    json_parser.load_json(args.input)
    airlines = json_parser.get_airlines_information()

    for airline in airlines:
        scraper = AirlineWebScraper(base_url=airline["site"],
                                    airline=airline["name"],
                                    country=airline["country"])
        dataframe = scraper.update_reviews_table(last_review_id=0)

        name = to_snake_case(airline["name"])
        now = datetime.now()
        csv_handler.save_to_csv(dataframe, path=f"{args.output}/{name}_{now}.csv")

if __name__ == "__main__":
    main()