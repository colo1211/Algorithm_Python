a, m, d, n = map(int,input().split())
i=1
while True:
    if i == n:
        print(a)
        break
    a = a * m + d
    i+=1