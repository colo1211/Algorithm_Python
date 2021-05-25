n, m = map(int,input().split())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))

min_list = [100]*n

for i in range(n):
    for j in range(m):
        if min_list[i] > table[i][j]:
            min_list[i] = table[i][j]
print(max(min_list))
