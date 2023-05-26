import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Path to input file")
    parser.add_argument("-o", "--output", type=str, help="Directory path to save the output file")
    args = parser.parse_args()

    return args