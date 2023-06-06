import pytest

from code.parsers.json import JSONParser, AirlinesJSONParser

class TestJSONParser:
    def test_load_json(self, json_path):
        """ Tests if JSON is being correctly loaded """
        parser = JSONParser()
        res = parser.load_json(json_path)
        assert res == None

    def test_load_json_invalid(self):
        """ Tests if JSON is being correctly loaded """
        parser = JSONParser()
        with pytest.raises(FileNotFoundError):
            _ = parser.load_json("./file.json")


class TestAirlinesJSONParser:
    def test_get_airlines_information(self, json_path):
        """ Tests if airlines are being correctly loaded """
        parser = AirlinesJSONParser()
        parser.load_json(json_path)
        res = parser.get_airlines_information()
        
        complete = True
        for item in res:
            if ((item["country"] is None)
                or (item["name"] is None)
                or (item["site"] is None)
            ):
                complete = False
                break

        assert complete == True


    def test_get_airlines_information_no_json(self):
        """ Tests if airlines are being correctly loaded """
        parser = AirlinesJSONParser()
        with pytest.raises(FileNotFoundError):
            _ = parser.load_json("./file.json")