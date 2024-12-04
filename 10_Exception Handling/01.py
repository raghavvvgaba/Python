try:
    a = int(input("Enter a number"))
    print("Number is ", a)
except ValueError:
    print("Entered value is not a number")