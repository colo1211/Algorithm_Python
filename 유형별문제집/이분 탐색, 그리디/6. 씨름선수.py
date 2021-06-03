# 키를 중심으로 내림차순 정렬
# 몸무게 max값 갱신 할 때 마다 count += 1
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(reverse=True, key=lambda x:x[0])
max_height = 0
count = 0
for height , weight in arr:
    if weight>max_height:
        count +=1
        max_height=weight
print(count)