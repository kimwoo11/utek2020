import argparse

def main(arguments):
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Librarians Dilemma')
    parser.add_argument('--input_path', required=True, help='path to input file with extension .in')
    args = parser.parse_args()
    main(args)
