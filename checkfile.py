import os.path
from readfile import read_file


def choose_file():
    path_txt = './data/base_teste.txt'
    path_csv = './data/base_teste.csv'

    if os.path.isfile(path_csv):
        return path_csv
    if os.path.isfile(path_txt):
        return path_txt

    raise Exception(
        " [teste-neoway] -> ERROR: Could not find 'base_teste' file")


def check_file():
    base_file = choose_file()

    print(' ')
    print(" [teste-neoway] -> Found a 'base_teste' file")
    print(' ')
    print(' [teste-neoway] -> Reading the file...')

    try:
        reading_file = read_file(base_file)
        print(' ')
        print(' [teste-neoway] -> File was read, sending to database')
        return reading_file
    except Exception as e:
        print(' ')
        print(' [teste-neoway] -> ERROR')
        print(' [teste-neoway] ->', e)
