from collections import deque

def BFS(gragh,start, visited):
    queue = deque([start]) #큐 선언과 동시에 초기화
    visited[start]=True
    while queue: # 큐가 빌때 까지
        print(queue)
        v = queue.popleft() #v는 방문 했다는 의미, 동시에 방문한 노드의 연결된 요소를 전부 다 `큐`에 추가한다. (visited[i]가 비어있다면!)
        # print(v, '번 방문 했음!')
        for i in gragh[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i]=True



gragh = [
    [],  # 0번 노드
    [2, 3, 8],  # 1번 노드
    [1, 7],  # 2번 노드
    [1, 4, 5],  # 3번 노드
    [3, 5],  # 4번 노드
    [3, 4],  # 5번 노드
    [7],  # 6번 노드
    [2, 6, 8],  # 7번 노드
    [1, 7]  # 8번 노드
]

visited = [False] * 9
BFS(gragh, 1, visited)


# BFS에서 큐의 자료 이동을 반드시 확인 할 것
# 큐에서 맨 왼쪽 요소가 나갔다는 의미는 즉, 방문을 의미한다.
# 방문과 동시에 visited[i]가 False인 요소들을 gragh[v]에서 모두 큐에 추가한다.
# 이런 과정을 반복하다 보면 너비우선 탐색이 가능하다.
# deque([1])
# deque([2, 3, 8])
# deque([3, 8, 7])
# deque([8, 7, 4, 5])
# deque([7, 4, 5])
# deque([4, 5, 6])
# deque([5, 6])
# deque([6])
