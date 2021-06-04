def q_s(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    return q_s(left)+[pivot]+q_s(right)

def solution(array, commands):
    answer = []
    for y in range(len(commands)):
        i = commands[y][0]-1
        j = commands[y][1]-1
        k = commands[y][2]-1
        # print(i,j,k)
        parse_arr = array[i:j+1]
        # print(parse_arr)
        parse_arr = q_s(parse_arr) #오름 차순 정렬
        #print(parse_arr)
        answer.append(parse_arr[k])
        print(parse_arr[k])
    return answer

