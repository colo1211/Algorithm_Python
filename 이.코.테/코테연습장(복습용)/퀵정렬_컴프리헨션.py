arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_arr = [x for x in tail if x<=pivot]
    right_arr = [x for x in tail if x>pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr) #재귀 호출


print(quick_sort(arr))