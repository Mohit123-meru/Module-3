def greet ():
    print ("Welcome to Mohit's Lemonade stand.")
    print ("Fresh Lemonade is made for you.")
greet ()
cup_price = float(input("What is the price for 1 cup?"))
cups_sold = int(input("How many cups do you want?"))
def total (cup_price, cups_sold):
    Total = (cup_price * cups_sold)
    return Total
price = total (cup_price, cups_sold)
prices = round (price, 2) 
amount = float(input("Give the amount."))
def change (amount, price):
    change = (amount - price)
    return change
changes = change (amount, price)
changes = round (changes, 2) 
print ("====Lemonade Stand====")
print (cup_price)
print (cups_sold)
print (price)
print (prices)
print (changes)

