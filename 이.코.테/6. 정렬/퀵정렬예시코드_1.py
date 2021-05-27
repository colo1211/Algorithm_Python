arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr,start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1 #pivot보다 큰거 찾는 역할
    right = end #pivot보다 작은 거 찾는 역할

    while left<=right: #left가 right보다 작을 때 까지 반복
        while left <= end and arr[left] <= arr[pivot] : #피벗보다 큰거 찾을 때 까지 반복
            left += 1
        while right > start and arr[right] >= arr[pivot]: # 피벗보다 작은거 찾을 때 까지 반복
            right -= 1
        if left > right:
            arr[right], arr[pivot]= arr[pivot], arr[right]
        else :
            arr[left], arr[right]= arr[right],arr[left]
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

quick_sort(arr, 0, len(arr)-1)
print(arr)