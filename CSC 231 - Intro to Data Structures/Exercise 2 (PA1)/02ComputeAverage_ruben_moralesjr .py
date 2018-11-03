# Day 2 Exercise (will be counted as Programing Assignment 1)

"""
Read in a file (called “numbers.txt”) of integers.  There will be one integer per line.
Print the number of integers read in.
Print the average of the integers.  Do not use the built-in sum operator on lists.
Find and print the minimum.   Do not assume that the minimum must be less than some fixed integer.  Do not use the built-in min operator on lists.
Find and print the maximum.  Do not assume the maximum must be greater than some fixed integer.  Do not use the built-in max operator on lists.
Print the median of the numbers.  Do not use that statistics package’s median method. This will require you to sort.
If you read the integers into a Python list, you may use the built-in list sorted or sort method.
Then take the one in the middle.  That’s the median.  But what if there is an even number of values?
What’s the “middle” element?  In that case, take the two nearest the middle and average them.

Here are two examples of computing the median.
2 1 10 3 5        To compute the median, sort:   1 2 3 5 10.  Take the one in the middle.
In this case that’s the value 3.    What is its index?   The length of the list divided by 2.

7 12 23 11     To compute the median, sort: 11 12 17 23.
Since there are an even number of elements, average the two in the middle: (12 + 17)/2 = 14.5.
What are the indices of these two elements?  The length of the list divided by 2, and (length of the list divided by 2) minus 1.

Helpful hint #1: How can Python compute whether a number is even or odd?
Take the number and perform modulo 2 (number % 2).  If the answer is 0, it’s even.  If the answer is 1, it’s odd.

Helpful hint #2: Since the index must be an integer, you have a problem if you take an odd number and divide it by 2 to compute an index.
So, how do make sure you end up with an integer?  Use integer division!  That’s the // operator in Python.
"""
# OPEN FILE AS READ #
numbers_file = open("numbers.txt", "r")

# MAKE A LIST #
number_list = []

print("Beginning of reading file.....")
for line in numbers_file:
    line.strip()
    number = int(line)
    print(number)

    # ADD NUMBERS TO LIST #
    number_list.append(number)

print(".....End of reading file")

# AVERAGE #
list_length = len(number_list)
total = 0

for list_item in number_list:

    total = total + list_item

average = total/list_length
print("The avg is", average)


# MINIMUM #
minimum = number_list[0]

for list_item in number_list:

    if list_item < minimum:
        minimum = list_item

print("The min is", minimum)


# MAXIMUM #
maximum = number_list[0]

for list_item in number_list:

    if list_item > maximum:
        maximum = list_item

print("The max is", maximum)


# MEDIAN #

# IF LIST LENGTH/COUNT IS ODD #
if list_length % 2 == 0:

    number_list.sort()

    # GET FIRST NUMBER TO DIVIDE #
    firstNumber = (list_length // 2) - 1
    print(number_list[firstNumber])

    # GET SECOND NUMBER TO DIVIDE #
    secondNumber = list_length // 2
    print(number_list[secondNumber])

    # SUM AND DIVIDE TO FIND MEDIAN #
    median = (number_list[firstNumber] + number_list[secondNumber]) // 2
    print("The median is", median)

# IF LIST LENGTH/COUNT IS EVEN #
elif list_length % 2 == 1:

    number_list.sort()

    print("The median is", number_list[list_length//2])
