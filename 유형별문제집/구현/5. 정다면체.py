n,m = map(int, input().split())
sum_arr= []
sum_count=[0]*(m+n+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        sum_arr.append(i+j)
for i in range(len(sum_arr)):
    sum_count[sum_arr[i]]+=1

max = max(sum_count)
for i in range(len(sum_count)):
    if max == sum_count[i]:
        print(i, end=' ')


