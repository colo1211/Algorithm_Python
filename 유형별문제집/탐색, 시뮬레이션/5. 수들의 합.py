n, m = map(int, input().split())
arr= list(map(int,input().split()))
count = 0
# 시간 초과 ver
def get_sum(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum

for i in range(len(arr)):
    if arr[i] == m:
        count += 1
    else :
        for j in range(i+1, len(arr)):
            if get_sum(arr[i:j+1]) == m:
                count += 1

print(count)