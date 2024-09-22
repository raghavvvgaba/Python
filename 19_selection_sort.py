#Selection sort repeatedly selects the smallest (or largest) element from the unsorted part of the list and swaps it with the first unsorted element, moving the boundary of the sorted portion one element at a time.

def selection(l):
    for i in range(0,len(l)):
        minpos = i
        for j in range(minpos,len(l)):
            if(l[j] < l[minpos]):
                # temp = l[i]
                # l[i] = l[j]
                # l[j] = temp
                (l[i],l[j]) = (l[j],l[i]) #python tuple swapping feature
    return l

list = [23,1,100,57,24,90]
print(selection(list))