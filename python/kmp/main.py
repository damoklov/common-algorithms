from time import time
from knuth_morris_pratt import *


def read_string(filename):
    with open(filename, 'r') as f:
        string = f.readline().rstrip()
        target = f.readline().rstrip()
    return string, target


def main(filename):
    string, target = read_string(filename)
    start = time()
    pi_list = kmp(string, target)
    end = time() - start
    print("Entry points: ", pi_list)
    print("Time taken: ", end)
    return pi_list


if __name__ == '__main__':
    main("test2.txt")

