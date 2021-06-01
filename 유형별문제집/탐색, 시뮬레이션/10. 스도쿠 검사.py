arr = [list(map(int,input().split())) for _ in range(9)]
answer = 'YES'

def is_sudoku(y,x):
    arr_filter= [0] * 10
    count=0
    for i in range(3):
        for j in range(3):
          arr_filter[arr[y+i][x+j]]+=1
    for i in range(len(arr_filter)):
        if arr_filter[i] >=2 :
            return False
    return True



for y in range(0, 9, 3):
    for x in range(0, 9, 3):
        if is_sudoku(y,x)==False:
            answer='NO'
            break
print(answer)