# Sorting Visualizer
CLI tool for visualizing sorting algorithms

![Alt text](/example.gif?raw=true "Bubble sort example")

##  How to use it? 🤔

1. Have python 3.6+ installed

1. Open cmd in project's main directory

1. Run `python sort.py` command,  bubble sort by default

1. run cmd in full screen for smoother effect

## Arguments ⚙️

`python sort.py -h` for list of algorithms and argument help

Argument order `python sort.py algorithm array_size`

1. `algorithm = bubble` required, use command above to see available algorithms

1. `array_size = 15` required must be in range(2, 51)

### Example

`python sort.py insertion 20` sorts array of numbers in range(1, 21) using insertion sort

## Built-in Algorithms

### Stable

  * #### O(n^2)

    * Bubble

    * Insertion

### Unstable

  * #### O((n+1)!)

    * Bogosort 💩

## How to add your own algorithm? 💪

Create file in **algorithms** folder, for example myalgorithm.py

‼️ | **Your function must be named after your file**
:---: | :---
⚠️ | **File name cannot start with an underscore**

### Example function: ✍️
```py
# ./sorting-visualizer/algorithms/myalgorithm.py
def myalgorithm(array):
  arr_copy = list(array)
  while True:
    # alter arr_copy
    yield arr_copy # function must yield updated array
                   # whenever you want to see the change
```

### Now you can visualize your algorithm running this command: 👀

`python sort.py myalgorithm`
