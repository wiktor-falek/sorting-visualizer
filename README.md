# Sorting Visualizer
CLI tool for visualizing sorting algorithms

![Alt text](/example.gif?raw=true)

##  How to use it? 🤔

Open cmd in project's directory

`python sort.py` bubble sort by default

run cmd in full screen for smoother effect

## Arguments ⚙️

python sort.py algorithm array_size

`-h` shows argument help and list of algorithms

`algorithm` for list of algorithms see below, defaults to bubble

`array_size` must be between 2 and 50, defaults to 15

## Built-in Algorithms

### Stable

* #### O(n^2)

*  Bubble

*  Insertion

### Unstable

* #### O((n+1)!)

*  Bogosort 💩

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

### Now you can visualize your timsort algorithm running this command: 👀

`python sort.py timsort`
