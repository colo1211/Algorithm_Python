def binary_search(arr, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target: # left
        return binary_search(arr,target, start, mid-1)
    else : # right
        return binary_search(arr,target, mid+1, end)


n = int(input())
arr_n = list(map(int,input().split()))
arr_n.sort()
m = int(input())
arr_target= list(map(int,input().split()))

for i in arr_target:
    result = binary_search(arr_n, i, 0, n-1)
    if result!=None:
        print('YES', end=' ')
    else:
        print('No',end=' ')