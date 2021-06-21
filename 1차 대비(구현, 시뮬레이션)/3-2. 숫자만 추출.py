ch = input()
num = ''
for i in range(len(ch)):
    if not 65<=ord(ch[i])<=90 and not 97<=ord(ch[i])<=122:
        num+=ch[i]
num = int(num)
print(num)
count = 0
for i in range(1, num+1):
    if num%i == 0:
        count +=1
print(count)