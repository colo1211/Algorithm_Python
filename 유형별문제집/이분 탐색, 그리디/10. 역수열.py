n = [0]*(int(input()))
arr= list(map(int, input().split())) #arr은 역수열 값
for i in range(0,len(arr)):
    if arr[i] == 0:
        n.insert(0,i+1)
    else :
        n[arr[i]] = i+1
    print(n)
