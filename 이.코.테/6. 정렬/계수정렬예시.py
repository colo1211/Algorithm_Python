# 데이터의 크기가 한정된 상황에서 매우 빠른 속도를 자랑한다. O(N+K)
arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

