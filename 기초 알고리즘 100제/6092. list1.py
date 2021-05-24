n=int(input())
arr= list(map(int,input().split()))
count = [0]*23

for i in range(n):
    count[arr[i]-1]+=1

for i in count:
    print(i, end=' ')

# print(~~~, end='')
# end='' -> 줄바꿈 멈춰!


