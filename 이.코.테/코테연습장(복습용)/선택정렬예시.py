arr=[7,5,9,0,3,1,6,2,4,8]

for i in range(0,len(arr)):
    min_index= i
    for j in range(i, len(arr)):
        if arr[min_index] > arr[j]:
            min_index=j
    arr[i] , arr[min_index]= arr[min_index], arr[i]
print(arr)
