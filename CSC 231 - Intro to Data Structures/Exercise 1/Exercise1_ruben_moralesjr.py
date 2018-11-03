# Day 1 Exercise

def do_math():
    """
    Create code within this function definition to do calculations below:
    What is 2 + 2?
    What is 10 / 3?
    What if I want integer division of 10 / 3?
    How do I compute 2 powers 10? (should be 1024)
    Write code to show your answers of those questions.
    There is no return value for this function.
    """
    mathAnswer = 2 + 2
    print(mathAnswer)

    mathAnswer2 = 10 / 3
    print(mathAnswer2)

    mathAnswer3 = 10 // 3
    print(mathAnswer3)

    mathAnswer4 = 2 ** 10
    print(mathAnswer4)


def do_strings():
    """
    Create my_string variable with value "casablanca"
    There is no return value for this function.
    Find the length of the string
    What is the 4th character?
    Print the substring of length 3 that starts at index 1.
    Is “cat” inside of your string?
    Does your string start with “a”?
    Write code to show your answers of those questions.
    There is no return value for this function.
    """

    my_string = "casablanca"
    print(len(my_string))
    print(my_string[3])
    print(my_string[1:4])
    print("cat" in my_string)
    print(my_string.startswith("a"))


def more_about_yourself():
    """
    Use print statements to tell your instructor more about yourself:
    When did you take CSC131?
    Based on your experience in CSC131 (or other intro-level programing courses), what helped you the most in
    learning programing?
    How do you plan to back up your programs for this course?
    """
    print("I took CSC 131 over the summer")
    print("Last year when i took MIS classes and learned SQL, Visual Basic, HTML, and CSS. Over time programming "
          "languages have been really easy for me to learn")
    print("Using a flash drive and also using the timmy drive")

#######################################
# callers, do not change the code below
#######################################
do_math()
print("--"*10)
do_strings()
print("--"*10)
more_about_yourself()
print("--"*10)

