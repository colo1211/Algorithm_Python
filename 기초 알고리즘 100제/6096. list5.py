def change_color_y(arr, x):
    # print(f'함수로 전달된 y와 x: {y,x}')
    for i in range(19):
        if arr[i][x]==0:
            arr[i][x]=1
        else :
            arr[i][x]=0

def change_color_x(arr, y):
    # print(f'함수로 전달된 y와 x: {y,x}')
    for j in range(19):
        if arr[y][j] == 0:
            arr[y][j] = 1
        else:
            arr[y][j] = 0

# 리스트 입력
arr = []
for i in range(19):
    arr.append(list(map(int, input().split())))

n = int(input())

user_choice=[]
for i in range(n):
    user_choice.append(list(map(int,input().split())))

for y in range(n):
    change_color_y(arr, user_choice[y][1]-1)
    change_color_x(arr, user_choice[y][0]-1)

for y in range(19):
    for x in range(19):
        print(arr[y][x],end=' ')
    print()