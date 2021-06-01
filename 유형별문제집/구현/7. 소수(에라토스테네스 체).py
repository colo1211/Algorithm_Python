# 소수를 판별 할 수 있는 가장 빠른 논리구조 : `에라토스테네스 체`
# 다른 로직으로 해보니 모두 시간초과 판정 받음
n = int(input())
ch = [0]*(n+1) # 인덱스와 연동시킬 수 있는 ch를 생성
count = 0
for i in range(2,n+1):
    if ch[i]==0: # 0이면 (아직 기록 안되어 있으면 count)
        count +=1
        for j in range(i,n+1,i):
            ch[j]=1 # i의 배수라면 ch를 1로 marking
print(count)