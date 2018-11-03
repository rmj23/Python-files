# Day 5 Exercise
from Student import *

"""
Part 2: Create 2 student objects:
Yang Song with GPA 4.0
Garen Crownguard with GPA 2.5
Print out those two student objects.
"""
student1 = Student("Yang", "Song", 4.0)
student2 = Student("Garen", "Crownguard", 2.5)

print(student1)
print(student2)

print("--"*10)
"""
Part 3: Reading in students from a file  

I've created a file roster.txt that contains a list of students in the following format
<last name><SPACE><first name><SPACE><gpa>
In the Roster file, let's open up the roster.txt file and read in each line, then use the information of each line to create a student object.
Hint: to break up each line so that we can get the individual information, we can use split().
Hint: a GPA is supposed to be a float number
Once you've created a Student object, add it to a list of students.
When you've finished reading in the whole file, write another loop to print out each student.

Make a print statement to show the T(N) of your solution to part 3.
Make another print statement to show the Big O of your solution to part 3.
Hint: depending your program design, you may have a different T(n) to the T(n) on the solution. It is okay.
"""
studentFile = open("roster.txt", "r")
student_list = []

for line in studentFile:
    value = line.split()

    first = value[1]
    last = value[0]
    gpa = value[2]

    student = Student(first, last, gpa)
    student_list.append(student)

for a_student in student_list:
    print(a_student)

print("T(n) = 2 + n * 6 + 1 + n = 7n + 3")
print("O(n)")

print("--"*10)
"""
Part 4: Do searches
Take the list of students and print the lowest GPA

Make a print statement to show the T(N) of your solution to part 4.
Make another print statement to show the Big O of your solution to part 4.
Hint: depending your program design, you may have a different T(n) to the T(n) on the solution. It is okay.
"""

student_list.sort(key=lambda x: x.gpa, reverse=False)
print(student_list[0])

print("T(N)")
print("O(n)")