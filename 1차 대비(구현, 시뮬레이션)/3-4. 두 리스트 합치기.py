def q_s (arr):
    if len(arr) <= 1 :
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [i for i in tail if i<=pivot]
    right = [i for i in tail if i>pivot]
    return q_s(left) + [pivot] + q_s(right)

n1 = int(input())
arr1= list(map(int,input().split()))
n2 = int(input())
arr2= list(map(int,input().split()))

new_arr = q_s(arr1+arr2)
for i in new_arr:
    print(i, end=' ')
