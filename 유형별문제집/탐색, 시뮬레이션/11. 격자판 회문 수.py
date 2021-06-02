# 회문 검사: arr = arr[::-1]

arr = [list(map(int,input().split())) for _ in range(7)]
def is_same(arr):
    mid = len(arr)//2
    for i in range(0,mid+1):
        if arr[i] != arr[len(arr)-i-1]: #다르면
            return False
    return True

count = 0
for i in range(7): # 가로축 검사, 리스트 슬라이싱 가능 + arr[::-1] 하면 바로 역순 배치(회문 판별 쉬움)
    for j in range(3):
        temp = arr[i][j:j+5]
        if temp == temp[::-1]:
            print(arr[i][j:j+5])
            count +=1

for y in range(3): # 세로축 검사,세로축은 리스트 슬라이싱 불가, 따라서 별도의 함수 생성
    for x in range(7):
        result = []
        for t in range(5):
            result.append(arr[y+t][x])
        if is_same(result) == True:
            print(result)
            count += 1

print(count)