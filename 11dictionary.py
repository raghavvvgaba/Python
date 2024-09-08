# Dictionary is a collection of key value pairs
# 1. It is unordered
# 2. It is mutable
# 3. It is indexed
# 4. Cannot contain duplicate keys

dict = {
    "Raghav":"Agra",
    "Priyansh":"Bhopal",
     list : [12,34],
    "a":100,
    "b":200,
    int:300,
    0:"Harry"
}
print(dict["Raghav"])
print(dict[list])
print(dict[int])

#-----------Dictionary methods------------
print(dict.items()) #returns all key value pairs in a list, where each key and value is in a tuple

print(dict.keys()) #gives all keys (left side)

print(dict.values()) #gives all values (right side)

dict.update({"Raghav":"Delhi"}) #updates the key value if present, otherwise adds a new key value pair

print(dict.get("Raghav2")) #gets the value 
#if key value is not present, get function returns none
print(dict["Raghav"]) #and this will return an error

print(len(dict)) #gives length of dictionary
