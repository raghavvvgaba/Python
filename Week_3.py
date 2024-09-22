# # 1.
# def contracting(arr):
#     c = 0
#     diff = abs(arr[1]-arr[0])
#     for i in range(2,len(arr)):
#         if(abs(arr[i]-arr[i-1])>=diff):
#             c = c+1
#         diff = abs(arr[i]-arr[i-1])
#     if(c>0):
#         return False
#     else:
#         return True
    
# print(contracting([9,2,7,3,1]))
# print(contracting([-2,3,7,2,-1]))
# print(contracting([10,7,4,1]))

# # 2. Hills and valleys
# def counthv(arr):
#     hc,vc = 0,0
#     for i in range(1,len(arr)-1):
#         if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
#             hc = hc + 1
#         elif(arr[i]<arr[i-1] and arr[i]<arr[i+1]):
#             vc = vc + 1
#     list = []
#     list.append(hc)
#     list.append(vc)
#     return list

# print(counthv([1,2,1,2,3,2,1]))
# print(counthv([1,2,3,1]))
# print(counthv([3,1,2,3]))

#3. Rotate an array
def rotate(arr):
    arr2 = [[None]*len(arr)*len(arr)]
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            print(str(arr[i][j]) + " ", end = "")
            arr2[j][i] = arr[i][j]
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))


# hours = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(hours[0]))
# print(hours[1][2])