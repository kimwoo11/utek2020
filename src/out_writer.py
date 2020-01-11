import os
import csv

osj = os.path.join

class OutputWriterP3:

    def __init__(self, file_path='.', file_name='p3_moves.out.txt'):
        self.path = os.path.join(file_path, file_name)
        self.writer = open(self.path, 'w+')

    def insert(books, idx):
        out_string = 'Insert {}-{},".format(idx[0], idx[1])
        for book in books:
            out_string += " \"{}\"".format(book)
        self.writer.write(out_string)

    def replace(books, idx):
        out_string = "Replace {}-{},".format(idx[0], idx[1])
        for book in books:
            out_string += " \"{}\"".format(book)
        self.writer.write(out_string)

    def delete(idx):
        out_string = 'Delete {}-{}'.format(idx[0], idx[1])
        self.writer.write(out_string)

    def close():
        self.writer.close()

class OutputWriterP2:
    
    def __init__(self, file_path='.', file_name='p2_moves.out.txt'):
        self.path = os.path.join(file_path, file_name)
        self.writer = open(self.path, 'w+')

    def insert(char, idx):
        out_string = "Insert {}, '{}'".format(idx, char)
        self.writer.write(out_string)

    def replace(char, idx):
        out_string = "Replace {}, '{}'".format(idx, char)
        self.writer.write(out_string)

    def delete(idx):
        out_string = 'Delete {}'.format(idx)
        self.writer.write(out_string)

    def close():
        self.writer.close()
