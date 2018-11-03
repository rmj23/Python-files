# Day 8 Exercise (will be counted as Programing Assignment 4)
"""
1.      Download and include the Deque class in your project
2.      Read in a string from the user
3.      Define and call a method is_palindrome that returns True if s is a palindrome and False otherwise;
4.      Don't worry about spaces or punctuation yet.
5.      How to do it:
    a.      For every character in the string, add to the end of the deque.
    b.      While the length of the deck is greater than 1,
        i.      Remove the front; remove the end; compare.  If equal, keep going
        ii.      Otherwise return False.
    c.       Return True.
"""

from Deque import *

deque = Deque()

string = str(input("type in a string:"))

def is_palindrome(str):

    for x in str:
        deque.addRear(x)

    while deque.size() > 1:
        deque.removeFront()
        deque.removeRear()
        if deque.removeFront() == deque.removeRear():
            continue
        else:
            return False
    return True


print(is_palindrome(string))