total = 0
coin = 0
badam_milk = 15

while True:
    coin = int ( input ("Enter the coins - either a 1 rupee, 2 rupee, 5 rupee, or 10 rupee."))
    if coin != 1 and coin != 2 and coin != 5 and coin != 10:
        print ("Invalid coin. Please try again.")
        continue
    total += coin
    coin += 1
    if total >= badam_milk:
        print ("Enough money is entered.")
        break

def change (total,badam_milk):
    changes = total - badam_milk 
    return changes

sum = change (total,badam_milk)

if sum == 0:
    pass
else:
    print ("Your change is :", sum , "rupees")