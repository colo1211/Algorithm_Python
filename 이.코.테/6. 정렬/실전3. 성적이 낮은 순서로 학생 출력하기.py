people_num = int(input())
people_info = []

for i in range(people_num):
    temp = input().split()
    people_info.append((temp[0], int(temp[1])))
# 서로 다른 자료형의 데이터는 리스트로 들어갈 때 튜플로 들어가는 것이 관행
people_info = sorted(people_info, key=lambda s: s[1])

for i in range(people_num):
    print(people_info[i][0])