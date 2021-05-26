# DFS는 기본적으로 스택과 재귀함수로 구현이 가능하다.
# 재귀함수로 구현 하기 위해서는 gragh, visited list 가 필요하다.
# gragh는 인접 노드 정보를 담은 리스트, visited는 방문 여부를 체크하는 리스트다.
def dfs(gragh, n, visited):
    print(f'{n}번 노드 방문함!')
    visited[n]=True # 방문처리
    for i in gragh[n]:
        if visited[i] == False:
            dfs(gragh,i,visited)
            print(f'더이상 갈 곳 없어 나 다시 {n}번 노드로 돌아간다~')


gragh = [ #인접 노드에 대한 정보
    [],#0번 노드
    [2,3,8], #1번 노드
    [1,7],#2번 노드
    [1,4,5],#3번 노드
    [3,5],#4번 노드
    [3,4],#5번 노드
    [7], #6번 노드
    [2,6,8], #7번 노드
    [1,7] #8번 노드
]
visited = [False] *9

dfs(gragh,1,visited)