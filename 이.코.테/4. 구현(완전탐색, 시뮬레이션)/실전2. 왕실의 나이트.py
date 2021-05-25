night_pos = input()
#a~h는 x축에 해당 -> night_pos[0] : x축
#1~8은 y축에 해당 -> night_pos[1] : y축

x= ord(night_pos[0])-97 # x축을 숫자로 변환하는 과정
y= int(night_pos[1])-1 # y축을 숫자로 변환하는 과정

dy=[-2,-1,-2,-1, 1, 2,2,1]
dx=[-1,-2, 1, 2,-2,-1,1,2]
count =0
n = len(dy)
for i in range(n):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny<0 or nx<0 or nx>=8 or ny>=8:
        continue
    count +=1

print (count)

