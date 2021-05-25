# 1. 조금 더 구현, 완전 탐색 스럽게 푸는 풀이 dx,dy를 사용하면 쉽게 풀이 가능
n = int(input())
direct = list(input().split())
y,x = 0,0
dy = [0, 0,-1,1]
dx = [-1,1, 0,0]
direct_menu = ['L','R','U','D']

nx,ny =0,0
for dir in direct:
    for i in range(len(direct_menu)):
        if dir == direct_menu[i]:
            ny=y+dy[i]
            nx=x+dx[i]

        if nx<0 or nx>n-1 or ny<0 or ny>n-1:
            continue
        else :
            y=ny
            x=nx

print(y+1,x+1)



## 2. 내가 생각한 풀이
# n = int(input())
# direct = list(input().split())
# user_y = 0
# user_x = 0
#
# for dir in direct :
#     if dir == 'L':
#         if user_x-1 <0 :
#             continue
#         else :
#             user_x-=1
#
#     elif dir == 'R':
#         if user_x+1 >n-1:
#             continue
#         else :
#             user_x+=1
#     elif dir == 'U':
#         if user_y-1 <0:
#             continue
#         else :
#             user_y-=1
#
#     elif dir == 'D':
#         if user_y+1>n-1:
#             continue
#         else :
#             user_y += 1
#
# print (user_y+1,user_x+1)