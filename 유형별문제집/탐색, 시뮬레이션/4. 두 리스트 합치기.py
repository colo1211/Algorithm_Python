n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
new_arr = a+b
new_arr.sort()
for i in new_arr:
    print(i, end=' ')