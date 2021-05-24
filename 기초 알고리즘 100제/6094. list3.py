# # 방법 1. sort 함수 사용
# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()
# print(arr[0])

# # 방법 2. 최소값 찾기
n = int(input())
arr = list(map(int,input().split()))
min=10000
for i in range(n):
    if arr[i]<min:
        min=arr[i]

print (min)