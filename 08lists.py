friends = ["Apple", "Akash", 5 , 34.06, False]
print(friends)
print(friends[0])

#lists can be changed, unline strings (which are immutable)
#lists methods make changes in the lists itself, unlike strings where a new string is created when using string methods
friends[0] = "Grapes"
print(friends)

print(friends[1:6]) 

#--------------------list methods--------------------
friends.append("Harry") #makes insertion at end of the same list. It does not create a new list
print(friends)


list1 = [1,3,5,6]
list2 = list1
list1[2] = 7   #this changes both the list as they both are pointing to the same address
print(list1)
print(list2)  

list1 = list1[0:2] + [2] + list1[3:] #now this creates a new list admd therefore only changes list1 and not list2
print(list1)   
print(list2)  

#concatenation produces a new list whereas append is a function that extends a list with a new value without changing it

list1.extend(list2) #this method works like append and extends the list by itself



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

a.remove(0) #removi
print(a)
