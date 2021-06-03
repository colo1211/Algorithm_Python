n, c = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort()

def Count(least_distance):
    count = 1
    end_point = arr[0]
    for i in arr:
        if i-end_point >= least_distance:
            count +=1
            end_point = i
    return count

start = arr[0]
end = arr[-1]
res= 0

while start <= end :
    mid = (start+end)//2
    if Count(mid)>=c: #3마리 배치할라면 4마리도 정답영역은 가능하므로
        res = mid
        start = mid +1
    else :
        end = mid -1

print(res)