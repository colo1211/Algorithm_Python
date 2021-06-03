#m개의 DVD 내에 arr내에 있는 노래들을 모두 녹화
#이 때, 각 dvd에 가장 최소만큼 녹음 할 수 있게끔 배분하는 최대 DVD 용량은?
n, m = map(int,input().split())
arr=list(map(int,input().split()))

def Count(capacity): # mid(capacity)는 CD 1개의 용량
    cnt = 1
    sum = 0
    for x in arr:
        if sum+x > capacity: # 미리 더했을 때 초과되면
            cnt +=1
            sum = x
        else :
            sum+=x
    return cnt

start = 1
end = sum(arr)
res = 0
while start <= end:
    mid = (start+end)//2
    if Count(mid)<=m :
        # print(mid)
        res = mid
        end = mid -1
    else :
        start = mid + 1

print(res)