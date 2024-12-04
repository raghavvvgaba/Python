# def intreverse(s):
#     sum = 0
#     while(s!=0):
#         r = int(s%10)
#         sum = (sum*10)+r
#         s = int(s/10)
#     return sum

# print(intreverse(387))




# def matched(s):
#     for  i in range(0,len(s)+1):
#         if(s.find('"("') and s.find('")"')):
#             return True
#         else:
#             return False
        
# print(matched("(7)(a"))





# def isPrime(n):
#     c=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             c = c+1
#     if(c==2):
#         return True
#     else:
#         return False
# def sumprimes(l):
#     sum = 0
#     for i in range(0,len(l)):
#         n=l[i]
#         if(isPrime(l[i])):
#             sum += n
#     return sum
# print(sumprimes([3,3,1,13]))
