# Day 8 Exercise (will be counted as Programing Assignment 4)

"""
Download the Queue class. (10 minutes)
1.      Let's make sure we can use the Queue class
2.      Create a queue
3.      Enqueue some items: "hello", 231, "hard?", True
4.      Print the queue
5.      Dequeue 2 items
6.      Print the queue: we want to see the items in the queue, what is a "clean" way to do this? =)
"""
from Queue import *

queue = Queue()

queue.enqueue("hello")
queue.enqueue(231)
queue.enqueue("hard?")
queue.enqueue(True)

str_var = ""
for x in queue.items:
    str_var += str(x) + "--"
print("head--" + str_var + "end")

queue.dequeue()
queue.dequeue()

str_var = ""
for x in queue.items:
    str_var += str(x) + "--"
print("head--" + str_var + "end")

### Sample output (it is okay to format the output differently, but your output should display the items in the queue)
#head--True--hard?--231--hello-end
#head--True--hard?-end
