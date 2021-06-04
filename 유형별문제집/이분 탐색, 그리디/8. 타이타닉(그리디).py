# Tip!
# pop(),pop(0) 사용하기 위해서는 while arr: 과 같은 리스트가 빌때까지 반복문을 수행하는 문법을 작성
n, m = map(int,input().split())
arr= list(map(int,input().split()))

def q_s (arr):
    if len(arr)==0:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    return q_s(left)+[pivot]+q_s(right)

arr = q_s(arr)
# print(arr)
count = 0
while len(arr)>1: # 조건을 만족하는 max를 찾기 위해
    if arr[0]+arr[-1] > m: # 넘어가면 무거운 사람 먼저 탈출
        # print('혼자 빠져 나감',arr[-1])
        arr.pop()
        count +=1
    else:
        # print('여기보세여',arr)
        # print('같이 빠져 나감',arr[0],arr[-1])
        arr.pop()
        arr.pop(0)
        count +=1
# print(arr)
for i in range(len(arr)):
    count+=1
print(count)
