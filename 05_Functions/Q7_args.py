# function with *args
#Write a function that takes variable number of arguments and returns their sum

def sum_all(*args):     # the symbol * takes in multiple arguments
    return sum(args)
print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5, 6))

#args returns a tuple, so it can be manipulated our own way as well

def multiply_by_7(*args):
    print(args)
    for i in args:
        print(i * 7)
    return
multiply_by_7(1, 2, 3, 4, 5)