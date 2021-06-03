# def get_min(arr): # 이미 정렬되어 있으므로 작은거 있으면 바로 break
#     min = arr[0]
#     min_index = 0
#     for i in range(len(arr)):
#         if min>arr[i]:
#             min_index = i
#             break
#     return min
#
# def get_max(arr): # 이미 정렬되어 있으므로 큰거 있으면 바로 break
#     max = arr[-1]
#     min_index= 0
#     for i in range(len(arr)-2,1,-1):
#         if max <arr[i]:
#             max_index = i
#             break
#     return max

l = int(input())
arr = list(map(int,input().split()))
m = int(input())

def q_s(arr):
    if len(arr)==0:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    return q_s(left)+[pivot]+q_s(right)


arr = q_s(arr)
for i in range(m): # 연산 반복 횟수
    arr = q_s(arr)
    arr[0] += 1
    arr[-1] -= 1
arr = q_s(arr)
print(arr[-1]-arr[0])



