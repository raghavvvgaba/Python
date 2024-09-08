# Set is a collection of non-repetitive elements
# Even if you add multiple repeated elements, it will give it only once
# Order is not maintained. If you want order, use list
# Sets are unindexed
# It can take multiple data types


#To create a set
s = {1,5,32}

#To create an empty set
e = set()

#If you use given below, it will create an empty dictonary
d = {}
print(type(d))

#-------------Set methods---------------

s.add(566)  #to add values
print(s)

len(s) #gives length of set

s.remove(1) #removes a given element

s.pop() #removes a random element from set