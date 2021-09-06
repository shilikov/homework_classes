import fileinput
import os
import zipfile
from collections import defaultdict
from os import path
import re




def comparator(doc):
    return len(doc)

def count(doc):
    files = []
    new_file = 'new_file.all'

    def counttt(doc):
        files = []
        if doc:
            for file_name in doc:
                with open(file_name, 'r') as file, open('all.txt', 'w') as f:
                    count = len(open(file_name).readlines())
                    files.append(file.readlines())
                    files.sort(key=comparator)
                    with open(file_name, 'r') as file, open('all.txt', 'w') as f:
                        for file in files:
                            f.write(f'\n\n------------ {file_name},\n {count}\n\n')
                            f.writelines(file)
                            f.write('\n')

    #
    counttt(['1.txt', '2.txt', '3.txt'])


    for file_name in doc:

        with open(file_name, 'r') as fr, open(new_file, 'a') as fw:
            count = len(open(file_name).readlines())
            # files.append(fr.read().splitlines())
            # files.sort(key=lambda item: len(item[2]))
            # files.append(fr.readlines())
            # files.sort(key=lambda item: len(item[2]))
            # files.sort(key=comparator)
            fw.write(f'\n\n------------ {file_name},\n {count}\n\n')
            for file in fr:
                    fw.write(file)



count(['1.txt', '2.txt', '3.txt'])



