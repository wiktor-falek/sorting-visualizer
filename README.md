# Sorting Visualizer
CLI tool for visualizing sorting algorithms

![Alt text](/example.gif?raw=true "Bubble sort example")

##  How to use it? 🤔

1. Open cmd in project's directory

1. run `python sort.py` command,  bubble sort by default

1. run cmd in full screen for smoother effect

## Arguments ⚙️

python sort.py algorithm array_size

`python sort.py -h` for argument help and list of algorithms

1. `algorithm` required, defaults to bubble sort

1. `array_size` must be between 2 and 50, defaults to 15

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

⚠️ | **File name cannot start with an underscore**
:---: | :---
‼️ | **Your function must be named after your file**


### Example function: ✍️
```py
# ./algorithms/myalgorithm.py
def myalgorithm(array):
  arr_copy = list(array)
  while True:
    # alter arr_copy
    yield arr_copy # function must yield updated array
                   # whenever you want to see the change
```

### Now you can visualize your algorithm running this command: 👀

`python sort.py myalgorithm`
