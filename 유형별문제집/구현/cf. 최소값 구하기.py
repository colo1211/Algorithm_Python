# 최소값 구하기

arr = [5,3,7,9,2,5,2,6]

min = arr[0]
# min = int(1e9)
# min = float('inf') #파이썬에서의 무한대 값
for i in range(1,len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)