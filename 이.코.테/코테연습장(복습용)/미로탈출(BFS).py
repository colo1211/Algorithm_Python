from collections import deque
graph = []
n,m = map(int, input().split())
dy = [-1,1,0,0]
dx = [0,0,1,-1]

# 2차원 배열 입력
for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(y,x):
    queue= deque()
    queue.append((y,x))
    while queue: #큐가 모두 빌 때 까지!
        y,x = queue.popleft()
        for i in range(len(dy)):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m :
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx]==1:
                graph[ny][nx] = graph[y][x]+1
                queue.append((ny,nx))
    return graph[n-1][m-1]

print(bfs(0,0))