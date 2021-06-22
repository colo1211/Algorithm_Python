n , m = map(int, input().split()) #n은 리스트 길이, m은 타겟
arr = list(map(int, input().split()))
lt = 0
rt = 1
total_sum = arr[0] # lt부터 rt바로 앞(rt-1)까지의 합
cnt = 0

while True :
    if total_sum < m: #타겟 숫자보다 작고
        if rt < n: # rt가 n보다 작다면
            total_sum += arr[rt]
            rt += 1
        else : #rt가 n보다 크거나 같다면
            break

    elif total_sum == m: #타겟 숫자와 동일하다면
        cnt += 1
        total_sum -= arr[lt]
        lt += 1

    else : #타겟 숫자보다 크다면
        total_sum -= arr[lt]
        lt += 1


print(cnt)