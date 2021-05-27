arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        while left<=end and arr[left]<=arr[pivot] :#큰거 나올때 까지 탐색
            left += 1
        while right>start and arr[right] >= arr[pivot] : # 작은거 나올때 까지 탐색
            right -= 1
        if left>right: #엇갈렸다면? pivot과 right(작은 수) 를 스왑
            arr[pivot], arr[right]= arr[right], arr[pivot]
        else : #엇갈리지 않았다면? left와 right를 스왑
            arr[left], arr[right]= arr[right], arr[left]

    quick_sort(arr,0, right)
    quick_sort(arr,right+1, end)

quick_sort(arr,0,len(arr)-1)
print(arr)