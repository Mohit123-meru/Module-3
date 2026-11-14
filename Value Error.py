try:
    number = int(input("Enter any number : "))
    print ("Your number is : ", number)
except ValueError as error:
    print ("Your exception is : ",error )

