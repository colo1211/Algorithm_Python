n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(y,x):
    if y < 0 or y >= n or x < 0 or x >= m: # 예외처리
        return False
    if graph[y][x] == 0 :
        graph[y][x]=1 # 방문 하자마자 처리하기
        dfs(y-1,x) #상
        dfs(y,x-1) #좌
        dfs(y+1,x) #하
        dfs(y,x+1) #우
        return True
    else :
        return False # 1인 곳은 방문과 동시에 return

count =0
for y in range(n):
    for x in range(m):
        if dfs(y,x) == True:
            count += 1

print(count,graph)