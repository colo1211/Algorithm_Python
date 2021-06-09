n = int(input())
arr = list(map(int, input().split()))

temp = [] #뭐가 더 큰지 판별해주는 임시 저장 리스트

start = 0
end = len(arr)-1
last_num = 0

while start <= end:
    temp.append((arr[start], 'L')) #왼쪽 값을 넣어준다.
    temp.append((arr[end], 'R')) #오른쪽 값을 넣어준다.
    if temp[0][0] < temp[1][0] and last_num < temp[0][0]:
        last_num = temp[0][0]
        start +=1
        print(temp[0][1])
    if temp[0][0] > temp[1][0] and last_num < temp[1][0]:
        last_num = temp[1][0]
        end -= 1
        print(temp[1][1])


print(temp)