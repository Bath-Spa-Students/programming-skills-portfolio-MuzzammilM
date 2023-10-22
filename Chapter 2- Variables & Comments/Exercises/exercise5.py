#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.
# Define the price of a USB stick and the girl's budget

amount = 50
priceUSB = 6
boughtUSB = (amount / priceUSB)
print("The girl can buy",int(boughtUSB),"of USBs from £",amount)
change = amount - (priceUSB*int(boughtUSB))
print(f"The change is: £",change)