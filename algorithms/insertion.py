def insertion(array):
    arr = list(array)
    i = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
            yield arr
        arr[j+1] = x
        i += 1
        yield arr