#Insertion sort builds a sorted portion of the list by repeatedly picking the next unsorted element and inserting it into the correct position within the already sorted section.

def insertion(arr):
    for i in range(1,len(arr)):
        pos = i
        while(arr[pos-1]>arr[pos] and pos>0):
            (arr[pos-1],arr[pos]) = (arr[pos],arr[pos-1])
            pos = pos - 1
    return arr

list = [23,12,102,97,1,45]

print(insertion(list))