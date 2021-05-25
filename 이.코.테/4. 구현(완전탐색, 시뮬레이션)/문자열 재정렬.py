# sort() 함수는 문자간 정렬도 지원 가능
# isalpha 는 해당 문자가 알파벳인지 판별하는 기능
# 방법 1. 모범답안
data = input ()
result = [] # 이외 다른 문자들을 넣은 배열
value = 0 # 숫자의 합
for i in data:
    if i.isalpha(): # 알파벳이 참이면
        result.append(i)
    else : #숫자라면
        value += int(i)

result.sort()
result.append(str(value))
print(''.join(result))

# 방법 2. 나의 풀이 (쓰레기)
# ch = input()
# n = len(ch)
#
# new_ch=[]
#
# for i in range(n):
#     num=ord(ch[i])
#     new_ch.append(num)
# new_ch.sort()
# a=[]
#
# for i in range(n):
#     change_ch = chr(new_ch[i])
#     a.append(change_ch)
# sum =0
# for i in range(n):
#     if not ('A' <= a[i] <= 'Z'):
#         sum+= int(a[i])
#         a[i]=0
# a.append(str(sum))
# while 0 in a:
# 	a.remove(0)
#
# print(''.join(a))
