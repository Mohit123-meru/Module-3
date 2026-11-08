def fact (f):
    ''' this is a function to find a factorial of a number '''
    if f == 0 or f == 1:
        return 1
    else:
        return f * fact (f-1)
    fact (f) 
fc = fact (int (input ("Give a number to find its factorial")))
print (fact.__doc__)
print (fc)