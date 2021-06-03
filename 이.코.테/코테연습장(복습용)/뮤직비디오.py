n, m = map(int,input().split())
arr=list(map(int,input().split()))

def Count(Threshold):
    count = 1
    sum = 0
    for i in arr:
        if i+sum > Threshold:
            count +=1
            sum = i
        else :
            sum+=i
    return count

start = 1
end = sum(arr)
res= 0
while start <= end:
    mid = (start+end)//2
    if Count(mid) <= m: #용량이 커서 return(CD개수)이 목표보다 적다면
        res= mid
        end = mid - 1
    else :
        start = mid +1


print(res)