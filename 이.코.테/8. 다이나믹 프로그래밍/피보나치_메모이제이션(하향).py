# 하향식은 보통 재귀함수로 구현
# 피보나치 수열 99까지의 합을 구하는 문제
d = [0]*100 # 이미 계산 한 것을 기록하는 테이블(캐싱, 메모이제이션)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if d[n]!=0: #0이 아니라면 바로 d[n]=d[n-1]+d[n-2]를 리턴한다.
        return d[n]
    d[n] = fibonacci(n-1)+fibonacci(n-2)
    return d[n]
print(fibonacci(99))
