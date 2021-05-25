n,m,k = map(int, input().split())
arr = list(map(int,input().split()))
# n은 배열의 개수, m은 합의 개수, k는 최대 연속 개수
arr.sort()
first = arr[-1]
second = arr[-2]
count=0 # 제일 큰 수가 등장하는 횟수

count = int(m/(k+1)*k)
count += m%(k+1) #안나눠 떨어질 때를 대비한 코드

result = count * first + (m-count) * second
print(result)

