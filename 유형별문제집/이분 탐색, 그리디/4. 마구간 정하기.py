n,c = map(int, input().split()) #c는 말의 개수
arr = []

def q_s(arr):
    if len(arr)==0:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]
    return q_s(left) + [pivot] + q_s(right)

def Count(target_horse): #target_horse: 말 사이의 거리
    count = 1
    end_point = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-end_point >= target_horse:
            count +=1
            end_point = arr[i]
    return count


for _ in range(n):
    arr.append(int(input()))

arr = q_s(arr)
start = 1
end = max(arr)
res = 0
while start <= end:
    mid = (start+end)//2
    # 처음 mid 값:5, return:2(배치 거리가 너무 길다) -> else : end=mid-1
    if Count(mid) >= c : #배치 거리가 짧아서 말의 개수가 더 많이 배치되면, 배치거리를 늘린다. start = mid + 1
        res = mid
        start = mid +1

    else : #배치거리가 길어서 말의 개수가 너무 적게 배치되면, 배치거리를 줄인다. end = mid-1
        end = mid -1

print (res)