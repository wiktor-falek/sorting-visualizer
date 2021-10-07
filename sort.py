from random import shuffle
import argparse
import time
import os

from _modules import * # modules = list of modules in algorithms folder


def visualize(arr, iterations):
    arr_len = len(arr)
    if not arr_len: return

    m = [[0]*max(arr) for _ in range(arr_len)]

    for i in range(arr_len):
        for j in range(arr[i]):
            m[i][j] = 1

    matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
    s = "\n"
    for array in matrix:
        for value in array:
            s += ' █' if value == 1 else '  '
        s += '\n'
    s += f'\n iterations: {iterations}'
    os.system('cls')
    print(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Visualisation of sorting algorithms")
    parser.add_argument('a', type=str, default='bubble', nargs='?',
                        help=f"available algorithms {modules}")
    parser.add_argument('s', type=int, default=15, nargs='?',
                        help="array with values ranging from 1 to size + 1 (limited to 2-70)")

    args = parser.parse_args()
    algorithm, arr_size = args.a, args.s

    if 2 > arr_size or arr_size > 50:
        raise ValueError('Array size must be in range(2, 51)')

    initial_array = [x for x in range(1, arr_size + 1)]
    array = list(initial_array)
    while array == initial_array:
        shuffle(array)

    if algorithm in modules:
        gen = eval(algorithm)(array)
    else:
        print(f"'{algorithm}' algorithm not found\navailable algorithms: {modules}")
        exit()

    iterations = 0
    alg_time = 0
    start_total_time = time.time()

    while True:
        try:
            start = time.perf_counter()
            arr = list(next(gen))
            alg_time += time.perf_counter() - start
            iterations += 1
            visualize(arr, iterations)
        except StopIteration:
            total_time = time.time() - start_total_time
            break

    print(f' total time: {total_time:.4f}s')
    print(f' algorithm time: {alg_time:.10f}s')