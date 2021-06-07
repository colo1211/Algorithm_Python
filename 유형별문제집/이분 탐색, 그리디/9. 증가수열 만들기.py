n = int(input())
arr = list(map(int,input().split()))
last_pop_num = arr.pop(arr.index(min(arr[0],arr[-1])))
temp = []
start = 0
end = n-2
while start <= end :
    print(start, end)
    if arr[start] < arr[end] and last_pop_num < arr[start]:
        temp.append((arr[start], 'L'))
        last_pop_num = arr[start]
    elif arr[start] > arr[end] and last_pop_num < arr[end]:
        temp.append((arr[end], 'R'))
        last_pop_num = arr[end]
    print('마지막 뽑은 번호:',last_pop_num)
    start +=1
    end -=1
print(arr,temp)
