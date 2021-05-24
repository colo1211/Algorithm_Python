n = int(input())
arr = list(map(int , input().split()))

for i in range(n-1,-1,-1):
    print(arr[i], end=' ')

#reverse() 를 사용하면 아예 리스트 자체가 뒤집힌다. 