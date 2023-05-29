import os
from typing import List

import argparse

def get_parser():
    """ Creates a parser to get variables from stdin. """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Path to input file")
    parser.add_argument("-o", "--output", type=str, help="Directory path to save the output file")
    args = parser.parse_args()

    return args


def get_files_list(input_path: str):
    """ Creates a parser to get variables from stdin.
    
    Arguments:
    input_path: Path to directory where files are located, or path to single file.

    Returns:
    files: List containing the path to all the files provided.
    """
    files: List[str] = []
    if os.path.isdir(input_path):
        files = [input_path + "/" + f for f in os.listdir(input_path)]
    elif os.path.isfile(input_path):
        files.append(input_path)

    return files