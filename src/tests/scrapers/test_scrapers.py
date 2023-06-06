from typing import Dict

import pandas as pd
from bs4 import BeautifulSoup

from code.scrapers.scrapers import AirlineWebScraper

class TestAirlineWebScraper:
    def test_get_text(self, airline_info):
        """ Verifies if text is being returned """
        airline = airline_info
        scraper = AirlineWebScraper(airline["site"], airline["name"], airline["country"])

        soup = BeautifulSoup()
        tag = soup.new_tag("p")
        tag.string = "My tag"
        res = scraper.get_text(tag)
        assert res == tag.string


    def test_add_metadata(self, airline_info):
        """ Verifies if metadata is being added """
        airline = airline_info
        scraper = AirlineWebScraper(airline["site"], airline["name"], airline["country"])

        data = { "week": [3, 2], "day": ['m', 's'] }
        df = pd.DataFrame.from_dict(data)
        df = scraper.add_metadata(df)

        assert df["airline_name"] is not None
        assert df["country"] is not None


    def test_get_review(self, airline_info):
        """ Tests if airline info is being captured """
        airline = airline_info
        scraper = AirlineWebScraper(airline["site"], airline["name"], airline["country"])
        url = f"{airline['site']}/page/1/?sortby=post_date%3AAsc&pagesize=1"
        review = scraper.get_review(url)
        assert isinstance(review, Dict)


    def test_update_reviews_table(self, airline_info):
        """ Verifies web scrapping process """
        airline = airline_info
        scraper = AirlineWebScraper(airline["site"], airline["name"], airline["country"])
        dataframe = scraper.update_reviews_table(1, 2)
        assert isinstance(dataframe, pd.DataFrame)