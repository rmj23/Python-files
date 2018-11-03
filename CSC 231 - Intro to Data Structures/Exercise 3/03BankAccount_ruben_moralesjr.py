# Day 3 Exercise
class BankAccount:
    '''
    Stores information about a bank account including the first and last name of the account holder,
    and the account balance.
    '''

    def __init__(self, first, last, bal):

        #The constructor for a bank account.
        #:param first: The customer's first name.
        self.first_name = first

        #:param last: The customer's last name.
        self.last_name = last

        #:param bal: The balance of the account.
        self.balance = bal
        #:return: Nothing



    def deposit(self, amt):

        #Adds an amount to the account's balance.
        #:param amt: The amount to add to the account.
        self.balance = self.balance + amt

        #:return: Nothing.



    def withdraw(self, amt):

        #Deducts an amount from the account's balance.
        #:param amt: The amount to deduct.
        self.balance = self.balance - amt

        #:return: Nothing.



    def __str__(self):

        #A pretty string to print for the BankAccount.  Should look like "Jones, Mary    $300"
        #:return: The string for printing.
        return str(self.last_name) + ", " + str(self.first_name) + " $" + str(self.balance)



#####################
#do not change blow:
#####################

account1 = BankAccount("Jane", "Doe", 50)
account2 = BankAccount("Mary", "Smith", 3000)
print(account1)
print(account2)
account1.deposit(75.25)
account2.withdraw(317.18)
print(account1)
print(account2)

###########################
# EXPECTED OUTPUT:
###########################
# Doe, Jane	$50
# Smith, Mary	$3000
# Doe, Jane	$125.25
# Smith, Mary	$2682.82
