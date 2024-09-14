friends = ["Apple", "Akash", 5 , 34.06, False]
print(friends)
print(friends[0])

#lists can be changed, unline strings (which are immutable)
#lists methods make changes in the lists itself, unlike strings where a new string is created when using string methods
friends[0] = "Grapes"
print(friends)

print(friends[1:6]) 

#list methods
friends.append("Harry") #makes insertion at end of the list
print(friends)


a = [5,3,2,9,0]
a.sort() #sort all integer numbers
print(a)

a.reverse()  #reverse all elements
print(a)

friends.insert(3, "Raghav") #insert elements at specific index.. syntax:- (index no, element to be inserted)
print(friends)

friends.pop() #removes the element at last and return it
print(friends)

friends.pop(1) #if you give it a index it pops out that element
print(friends.pop(0)) 
print(friends)

a.remove(0)
print(a)
