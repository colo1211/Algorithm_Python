table = []
for i in range(10):
    table.append(list(map(int,input().split())))
ant_y = 1
ant_x = 1


while True:
        if table[ant_y][ant_x] == 2 or (table[ant_y+1][ant_x] == 1 and table[ant_y][ant_x+1] == 1):
            table[ant_y][ant_x]=9
            break

        # 오른쪽을 봤을 때 1이 아니면 오른쪽 이동
        if table[ant_y][ant_x+1] != 1:
                table[ant_y][ant_x] = 9
                ant_x+=1

        # 오른쪽을 봤을 때 1이면 아래로 이동
        elif table[ant_y][ant_x+1] == 1:
            table[ant_y][ant_x] = 9
            ant_y += 1

for i in range(10):
    for j in range(10):
        print(table[i][j], end=' ')
    print()