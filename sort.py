from random import shuffle
import argparse
import time
import os

from _modules import * # modules = list of modules in algorithms folder


def visualize(arr):
    arr_len = len(arr)
    
    m = [[0]*max(arr) for _ in range(arr_len)]

    for i in range(arr_len):
        for j in range(arr[i]):
            m[i][j] = 1

    matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
    os.system('cls')
    for array in matrix:
        for value in array:
            print('█' if value == 1 else ' ', end=' ')
        print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Visualisation of sorting algorithms")
    parser.add_argument('a', type=str, default='bubble', nargs='?',
                        help=f"available algorithms {modules}")
    parser.add_argument('s', type=int, default=15, nargs='?',
                        help="array size with values ranging from 1 to size + 1")
    parser.add_argument('t', default=0, type=int, nargs='?',
                        help="delay between each update in ms")

    args = parser.parse_args()
    algorithm, arr_size, ms_delay = args.a, args.s, args.t

    array = [x for x in range(1, arr_size + 1)]
    shuffle(array)

    if algorithm in modules:
        gen = eval(algorithm)(array)
    else:
        print(f'algorithm not found\navailable algorithms: {modules}')
        exit()

    while True:
        if ms_delay > 0:
            time.sleep(ms_delay/1000)
        try:
            arr = list(next(gen))
            visualize(arr)
        except StopIteration:
            break