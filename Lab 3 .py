# Ruben Morales Jr
# Lab 3
# XYZ Corp. Determining priority vs normal treatment

#ask and collect customer information
customer = str(input("Name of customer? "))
businessAmount = float(input("Amount of business per year? "))
years = int(input("How long has the customer been with us? "))
paymentHistory = str(input("Good payment history? (yes or no) "))


if businessAmount >= 10000 and (paymentHistory == "yes" or years >= 20):
    #If customer has either good payment history or more than 20 years and business amount
    #is more than $10,000
    
    print(customer, "should get priority treatment")

elif businessAmount < 10000 and years < 20 and paymentHistory == "no":
    #If customer has less than 20 years, payment history is bad, and business amount is
    #less than $10,000

    print("Let's drop", customer)

else:
    #Change treatment to standard for all others
    print(customer, "should get standard treatment")
