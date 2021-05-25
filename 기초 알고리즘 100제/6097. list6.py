def on_stick(table, stick):
    if stick[1] == 0: # 가로
        for i in range(0, stick[0]):
            table[stick[2]-1][stick[3]-1+i]=1

    elif stick[1] == 1: # 세로
        for i in range(0, stick[0]):
            table[stick[2]-1+i][stick[3]-1]=1


h, w = map(int, input().split()) #격자판 가로, 세로
n = int(input()) # 스틱 개수
stick_info = []
for i in range(n):
    stick_info.append(list(map(int, input().split())))
# stick_info[0] : 막대의 길이(l)
# stick_info[1] : 막대의 방향(d) (0일때 가로, 1일때 세로)
# stick_info[2] : x (막대의 왼쪽 혹은 위쪽x), -1필요
# stick_info[3] : y (막대의 왼쪽 혹은 위쪽y), -1필요

table = [[0]*w for _ in range(h)]

for i in range(n):
    on_stick(table, stick_info[i])

for i in range(h):
    for j in range(w):
        print(table[i][j], end=' ')
    print()
