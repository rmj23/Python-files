##### Ruben Morales Jr
##### Lab 2
##### a program that will convert pints of milk to quarts, gallon, and pints.


### asks for the amount of pints and converts to int
pintsOfMilk = int(input("How many pints of milk do you have? "))

### finding the amount of pints to a gallon
gallons = pintsOfMilk // 8

### get the remaninding amount of pints
remaindingPintsOfMilk = pintsOfMilk % 8

### finding the amount of pints to a quart
quarts = remaindingPintsOfMilk // 2

### get the remanding amount of pints
remaindingPintsOfMilk = remaindingPintsOfMilk % 2

### finding the amount of pints to a pint
pints = remaindingPintsOfMilk // 1

### print the amount of pints to galoons, quarts, and pints
print(pintsOfMilk, "=", gallons, "gallon(s),", quarts, "quart(s), and", pints, "pint(s).")

### if amount of pints is less than 50, the print "Thats not much milk!"
### if amount of pints is greater than 50, then print "Thats a lot of milk!"
if pintsOfMilk < 50:
    print("That's not much milk!")
else:
    print("That's a lot of milk!")

gallonsPercent = (100 * (8 * gallons)) / 77
print(format(gallonsPercent, ".3f"), "% of the pints became gallons,")

quartsPercent = (100 * (2 * quarts)) / 77
print(format(quartsPercent, ".3f"), "% of the pints became quarts, and")

pintsPercent = (100 * (1 * pints)) / 77
print(format(pintsPercent, ".3f"), "% stayed as pints.")


