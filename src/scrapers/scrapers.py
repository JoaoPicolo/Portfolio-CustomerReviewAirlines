import time
from typing import Any

import requests
import pandas as pd
from bs4 import BeautifulSoup, Tag

class AirlineWebScraper():
    def __init__(self, base_url: str, airline: str, wait_secs = 0.5):
        """ Web Scraper for airline reviews.

        Reference site is: https://www.airlinequality.com/

        Arguments:
        base_url: Base URL to query.
        airline: Airline name.
        wait_secs: Seconds to wait between each request to the website. Default 0.5
        """
        self.base_url = base_url
        self.airline = airline
        self.wait_secs = wait_secs

    
    def get_text(self, tag: Tag):
        """ Returns the text from a given tag.
        
        Arguments:
        tag: Tag to look for.

        Returns:
        text: The text from the tag.
        """
        try:
            return tag.get_text()
        except:
            return


    def format_review(self, review: Any):
        """ Formats a given review.
        
        Arguments:
        review: Review obtained from the page.

        Returns:
        review_dict: Review formatted as a dict.
        """
        review_dict = {}
        
        # Gets easy information
        try:
            review_dict["date"] = review.find("meta").get("content")
        except:
            pass
        review_dict["header"] = self.get_text(review.find("h2", { "class": "text_header" }))
        review_dict["rating"] = self.get_text(review.find("div", { "class": "rating-10" }).find("span"))
        review_dict["content"] = self.get_text(review.find("div", { "class": "text_content" }))

        # Gets information from Table
        table = review.find("table", { "class": "review-ratings" })
        data = table.find_all("td")
        keys = data[::2]
        values = data[1::2]
        for key, value in zip(keys, values):
            key = self.get_text(key)
            star_value = value.find("span", {"class": "star fill" })
            if star_value:
                value = self.get_text(star_value)
            else:
                value = self.get_text(value)
        
            review_dict[key] = value

        return review_dict


    def get_reviews(self, page_url: str):
        """ Gets the reviews for a given page.
        
        Arguments:
        page_url: Page to request the reviews.

        Returns:
        reviews: List containing all the requested reviews as dicts.
        """
        reviews = []
        response = requests.get(page_url)
        content = BeautifulSoup(response.content, "html.parser")
        content_reviews = content.find_all("article", class_ = lambda value: value and value.startswith("review-"))
        for review in content_reviews:
            result = self.format_review(review)
            reviews.append(result)

        return reviews
    

    def add_airline(self, table: pd.DataFrame):
        """ Adds the airline name to the table.

        Arguments:
        table: Table to add attribute.
        
        Returns:
        table: Table with added attribute.
        """
        table["airline_name"] = self.airline
        return table


    def get_reviews_table(self, initial_page, end_page, page_size):
        """ Stores the reviews into a table.

        Arguments:
        initial_page: Initial page index.
        end_page: End page index.
        page_size: Number of reviews per page.

        Returns:
        table: Table containing the requested reviews.
        """
        table = None
        for i in range(initial_page, end_page + 1):
            print(f"Will get reviews for page {i}")
            url = f"{self.base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
            reviews = self.get_reviews(url)
            reviews_df = pd.DataFrame(reviews)
        
            if table is not None:
                table = pd.concat([table, reviews_df])
            else:
                table = reviews_df

            time.sleep(self.wait_secs)
        
        print("Finished getting reviews")
        
        table = self.add_airline(table)
        return table