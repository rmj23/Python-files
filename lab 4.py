# Ruben Morales Jr
# Lab 4
# Instructors Grading System

#part 2; set answer to yes to enter while loop
answer = "yes"

#part 2; while loop to do everything in part 1 and ask if there is another student
while answer == "yes":
    
    #part 1; ask how many grades and student name
    totalNumberOfGrades = int(input("How many grades are there? "))
    studentName = input("Student's name: ")

    #part 1; set sumOfGrades to 0
    sumOfGrades = 0

    #part 1; for loop to keep asking for student grade, check for error, and calulate a sum
    for x in range(totalNumberOfGrades):
    
        studentGrade = int(input("Student's grade? "))

        #part 3; error validation to check of grade is above 100 or below 0
        while studentGrade < 0 or studentGrade > 100:
            studentGrade = int(input("Invaild, student grade cannot be less than 0 or more than 100. try again: "))
    
        sumOfGrades += studentGrade

    #part 1; calculate average and print statement for the student
    avg = sumOfGrades / totalNumberOfGrades
    print(studentName+"'s"+" average is ", format(avg, ".2f"))

    #part 2; ask is there is another student to process
    answer = input("Is there another student to process? ")

