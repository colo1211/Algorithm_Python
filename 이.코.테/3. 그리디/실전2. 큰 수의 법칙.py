n,m,k = map(int, input().split())
arr = list(map(int,input().split()))
# n은 배열의 개수, m은 합의 개수, k는 최대 연속 개수
arr.sort()
arr_max_1 = arr[-1]
arr_max_2 = arr[-2]

result = 0
sum = 0

for i in range(m): #8번
    if sum == k: #3번이면 2번째 큰 수를 더해준다.
        result += arr_max_2
        sum = 0
    else :
        result += arr_max_1
        sum += 1
    # print(i,'번째 :', result,sum)
print(result)

