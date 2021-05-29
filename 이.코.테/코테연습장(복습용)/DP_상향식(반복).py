#아래에서 부터 시작하는 상향식 : 반복문
n=10
dt=[0]*(n+1) # 처음부터 계산 한 것들을 미리 기록하는 배열
#dt[0]은 비워둔다.
dt[1]=1
dt[2]=1
for i in range(3,n+1):
    dt[i] = dt[i-1]+dt[i-2]
    print(i, dt[i])
print(dt[n])