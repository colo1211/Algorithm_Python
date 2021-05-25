n, k = map(int,input().split())
print(f'n:{n} k:{k}')
count =0
while n!=1:
    if n % k == 0 : # 나눠 떨어진다면
        n /= k
        count +=1
    else : # 안나눠떨어진다면
        n-=1
        count+=1

print(count)