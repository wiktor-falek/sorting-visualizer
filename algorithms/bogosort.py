from random import shuffle

def is_sorted(array):
    return all([a <= b for a, b in zip(array, array[1:])])

def bogosort(array):
    arr_copy = array[:]
    while not is_sorted(arr_copy):
        shuffle(arr_copy)
        yield arr_copy
