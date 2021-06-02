n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

# 배열 테두리에 0을 삽입하는 방법
arr.insert(0,[0]*n) #위쪽 삽입
arr.append([0]*n) # 아래쪽 삽입
for i in arr:
    i.insert(0,0) # 왼쪽 삽입
    i.append(0) # 오른쪽 삽입
# print(arr)

dx = [-1,1,0,0]
dy = [0,0,1,-1]
count =0

for y in range(1,n+1):
    for x in range(1,n+1):
        for t in range(len(dy)):
            ny = y+dy[t]
            nx = x+dx[t]
            if arr[ny][nx] >= arr[y][x]: #큰게 하나라도 있다면(봉우리X), Count
                count += 1
                break
print(n**2-count)

# ver 2. 내장 함수 all 활용
# for y in range(1,n+1):
#     for x in range(1,n+1):
#         if all(arr[y][x] > arr[y+dy[k]][x+dx[k]] for k in range(4)): #4개가 모두 arr[y][x]가 크면 봉우리 count
#             count+=1