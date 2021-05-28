def find_target(arr_n,arr_target):
    result = []
    for i in arr_target:
        if i in arr_n: #리스트 내에 해당 요소가 존재하는지 확인
            result.append('YES')
        else :
            result.append('NO')
    return result



n = int(input())
arr_n = set(map(int,input().split())) #중복된 요소를 제거하기 위해 set(집합)자료형
m = int(input())
arr_target = list(map(int,input().split()))

result = find_target(arr_n,arr_target)
print(result)