n = int(input())
arr = list(map(int, input().split()))
temp = [] #뭐가 더 큰지 판별해주는 임시 저장 리스트
start = 0
end = len(arr)-1
last_num = 0
result = ''
while start <= end:
    if arr[start] > last_num:
        temp.append((arr[start],'L'))
    if arr[end] > last_num:
        temp.append((arr[end],'R'))
    temp.sort() # 2차원 배열을 정렬

    if len(temp) == 0:# temp 배열이 길이가 0이면 종료
        break
    else:
        result += temp[0][1]
        last_num = temp[0][0]
        if temp[0][1] == 'L':
            start +=1
        else :
            end -= 1
    temp.clear()

print(len(result))
print(result)