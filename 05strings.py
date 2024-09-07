#strings can be written in three ways
a= 'Raghav'
b= "Raghav"
c= '''Raghav'''

#strings are immutable, means you can't change once an existing string is made

#---------to slice a string----------
name = "Raghav"
nameshort = name[0:2] #starts from 0 to 2 (excluding 2)
print(nameshort)
print(name[1]) #prints a single character at 1
print(name[1:]) #prints from 1 till end
print(name[:5]) #prints from start till 5

#you can use negative indexing as well
print(name[-5:-1]) #-5 to -1 (excluding -1)

#convert negative to positive for corresponding positive values
print(name[1:5])

#-------slicing with skip value
word = "0123456789"
print(word[1:6:2]) #starts from 1, goes till 6(excluding it) and jumps two values between it, prints 135
print(word[1:6:1]) # jumps one value, means nothing new, prints 12345