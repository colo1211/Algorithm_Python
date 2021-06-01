n = int(input())
arr= list(map(int,input().split()))

flag = 0
sum =0
ack_sum = 0
for i in range(len(arr)):
    if arr[i]==1 and flag==0:
        sum+=1
        flag=1
        ack_sum=1
    elif arr[i]==1 and flag==1:
        ack_sum += 1
        sum+=ack_sum
    else :
        ack_sum = 0
        flag=0
print (sum)