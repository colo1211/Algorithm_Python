arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]: #이전 요소보다 작다면 swap
            arr[j], arr[j-1]=arr[j-1],arr[j]
        else : #크다면 swap 안함
            break
print(arr)