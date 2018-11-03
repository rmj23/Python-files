# Day 5 Exercise

"""
Part 1: Defining a Student class
Rename this file to "Student.py" first.
Let's assume we need to store the student’s first name, last name and gpa.
Add a constructor that has three instance variables:
    - firstName
    - lastName
    - gpa
Create the __str__ method to print a student's information as:
<last name><SPACE><first name><SPACE><gpa>
"""
class Student:
    def __init__(self, first, last, gpa):
        self.firstName = first
        self.lastName = last
        self.gpa = gpa

    def __str__(self):
        return self.lastName + " " + self.firstName + " " + str(self.gpa)