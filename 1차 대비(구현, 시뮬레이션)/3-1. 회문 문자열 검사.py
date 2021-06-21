n = int(input())
for i in range(0,n):
    s = input()
    flag = 0
    s = s.upper()
    for j in range(len(s)//2):
        if s[j] != s[len(s)-1-j]:
            flag=1
            break
    if flag == 0:
        print(f'#{i+1} YES')
    else :
        print(f'#{i+1} NO')
