# 입력
k, n = map(int,input().split())
arr= []
for i in range(k):
    arr.append(int(input()))

def Count(mid):
    ack_sum = 0
    for i in arr:
        ack_sum += i//mid
    # print(ack_sum)
    return ack_sum

# 1부터 최대값까지 정답의 범위라고 생각 (1~802)
max_arr = max(arr)

start = 1
end = max_arr
answer = 0
while start <= end :
    mid = (start+end)//2
    if Count(mid) >= n : # 타겟보다 더 많이 나온다면? (나누는 인자를 크게한다)-> start=mid+1
        answer = mid
        start = mid+1
    else : # 타겟보다 더 적게 나온다면? 나누는 인자를 더 작게한다.
        end = mid-1

print(answer)
