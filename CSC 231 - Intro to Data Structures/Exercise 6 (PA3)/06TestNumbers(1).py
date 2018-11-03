# Day 6 Exercise (will be counted as Programing Assignment 3)
import random
import time
"""
Part1: generating a list of random numbers
Set a variable, n, to be 100.
Using a loop, create a list that has n random integers in it (all between 0 and 2*n).
The list should be named "my_list"
Sort the numbers in my_list and print out my_list.
"""
n = 100
my_list = []

for x in range(n):
    random_number = random.randint(2, 2*n)
    my_list.append(random_number)

my_list.sort()
print(my_list)

"""
Part 2: sequential search
Write a method called sequential_search(some_list, x).  The first argument will be a list, the second argument is an 
element that might be in a list.
sequential_search(some_list, x) should return true if x is in the list; false otherwise.  
Do not use the built-in list methods to see if x is in there.  Just iterate to find it (or not).
"""
def sequential_search(some_list, x):
    for number in some_list:
        if number == x:
            return True

    return False

"""
Part 3: searching for -1 in my_list, and time the search
Time how long it takes to find some number (-1) that is not in the list. 
 “start = time.clock()”   “end = time.clock()”.   The total time is end - start.
Print out (on one line), the value of n, a tab, and the total time.
"""
start = time.clock()
sequential_search(my_list, -1)
end = time.clock()

print(n, "\t", (end - start))

"""
Part 4: increasing the list size and plot the time taken by each search
Take all of the code (not including the method find) and put it inside a loop that varies n from 50000 to 1000000, step 50000.   
“for n in range(50000, 1000000, 50000):”

Copy and paste the data you just produced into a spreadsheet in Excel.
Make the first column 50000, 100000, 150000...
Make the 2nd column the times of each sequential search.
Select the two columns.  Choose Scatter Plot.
Plot it!
Submit a screenshot of your spreadsheet and plot as part of your submission.
"""
print("----part 4 -----")
for n in range(50000, 1000000, 50000):
    my_list = []

    for x in range(n):
        random_number = random.randint(2, 2 * n)
        my_list.append(random_number)

    start = time.clock()
    sequential_search(my_list, -1)
    end = time.clock()

    print(n, "\t", (end - start))


"""
Part 5: comparing sequential search with binary search
Below are two more versions of binary searches: a iterative solution and a recursive solution.
Use the same range of n to do a comparison of your sequential search and the two versions of binary searches.
This time, build another spreadsheet with 4 columns:
Make the first column 50000, 100000, 150000...
Make the 2nd column the times of each sequential search.
Make the 3rd column the times of each binary search (recursive version).
Make the 4th column the times of each binary search (iterative version).
Make an scatter plot with all 4 columns.
Make another scatter plot without the sequential search (only keep the n, the times of both versions of binary searches)
Submit another screenshot of your spreadsheet and plot as part of your submission.
"""
################do not touch (begin)#####################
def binarySearchIteratively(aList, element):
    left = 0
    right = len(aList) - 1

    while left <= right:
        mid = (left + right) // 2
        if aList[mid] == element:
            return True
        elif aList[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    return False


def binarySearchRecursively(aList, element):
    return betterFindHelper(aList, element, 0, len(aList) - 1)


def betterFindHelper(aList, element, start, end):
    if start > end:
        return False

    middle = (start + end) // 2

    if aList[middle] == element:

        return True

    elif aList[middle] > element:

        return betterFindHelper(aList, element, start, middle - 1)

    else:

        return betterFindHelper(aList, element, middle + 1, end)
################do not touch (end)#####################
print("----part 5 -----")

for n in range(50000, 1000000, 50000):
    my_list = []

    for x in range(n):
        random_number = random.randint(2, 2 * n)
        my_list.append(random_number)

    start = time.clock()
    sequential_search(my_list, -1)
    end = time.clock()

    start2 = time.clock()
    binarySearchRecursively(my_list, -1)
    end2 = time.clock()

    start3 = time.clock()
    binarySearchIteratively(my_list, -1)
    end3 = time.clock()

    time1 = end - start
    time2 = end2 - start2
    time3 = end3 - start3

    print(n, "\t", time1, "\t", time2, "\t", time3)
