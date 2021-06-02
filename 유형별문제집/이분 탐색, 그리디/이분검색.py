def quicksort(arr):
    if len(arr)==0:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quicksort(left)+[pivot]+quicksort(right)

def binary(arr, target, start, end):
    if start > end:
        return arr
    mid = (start+end)//2
    if arr[mid] == target:
        return mid+1
    elif arr[mid]<target: #오른쪽 탐색
        return binary(arr,target,mid+1, end)
    else :  #왼쪽 탐색
        return binary(arr,target,0,mid-1)


n, m = map(int, input().split())
arr=list(map(int,input().split()))
arr=quicksort(arr)
print(binary(arr,m,0,len(arr)-1))