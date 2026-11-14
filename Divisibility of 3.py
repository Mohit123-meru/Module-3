valid = False
while not valid == True:
    try:
        n = int(input("Enter a number : "))
        while n % 3 == 0:
            print ("Your number is divisible by 3.")
            print ("bye.")
            n = int(input("Enter a second number : "))
        valid = True
    except ValueError :
        print ("Your input is invalid.")