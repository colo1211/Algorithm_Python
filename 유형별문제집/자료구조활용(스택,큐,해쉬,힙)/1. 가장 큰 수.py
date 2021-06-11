num,n = map(int,input().split())
arr = list(map(int, str(num)))

stack = []
for want_to_input in arr: # 배열을 순차적으로 스택에 추가
    while stack and n>0 and stack[-1] < want_to_input: # 추가할 원소를 stack에 자기보다 큰 수가 있으면 제거 후 append ,
        # while stack : 비어있으면 진행 X, 차있으면 진행 O
        stack.pop()
        n -= 1
    stack.append(want_to_input)
if n != 0:
    stack = stack[:-n]

res = ''.join(map(str, stack))
print(res)