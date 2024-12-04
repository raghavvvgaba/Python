#Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. 

# Generator objects are used either by calling the next method of the generator object or using the generator object in a “for in” loop


def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10) :
    print(num)