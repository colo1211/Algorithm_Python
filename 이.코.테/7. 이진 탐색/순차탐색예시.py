def seq_search(arr, n , target):
    for i in range(n):
        if arr[i] == target:
            return i

print('생성 원소 개수, 문자열을 한칸 띄어 입력하라')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('문자열 Full 입력 ㄱㄱ')
arr = input().split()
print(seq_search(arr, n, target)+1)
