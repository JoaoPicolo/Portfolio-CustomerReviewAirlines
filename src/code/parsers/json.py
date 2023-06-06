from typing import List, Dict

import json

class JSONParser():
    def __init__(self):
        """ Class used to manipulate JSON files. """
        self.json: Dict = None


    def load_json(self, path: str):
        """ Reads the JSON from a given path.
        
        Arguments:
        path: Patht to the JSON to be read.
        """
        try:
            file = open(path, 'r')
            self.json = json.load(file)
            file.close()
        except ValueError as e:
            print("Error reading JSON", e)


class AirlinesJSONParser(JSONParser):
    def __init__(self):
        """ Class used to manipulate the airline's JSON. """
        pass


    def get_airlines_information(self):
        """ Returns the content of the airline's file in an array.
        
        Each airline is a dict containing country, airline and site
        (referencing the review site).

        Returns:
        airlines: Array with dict the content described above.
        """
        if self.json is None:
            print("Make sure to load the JSON file")
            raise ValueError()

        airlines: List[Dict] = []
        for _, value in self.json.items():
            airlines.append(value)

        return airlines

    