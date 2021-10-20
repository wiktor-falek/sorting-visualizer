# Sorting Visualizer
CLI tool for visualizing sorting algorithms

![Alt text](/example.gif?raw=true "Bubble sort example")

##  How to use it? 🤔

1. Have python 3.6+ installed

1. Open terminal in project's main directory

1. Run `python sort.py` command, uses bubble sort by default

1. Maximize terminal to full screen for smoother effect

## Arguments ⚙️

`python sort.py -h` for list of algorithms and argument help

\#  | Argument  | Type |  Default | Description                              | Required
| :---         |     :---:      |     :---:      |     :---:      |     :---:      |          ---: |
\1.  | algorithm | str  | bubble   | sorting algorithm from algorithms folder | ✔️ Yes
\2.  | array_size| int  | 15       | size of array ` range(1, array_size+1)`  | ✔️ Yes

### Example

`python sort.py insertion 20` sorts array of numbers in range(1, 21) using insertion sort

## Built-in Algorithms

### Stable 👍

  * #### O(n^2)

    * Bubble

    * Insertion

### Unstable 👎

  * #### O(n!) 💀

    * Bogosort 💩

## How to add your own algorithm? 💪

Create .py file in **algorithms** folder, for example myalgorithm.py

‼️ | **Your function must be named after your file**
:---: | :---
⚠️ | **File name cannot start with an underscore**

### Example function ✍
```py
# ./sorting-visualizer/algorithms/myalgorithm.py

def myalgorithm(array):
  arr_copy = list(array)
  while not_sorted:
    # modify arr_copy
    yield arr_copy # function must yield updated array
                   # whenever you want to see the change
  # function should yield until array is sorted
```

### Now you can visualize your algorithm running this command 👀

`python sort.py myalgorithm`
