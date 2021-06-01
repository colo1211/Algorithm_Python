# 예외처리 신경쓰기
N = int(input())
arr = list(map(int, input().split()))

# 평균
avg = round(sum(arr)/N)
min = float('inf')
# enumerate : idx에는 인덱스, value에는 값을 순회하는 반복문 내에 사용하는 문법
for idx, x in enumerate(arr):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x # 평균과 갭이 작은 학생의 스코어
        res = idx+1 # 평균과 갭이 작은 학생의 인덱스
    elif tmp == min: # 현재의 갭과 최소값이 같다면
        if x > score: # 점수가 높은 학생의 번호를 답으로 cf. x>=score이면 같은 학생 중에 맨 뒤의 인덱스가 저장됨
            score =x
            res = idx+1

print(avg, res)
