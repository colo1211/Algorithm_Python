n = int(input())
n_list = []
arr= list(map(int, input().split())) #arr은 역수열 값
arr = arr[::-1]
for i in arr:
    n_list.insert(i,n)
    n -= 1
print(n_list)
