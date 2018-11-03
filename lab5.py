#lab 5
#Ruben Morales Jr
#Employee calculator that calculates over-time pay and regular pay for an or many employees

def print_it(regular, overtime, total, name, hoursWorked):
    print(name, "worked hours", hoursWorked, "and should get paid:")
    print("\t$", format(regular, "9.2f"), "in regular pay")
    print("\t$", format(overtime, "9.2f"), "in over-time pay")
    print("\t$", format(total, "9.2f"), "on total pay")
    
def calc_pay(name, hoursWorked, rate):
    if hoursWorked <= 40:
        regularPay = rate * hoursWorked
        overtimePay = 0
        totalPay = regularPay + overtimePay
    else:
        overtimeHours = hoursWorked - 40
        regularPay = rate * 40
        overtimePay = (rate * 1.5) * overtimeHours
        totalPay = regularPay + overtimePay
    print_it(regularPay, overtimePay, totalPay, name, hoursWorked)
    
def main():
    name = input("Employee's Name: ")
    hoursWorked = int(input("Number of Hours Worked (between 10 and 50): "))
    while hoursWorked < 10 or hoursWorked >50:
        hoursWorked = int(input("Hours can not be greater than 50 or less than 10. Try again: "))
    rate = float(input("Rate/Hour? "))
    calc_pay(name, hoursWorked, rate)

main()
answer = input("Enter another employee? (yes to continue/no to quit): ")
while answer == "yes":
    main()
    answer = input("Enter another employee? (yes to continue or no to quit): ")
