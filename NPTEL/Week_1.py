def factors(n):
    flist=[]
    for i in range(1,n+1):
        if(n%i==0):
            flist.append(i)
    return flist

print(factors(100))