n = input()
answer = int(n[0])
for i in range(1 , len(n)):
    num = int(n[i])
    if num <=1 or answer<=1:
        answer += num
    else:
        answer *= num
print (answer)