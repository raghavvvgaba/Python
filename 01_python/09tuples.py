#tuple is an immutable data type, it cannot changed
a = (1,2,3,5,6,6)
print(type(a))

b = (1,) #creating a single tuple
c = (1) #cannot be created like this cause python recognise this as int

d = ("Raghav", "Harry", 12, 3.12, False)
print(d)

#-----------TUPLE METHODS---------------
print(a.count(6)) #counts the occurence of an element

print(a.index(5)) #gives the index of the element in the tuple

print(len(a)) #gives length of tuple

a1, a2, a3, a4, a5, a6 = a #unpacks tuple into individual variables
print(a1, a2, a3, a4, a5, a6) 