try:
    n1 = int(input("Enter a number of your choice : "))
    n2 = int(input("Enter another number of your choice : "))
    quotient = n1 / n2
    
except ZeroDivisionError:
    print ("Zero is invalid. Enter a different number.")
except ValueError:
    print ("Print a valid number.")
except:
    print ("Your input is invalid.")
else:
    print (quotient)
finally:
    print ("Bye.")