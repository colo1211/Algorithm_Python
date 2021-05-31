import sys
# sys.stdin = open('input.txt','rt')
n , k = map(int,input().split())
count=0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
        if count == k:
            print(i)
            break
else :
    print(-1)

# 파이썬은 for-else 구문이 존재
# 만약 for문을 다 돌고 나면 else에서 -1을 출력