arr = list(range(0,21))
# print(arr)
for _ in range(10):
    a,b = map(int,input().split())
    for i in range((b-a+1)//2): #b-a+1 : 길이의 절반만큼 반복하기 SWAP 하기 위해서
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
        # print(arr)
for i in range(1,len(arr)):
    arr[i-1]= arr[i]
arr.pop()
for i in arr:
    print(i, end='')
