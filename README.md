# Sorting Visualizer
CLI tool for visualizing sorting algorithms

##  How to use it? 🤔

Open cmd in project's directory

`python sort.py` bubble sort by default

`python sort.py -h` for argument help 

## How to add your own algorithm? 💪

Create file in algorithms folder, for example timsort.py

NOTE: file name cannot start with `_` an underscore

Create a sorting function named after your file

### Example function: ✍️
```py
# ./algorithms/timsort.py
def timsort(array):
  arr_copy = array[:]
  while True:
    # swap arr_copy
    yield arr_copy # function must yield whenever you want to see the change
```

Now you can visualize your timsort algorithm running this command: 👀

`python sort.py timsort`
