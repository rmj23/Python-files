# Day 12 Exercise  (PA6)

"""
Part 1:
The functions below are a sequential search and a binary search. (The binary search does not have the sorting part.)
We also have defined a list called sizes, from 10 to 1000,000.

Let do a comparison, for each size value, you need to:
1) generate that number of random integer values (from 1 to 1000,0000) in a list
2) run a sequential search of -1 and track the time
3) sort the list using .sort() method
4) run a binary search of -1 on the sorted list, and record the time of sorting and binary search
5) Answer this question with a visualization: if we add the sorting time to the binary search, is binary search still faster
   when searching for only one value in an unsorted list? You can make the visualization with Excel.
6) Submit a visualization and your code.
"""

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

def binSearch(list, target):
    return binSearchHelper(list, target, 0, len(list) - 1)

def binSearchHelper(list, target, left, right):
    if left > right:
        return False

    middle = (left + right)//2
    if list[middle] == target:
        return True
    elif list[middle] > target:
        return binSearchHelper(list, target, left, middle - 1)
    else:
        return binSearchHelper(list, target, middle + 1, right)

import random
import time


list_sizes = [10,100,1000,10000,100000,1000000]
alist = []
for x in list_sizes:
    for n in range(x):
        randnumber = random.randint(1, 1000000)
        alist.append(randnumber)

    start = time.clock()
    sequentialSearch(alist, -1)
    end = time.clock()

    start1 = time.clock()
    alist.sort()
    binSearch(alist, -1)
    end1 = time.clock()

    print(x, end-start, end1-start1)

print("---"*20)
print("if we add the sorting time to the binary search, is binary search still faster when searching for only one value in an unsorted list? \n\t")
print("\t binary search is not faster than sequential, regardless if we add the sorting or not")