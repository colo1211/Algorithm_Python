n = int(input())
arr = list(map(int,input().split()))

def digit_sum(x):
    x= str(x)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    return sum

max= 0
for idx, x in enumerate(arr):
    if max < digit_sum(x): #max 보다 크다고 했기 때문에 다음 max값과 같은 것이 나올때는 갱신 X. 만약 max<=digit(x) 로 했으면 마지막 동일값 저장
        max = digit_sum(x)
        index = idx
print(arr[index])
