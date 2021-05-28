def rice_cake_cut(arr, target, start, end):
    while start<=end:
        mid=(start+end)//2
        total = 0
        for x in arr:
            if x > mid : #mid 보다 큰 arr요소들만 빼서 total 함수에 더한다.
                total += (x-mid)

        if total==target: #target 길이가 나온다면 바로 mid를 return
            return mid
        elif total>target: #목표한거 보다 더 많이 잘린다면? mid+1
            start = mid+1
        else : #목표한거 보다 덜 잘렸다면? end = mid-1
            end = mid-1

n, m= map(int, input().split()) #n은 떡의 개수 m은 고객 오더 떡 길이
arr = list(map(int,input().split()))
arr.sort()
print(rice_cake_cut(arr,m,0,arr[-1]))
