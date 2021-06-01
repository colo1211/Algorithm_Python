n=int(input())
arr=[]
def is_collect(arr):
    count =0
    arr.sort()
    for i in range(1,len(arr)):
        vs = arr[0]
        if arr[i] != vs:
            count += 1
    if count==1: # 하나만 틀리다면
        return 1000+((arr[-1])*100)
    elif count==2: # 세다 틀리면
        return (arr[-1]*100)
    else :
        return 10000 + (arr[-1] * 1000)

for _ in range(n):
    arr.append(list(map(int,input().split())))

max = 0
for i in range(n):
    if max < is_collect(arr[i]):
        max = is_collect(arr[i])
print(max)
