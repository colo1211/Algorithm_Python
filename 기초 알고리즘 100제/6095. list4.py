n=int(input())
arr=[[0]*19 for _ in range(19)]

for _ in range(n):
    y,x = map(int,input().split())
    arr[y-1][x-1]=1

for y in range(19):
    for x in range(19):
        print(arr[y][x],end=' ')
    print()

# 줄바꿈 : print() , \n (간격 더 넓음)