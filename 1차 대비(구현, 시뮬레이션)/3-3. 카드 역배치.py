arr = [i for i in range(1,21)]
for _ in range(10):
    a,b = map(int,input().split())
    a= a-1
    for i in range(a,b):
        arr[i], arr[b-1-i] = arr[b-1-i], arr[i]
        print(arr)