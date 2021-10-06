def insertion(array):

    arr = array[:]
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
'''
    i ← 1
while i < length(A)
    x ← A[i]
    j ← i - 1
    while j >= 0 and A[j] > x
        A[j+1] ← A[j]
        j ← j - 1
    end while
    A[j+1] ← x[3]
    i ← i + 1
end while


    arr = array[:]
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
            yield arr
        i += 1
'''