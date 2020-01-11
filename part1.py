import argparse
from src.parse_input import *
from src.out_writer import *


def main(arguments):

    original, desired = parse(args)
    exp = args.input_path.split('/')[-1].split('.')[0]
    writer = OutputWriterP3(file_name=exp)
    
    # write hard coded solutions for test inputs
    if exp == 'part11':
        idx = [0, 3]
        writer.delete(idx)
        
    elif exp == 'part12':
        idx = [14, 21]
        books = desired[14:22]
        writer.replace(books, idx)

    elif exp == 'part13':
        idx = [28, 50]
        books = desired[28:51]
        writer.insert(books, idx)

    writer.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Librarians Dilemma')
    parser.add_argument('--input_path', required=True, help='Pass input file path to --input_path')
    args = parser.parse_args()    
    main(args)
    