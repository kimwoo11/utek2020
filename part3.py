import argparse
from src.parse_input import *
from src.out_writer import *

def main(arguments):
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Librarians Dilemma')
    parser.add_argument('--input_path', required=True, help='Pass input file path to --input_path')
    args = parser.parse_args()
    original, desired = parse(args)
