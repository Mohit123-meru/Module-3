n = int(input("Give a number: "))
def quadruple(n):
    n = n * n * n * n
    return n
def divide_4 (n):
    if n %4 == 0:
        print ("Your number is divisible by 4.")
        print ("n = ", n)
        return quadruple (n)
    else :
        print ("Your number is not divisible by 4")
        return False
print (divide_4 (n))
print (divide_4 (4))
