import os

import pytest
import numpy as np
import pandas as pd

@pytest.fixture(scope="function")
def random_dataframe():
    """ Creates a DataFrame to be used on testing """
    base_dir = "./src/tests/raw_csv/"
    files = os.listdir(base_dir)
    file = np.random.choice(files)
    
    df = pd.read_csv(base_dir+file)
    return df


@pytest.fixture(scope="function")
def dataframe_paths():
    """ Returns all DataFrame paths to be used on testing """
    base_dir = "./src/tests/raw_csv/"
    
    results = []
    files = os.listdir(base_dir)
    for file in files:
        results.append(base_dir + file)

    return results


@pytest.fixture(scope="function")
def json_path():
    """ Returns all the path to the airlines json """
    path = "./src/tests/raw_json/airlines.json"
    return path


@pytest.fixture(scope="function")
def airline_info():
    """ Returns a airline information """
    airline = {
        "country": "United States",
        "name": "American Airlines",
        "site": "https://www.airlinequality.com/airline-reviews/american-airlines/"
    }
    return airline

