num = input()
n = len(num)
result = int(num[0])
for i in range(1,n):
    data = int(num[i])
    if data<=1 or result<=1:
        result += data
    else :
        result *= data

print(result)