n = input()
n = list(n)
result=''
for i in n:
    if not 65<=ord(i)<=90 and not 97<=ord(i)<=122:
        result+=i
result=int(result)
print(result)
count =0
for i in range(1,result+1):
    if result % i == 0:
        count += 1
print(count)