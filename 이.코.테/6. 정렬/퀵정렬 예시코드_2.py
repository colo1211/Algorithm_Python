# 파이썬 리스트 컴프리헨션을 활용한 퀵정렬

arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort_2(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    return quick_sort_2(left)+[pivot]+quick_sort_2(right)

print(quick_sort_2(arr))
