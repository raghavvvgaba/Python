a = input("Enter number 1: ")  #12
b = input("Enter number 2: ")  #45
print("number is "+ a)
print("number is "+ b)
print(a+b) #this gives output as 1245
#this is because python takes input as string and on adding it concatenated them

#to take input as integer, you have to typecast it

c = int(input("Enter number 3: ")) #12
d = int(input("Enter number 4: ")) #45
print(c+d)   #output -> 35
