a,r,n = map(int, input().split())
idx_count=1
while True:
    a *= r
    idx_count+=1
    if idx_count == n:
        print(a)
        break