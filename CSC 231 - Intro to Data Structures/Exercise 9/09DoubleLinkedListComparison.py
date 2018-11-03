# Day 9 Exercise

"""
Show that implementing a Queue using a list is not as efficient as implementing a Queue using a (double) linked list.
How?   Take an implementation of a Queue done with a list (QueueWithList.py).
Time how long it takes to enqueue n items and then dequeue n items.
Take an implementation of a Queue done with a linked list (QueueWithLinkedList.py).
Time how long it takes to enqueue n items and then dequeue n items.
Print out the value of n and the two times.
Put this code in a for  loop that varies n from 10000 to 100000
( you can decide the step size to balance the running time and information you want to present)
Produce a graph.

At the end of this program, make a print statement to explain what you have found from your graph

Submit your program and the graph you have made.


"""
import time
from QueueWithList import *
from QueueWithLinkedList import *

list = QueueWithList()
linkedList = QueueWithLinkedList()

for n in range(10000, 100000, 5000):

    start = time.clock()
    for i in range(n):
        list.enqueue(i)
    for i in range(n):
        list.dequeue()
    end = time.clock()

    start2 = time.clock()
    for x in range(n):
        linkedList.enqueue(x)
    for x in range(n):
        linkedList.dequeue()
    end2 = time.clock()

    print(n, end-start, end2-start2)

print("Explain what you have found from your graph")
print("You can use multiple lines of output if you want to")
print("---"*20)
print("The list compared to the linked list makes it seem that the list takes a lot more time to do these functions.")
print("At the beginning of the iteration both list take about the same time to do these functions.")
print("But as the iteration becomes more complex it takes it more time for the list to processes these function unlike")
print("the linked list.")