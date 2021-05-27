#방문 한 위치의 요소에 누적 합을 구함으로서 얼마나 걸리는지 최소 거리를 판별하는 문제
from collections import deque
n,m = map(int,input().split())
graph = []

dy = [-1,1,0,0]
dx = [0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))
# 공백 없이 입력 받으려면 .split()을 제외해주면 된다.

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    # print(queue)
    while queue: #큐가 사라질 때 까지,
        y,x = queue.popleft()
        # print(y,x)
        for i in range(len(dy)):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or ny>=n or nx <0 or nx >=m or graph[ny][nx]==0:
                continue
            elif graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x]+1
                queue.append((ny,nx))
    return graph[n-1][m-1]


print(bfs(0,0))
