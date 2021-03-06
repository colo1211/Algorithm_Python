## 다이나믹 프로그래밍 (Dynamic Programming, DP)

- 하나의 문제는 `딱! 한번만` 풀도록 하는 알고리즘 <br>
- 이미 계산된 것은 다시는 계산을 안해서 메모리(공간)는 차지하더라도 시간적 효율을 극대화

#### 대표적 예시 : 피보나치 수열

### DP를 사용해야 할수 있겠다는 조건
`점화식 만들어 낼 수 있어?` : 그럼 DP로 구현  
#### A (n) = A (n-1) + A (n-2) 단, A(1)=1 , A(2)=1

### DP 를 할 수 있는 조건 
1. `최적 부분 문제` : 큰 문제를 작은 문제로 나눠서 해결한다. 
2. `중복 부분 문제` : 동일한 중복된 문제들은 반복 해결한다. 

> DP와 분할 정복법의 차이점 : 중복 부분의 유무(조건2)

###  DP 유형 
1. Bottom Up (상향식) : 아래에서 부터 해결 (Using 반복문) <br> 
   ````
       # 상향식은 보통 반복문으로 구현
    # d[n] = d[n-1]+d[n-2] : 결과를 저장하기 위한 dp 테이블 초기화
    d = [0] * 100 #1부터 99까지 이므로 100을 곱
    d[1]=1
    d[2]=1
    n = 99
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    
    print(d[n])
   ````
2. Top Down (하향식) : 위에서 부터 아래로 해결 (Using 재귀함수) <br> 
   * 메모이제이션(Memoization 기법,캐싱 Caching 기법)    
   ````
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
   ````