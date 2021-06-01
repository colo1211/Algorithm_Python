n=int(input())
apple_tree=[list(map(int,input().split())) for _ in range(n)]
sum =0
start=end=n//2

for y in range(n): #세로축 증가
    for x in range(start, end+1): # 가로축 증가할 때 마다 범위 조정
        sum += apple_tree[y][x]
    if y < n//2 : # 중간 전에는 하나씩 증가시킨다.
        start -= 1
        end += 1
    else : # 중간 이후에는 하나씩 감소시킨다.
        start +=1
        end -=1
print(sum)
