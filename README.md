# Sorting Visualizer

CLI tool for visualizing sorting algorithms

![Alt text](/example.gif?raw=true "Bubble sort example")

##  How to use it? 🤔

1. Have python 3.6+ installed

1. Open terminal in project's main directory

1. Run `python sort.py` command, optionally add arguments

1. Maximize terminal to full screen for smoother effect

## Arguments ⚙️

`python sort.py -h` for list of algorithms and argument help

\#  | Argument | Type |  Default | Description                              | Required
| :---         |     :---:      |     :---:      |     :---:      |     :---:      |          ---: |
1\. | algorithm | str | bubble | sorting algorithm from algorithms folder | ❎ No
2\. | array_size| int | 15 | array with integers ranging from 1 to array_size + 1 | ❎ No

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

‼️ | **File name cannot start with an underscore**
:---: | :---
⚠️| **Your function must be named after your file**

### Example function ✍
```py
# ./sorting-visualizer/algorithms/myalgorithm.py

def myalgorithm(array):
  arr_copy = list(array)
  while not_sorted:
    # modify arr_copy
    yield arr_copy # function must yield updated array
                   # whenever you want to see the change
```

### Now you can visualize your algorithm running this command 👀

`python sort.py myalgorithm`
