n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

result = []
for y in range(n):
    sum_garo= 0
    for x in range(n):
        sum_garo+=arr[y][x]
    result.append(sum_garo)
for y in range(n):
    sum_sero = 0
    for x in range(n):
        sum_sero+=arr[x][y]
    result.append(sum_sero)

sum_cross=0
sum_cross_2=0
for y in range(n):
    sum_cross+=arr[y][y]
    sum_cross_2+=arr[y][n-y-1]
result.append(sum_cross)
result.append(sum_cross_2)
print (max(result))