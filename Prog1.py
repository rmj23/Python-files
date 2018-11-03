#### Program 1
#### Ruben Morales Jr
#### Cash register that tell you the change to hand out
##### Asks the user for the price of an item- assume floating point.

priceOfItem = float(input("Price of Item? "))


##### Applies a 7.25% tax to the price.
##### Use the “round” function, i.e. result =round(amount * tax_rate,2)

taxAmount = (priceOfItem * .0725)
totalCost= priceOfItem + taxAmount


##### Displays the amount owed.

print("The price of the item is $",format(priceOfItem,"5.2f"))
print("The tax on the item is ",format(taxAmount,"8.2f"))
print("The total cost is ",format(totalCost,"13.2f"))


##### Asks the user for the amount submitted in payment- assume floating point.

tendered = float(input("How much are you paying? "))
print("You tendered ",format(tendered,"18.2f"))


##### Calculates the total amount of change the user should get.

change = tendered - totalCost
print("Your change is ",format(change,"16.2f"))


##### Calculates how many dollar bills, quarters, dimes, nickels, and pennies the user should get.

print(" Your change is:")

changeInPennies = int(round((change * 100), 0))

#calculations for dollar bills
countOfDollarBills = changeInPennies / 100
changeLeft = changeInPennies % 100
roundedCountOfDollarBills = round(countOfDollarBills - (changeLeft * .01), 1)
numberOfDollarBills = int(roundedCountOfDollarBills)
print("\t",numberOfDollarBills,"dollar bills,")

#calculations for quarters
countOfQuarters = changeLeft / 25
changeLeft = changeLeft % 25
roundedCountOfQuarters = round(countOfQuarters - (changeLeft * .01), 1)
numberOfQuarters = int(roundedCountOfQuarters)
print("\t",numberOfQuarters,"quarters,")

#calculations for dimes
countOfDimes = changeLeft / 10
changeLeft = changeLeft % 10
roundedCountOfDimes = round(countOfDimes - (changeLeft * .01), 1)
numberOfDimes = int(roundedCountOfDimes)
print("\t",numberOfDimes,"dimes,")

#calculations for nickles
countOfNickles = changeLeft / 5
changeLeft = changeLeft % 5
roundedCountOfNickles = round(countOfNickles - (changeLeft * .01), 1)
numberOfNickles = int(roundedCountOfNickles)
print("\t",numberOfNickles,"nickles, and")

#calculations for pennies
countOfPennies = changeLeft / 1
changeLeft = changeLeft % 1
roundedCountOfPennies = round(countOfPennies - (changeLeft * .01), 1)
numberOfPennies = int(roundedCountOfPennies)
print("\t",numberOfPennies,"pennies.")
