import time
from typing import Any

import requests
import pandas as pd
from bs4 import BeautifulSoup, Tag

class AirlineWebScraper():
    def __init__(self, base_url: str, airline: str, country: str, wait_secs = 0.5):
        """ Web Scraper for airline reviews.

        Reference site is: https://www.airlinequality.com/

        Arguments:
        base_url: Base URL to query.
        airline: Airline name.
        country: Country where the airline was created.
        wait_secs: Seconds to wait between each request to the website. Default 0.5
        """
        self.base_url = base_url
        self.airline = airline
        self.country = country
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
            star_value = None
            try:
                star_value = value.find_all("span", { "class": "star fill" })[-1]
            except:
                pass
            if star_value:
                value = self.get_text(star_value)
            else:
                value = self.get_text(value)
        
            review_dict[key] = value

        return review_dict


    def get_review(self, page_url: str):
        """ Gets the review for a given page.
        
        Arguments:
        page_url: Page to request the reviews.

        Returns:
        reviews: List containing all the requested reviews as dicts.
        """
        response = requests.get(page_url)
        content = BeautifulSoup(response.content, "html.parser")
        content_reviews = content.find_all("article", class_ = lambda value: value and value.startswith("review-"))
        review = content_reviews[0]
        review = self.format_review(review)
  
        return review
    

    def add_metadata(self, table: pd.DataFrame):
        """ Adds the given airline information to the table.

        Arguments:
        table: Table to add attribute.
        
        Returns:
        table: Table with added attribute.
        """
        table["airline_name"] = self.airline
        table["country"] = self.country
        return table


    def update_reviews_table(self, last_review_id: int):
        """ Stores the reviews into a table.
        
        This function will query the reviews from oldest to newest, so
        the oldest review from the airline is last_review_id = 1. Only
        one review is received per iteration, this allows to create a
        custom id that can be used later to call this function and update
        the table as needed.

        Arguments:
        last_review_id: Last review read from this airline.

        Returns:
        table: Table containing the requested reviews.
        """
        table = None

        try_max = 2
        try_count = 0

        while try_count < try_max:
            try:
                current_id = last_review_id + 1
                print(f"Will get review id {current_id}")
                url = f"{self.base_url}/page/{current_id}/?sortby=post_date%3AAsc&pagesize=1"
                review = self.get_review(url)
                review["id"] = current_id
                reviews_df = pd.DataFrame([review])
                try_count = 0       # Resets to get the next review
                last_review_id += 1 # Increments because will try to get next

                if table is not None:
                    table = pd.concat([table, reviews_df])
                else:
                    table = reviews_df
            except:
                try_count += 1

            time.sleep(self.wait_secs)

        print("Finished getting reviews")

        try:
            table = self.add_metadata(table)
        except:
            pass

        return table