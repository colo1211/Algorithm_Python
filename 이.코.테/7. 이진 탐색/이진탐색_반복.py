def binary_search(arr, target, start, end):
    while start<=end: #while 문 Tip : 종료 조건의 대우 명제를 작성하면 쉽게 작성 가능 (start>end면 종료 -> start<=end)
        mid = (start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target: #left 영역
            end = mid-1
        else :  #right 영역
            start =mid+1
    return None



n, target = map(int,input().split())
arr = list(map(int,input().split()))

result = binary_search(arr, target, 0, n-1)
print(result+1)