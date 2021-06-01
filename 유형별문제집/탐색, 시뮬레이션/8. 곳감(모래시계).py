n = int(input())
arr_gam = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
arr_trans = [list(map(int, input().split())) for _ in range(m)]

for y in range(m):
    direct = arr_trans[y][1]
    y_pos = arr_trans[y][0]-1
    shift = arr_trans[y][2]
    if direct == 0 : # 왼쪽
        for i in range(shift):
            arr_gam[y_pos].append(arr_gam[y_pos].pop(0))
    elif direct == 1: # 오른쪽
        for i in range(shift):
            arr_gam[y_pos].insert(0,arr_gam[y_pos].pop())

start = 0
end = n-1
sum = 0
for y in range(n):
    for x in range(start, end+1):
        sum += arr_gam[y][x]
    if y<n//2:
        start += 1
        end -= 1
    else :
        start -= 1
        end += 1
print(sum)