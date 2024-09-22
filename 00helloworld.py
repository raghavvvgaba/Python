# print("Hello World")

# age = 23
# if(age>18):
#     print("You can vote")
# else:
#     print("You can't vote")

# a = list(range(1,20,2)) #first is inclusive, second is exclusive, third is interval
# print(a)

# for x in range(10):
#     print(x, end=" ")

# print()
# def findpos(l,v):
#     pos=-1
#     i=0
#     for x in l:
#         if(x==v):
#             pos = i
#             break
#         i = i+1
#     return pos
# print(findpos(a,15))


# hundreds = {}
# # hundreds["Tendulkar, international"] = 100
# # hundreds["Tendulkar"] = {"international":100}
# # hundreds[("Tendulkar","international")] = 100
# hundreds[["Tendulkar","international"]] = 100
# print(hundreds)

def property(n):
    c = 0
    for i in range(2,n+1):
        if(n%i==0):
            c +=1
    if(c==2):
        return True
    else:
        return False
print(property(31))

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f


l = list(range(1,300,3))
print(l)
print("Next is sublist")
sublist = []
for x in l:
    if property(x):
        sublist.append(x)
print(sublist)


# print(list(map(factorial, l)))