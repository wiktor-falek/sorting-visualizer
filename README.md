## CLI TOOL FOR VISUALIZING SORTING ALGORITHMS

#### How to use?

`'python sort.py' ` bubble sort by default

`'python sort.py -h'` for argument help 

#### How to add your own algorithm?

create file in ./algorithms for example timsort.py

create a sorting function named after your file

example function:
```py
def timsort(array):
  arr_copy = array[:]
  while True:
    # swap arr_copy
    yield arr_copy # function must yield whenever you want to see the change
```
