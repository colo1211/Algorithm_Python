# 그리디 90% : 정렬로 해결
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key =lambda x:(x[1],x[0]))
# print(arr)
end_time = 0
count = 0
for start, end in arr:
    if start >= end_time:
        end_time = end
        count += 1
print(count)