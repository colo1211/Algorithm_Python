n = int(input())
arr = list(map(int,input().split()))

def reverse(x):
    x = int(x[::-1]) #문자열 전체 모두 뒤집기
    return x

def isPrime(x):
    count = 1
    if x == 2 :
        return True

    for i in range(2,x+1):
        if x%i == 0:
            count+=1

    if count ==2 :
        return True
    return False

for i in arr:
    i = str(i)
    if isPrime(reverse(i)) == True:
        print(reverse(i), end=' ')
