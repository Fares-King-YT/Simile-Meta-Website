import time

print("Hello User, what would you like to order\n")
time.sleep(0.5)

print("menu items are as follows: hamburgers cost $3.99 each, fries cost $1.99 per order, and drinks cost $0.99 each.\n")

burg = int(input("How many Burgers would you like? \n"))
fry = int(input("How many fries do you want? \n"))
dr = int(input("How many drinks do you want?\n"))

print(f"Ok so {burg} burgers and {fry} fries and {dr} drinks!")

# By Fares Afify 9D
subtotal = (burg * 3.99) + (fry * 1.99) + (dr * 0.99)
print(f"Your total without VAT is ${subtotal:.2f}")

# This is VAT and final amount calculation with f to format 2 decimal so its simple nd cleaner
vat_rate = 0.07
vat_amount = subtotal * vat_rate
total = subtotal + vat_amount

print(f"Including VAT your final total is ${total:.2f}")
