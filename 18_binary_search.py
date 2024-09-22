def bsearch(arr,element,start,end):
    if(end-start==0):
        return False
    mid = (start+end)/2
    if(element == arr[mid]):
        return True
    if(element<arr[mid]):
        bsearch(arr,element,start,mid)
    else:
        bsearch(arr,element,mid+1,end)