#Ruben Morales Jr
#Lemonade and cookie stand business
# ...

#ask about the price and item of item 1
item1 = input("What is the item being purchased?: ")
priceOfItem1 = float(input("What is the price of the item?: "))

#ask about the price and item of item 2
item2 = input("What is the item being purchased?: ")
priceOfItem2 = float(input("What is the price of the item?: "))


#calculations to find tax rate, add the rate to total of items, and print the amount owed with tax
totalPriceOfItems = priceOfItem1 + priceOfItem2
taxRate = totalPriceOfItems * .07
totalPrice = taxRate + totalPriceOfItems
print("The customer owes you ",format(totalPrice, ".2f"))


#ask for amount given
amountGiven = float(input("How much money did the customer give you?: "))


#print the cost of each item
print(item1,"costs $",format(priceOfItem1, ".2f"))
print(item2,"costs $",format(priceOfItem2, ".2f"))

#print subtotal, tax rate, amount due, and amount given
print("The subtotal is $",format(totalPriceOfItems))
print("The tax is $",format(taxRate, ".2f"))
print("The amount due is $",format(totalPrice, ".2f"))
print("You gave me $",format(amountGiven, ".2f"))


#calculate change
change = amountGiven - totalPrice
print("The amount of change is $",format(change, ".2f"))


#calculate average and print
average = totalPriceOfItems / 2
print("The average price was $",format(average, ".2f"))


#calculate circumference
diameter = int(input("What was the diameter of the cookie? "))
circum = 3.14 * diameter


#calculate area and print
radius = diameter / 2
area = 3.14 * (radius ** 2)
print("The circumference of the cookie was",circum,"and the area was",area)
