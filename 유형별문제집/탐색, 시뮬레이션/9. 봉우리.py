n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

# 배열 가장자리에 0을 삽입하는 방법
arr.insert(0,[0]*n)
arr.append([0]*n)
for i in arr:
    i.insert(0,0)
    i.append(0)

dx = [-1,1,0,0]
dy = [0,0,1,-1]
count =0

for y in range(1,n+1):
    for x in range(1,n+1):
        if all(arr[y][x] > arr[y+dy[k]][x+dx[k]] for k in range(4)):
            count+=1
print(count)