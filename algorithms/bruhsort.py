def bruhsort(array):
    arr = list(array)
    target_arr = []
    while arr:
        target_arr.append(arr.pop(arr.index(min(arr))))
        yield arr + target_arr
    return target_arr
