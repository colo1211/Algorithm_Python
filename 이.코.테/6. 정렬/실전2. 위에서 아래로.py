n = int(input())
arr= []
for i in range(n):
    arr.append(int(input()))
# 방법 1.
# arr.sort()
# arr.reverse()
# 방법 2.
arr = sorted(arr,reverse=True)
print(arr)
