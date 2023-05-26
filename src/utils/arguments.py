import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Path to red the original .csv file")
    parser.add_argument("-o", "--output", type=str, help="Path to save the manipulated .csv file")
    args = parser.parse_args()

    return args