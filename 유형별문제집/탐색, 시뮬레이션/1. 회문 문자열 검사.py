#홀수던 짝수던 중간까지만 검사하면 된다.
n = int(input())

def isSame(arr):
    arr=arr.upper()
    n=int(len(arr)/2)
    flag = 0
    for i in range(0,n):
        if arr[i] != arr[len(arr)-i-1]:
            flag = 1
            break
    if flag == 1:
        return 'NO'
    return 'YES'

for i in range(n):
    arr = input()
    print (f'#{i+1} {isSame(arr)}')