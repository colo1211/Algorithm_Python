n,k  = map(int,(input().split()))
#n은 배열의 길이, k는 스와핑 개수
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2)

#n은 5
for i in range(0,k):
    arr1[i],arr2[n-i-1] = arr2[n-i-1],arr1[i]

print(sum(arr1))
#sum=0
# for i in range(n):
#     sum+=arr1[i]
# print(sum)

#1. sum 내장함수를 사용하면 리스트의 sum을 빠르게 구할 수 있다.
#2. C언어에서 temp로 swaping 하던 것을 파이썬에서는 a,b=b,a 로 빠르게 swap할 수 있다.