# def firstNonRepeating(arr, n):
#     for i in range(n): 
#         j = 0
#         while(j < n): 
#             if (i != j and arr[i] == arr[j]): 
#                 break
#             j += 1
#         if (j == n): 
#             return arr[i] 

#     return None
	 
arr = [ 1,1,2,2,3,3,4,4,5 ] 
# n = len(arr) 
# print(firstNonRepeating(arr, n))


for i in range(len(arr)-1):
    if i+2 <= (len(arr)-1):
        # print((arr[i] == arr[i+1]) ,(arr[i] == arr[i+2]) )
        if ((arr[i] == arr[i+1]) or  (arr[i+1] == arr[i+2]) ) :
            # print(arr[i+1])
            pass
        else:
            print(arr[i+1])
        # pass
    # else:
    #     print(arr[i])

# for i in range(len(arr)):
