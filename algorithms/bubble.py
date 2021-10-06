def bubble(array):
    arr = array[:]
    max_i = len(arr) - 1
    go_on = True
    while go_on:
        go_on = False
        for i in range(max_i):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                yield arr
                go_on = True
        
