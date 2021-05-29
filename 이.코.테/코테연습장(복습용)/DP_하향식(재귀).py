dt = [0] * 6
def fibonacci (n):
    if n ==1 or n==2:
        return 1
    if dt[n]!=0: #비어있지 않다면 여기서 바로 리턴
        return dt[n]
    dt[n] = fibonacci(n-1)+fibonacci(n-2) #비어있다면 이전 식들을 활용하여 계산해서 dt를 채운다.
    print(n,dt[n])
    return dt[n]

print(fibonacci(5))