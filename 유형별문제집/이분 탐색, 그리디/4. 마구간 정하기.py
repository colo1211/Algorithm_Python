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
    count = 0
    for x in range(len(arr)):
        if x+target_horse < len(arr):
            count += 1
        else :
            return count


for _ in range(n):
    arr.append(int(input()))

arr = q_s(arr)
start = 1
end = max(arr)
res = 0
while start <= end:
    mid = (start+end)//2
    if Count(mid) <= c : #Count(mid) : 말 배치 가능 개수 , mid : 말 사이의 거리
        res = mid
        # print(res)
        end = mid - 1

    else :
        start = mid + 1
print (arr[res]-arr[0])