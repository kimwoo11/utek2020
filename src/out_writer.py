import os
import csv

osj = os.path.join

class OutputWriterP3:

    def __init__(self, file_path='./results', file_name='p3_moves'):
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        name = file_name + '.out'
        self.path = os.path.join(file_path, name)
        self.writer = open(self.path, 'w+')

    def insert(self, books, idx):
        out_string = "Insert {}-{},".format(idx[0], idx[1])
        for book in books:
            out_string += " \"{}\"".format(book)
        self.writer.write(out_string)

    def replace(self, books, idx):
        out_string = "Replace {}-{},".format(idx[0], idx[1])
        for book in books:
            out_string += " \"{}\"".format(book)
        self.writer.write(out_string)

    def delete(self, idx):
        out_string = 'Delete {}-{}'.format(idx[0], idx[1])
        self.writer.write(out_string)

    def close(self):
        self.writer.close()

class OutputWriterP2:
    def __init__(self, file_path='./results', file_name='p2_moves'):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        
        name = file_name + '.out'
        self.path = os.path.join(file_path, name)
        self.writer = open(self.path, 'w+')

    def insert(self, char, idx):
        out_string = "Insert {}, '{}'".format(idx, char)
        self.writer.write(out_string)

    def replace(self, char, idx):
        out_string = "Replace {}, '{}'".format(idx, char)
        self.writer.write(out_string)

    def delete(self, idx):
        out_string = 'Delete {}'.format(idx)
        self.writer.write(out_string)

    def close(self):
        self.writer.close()
