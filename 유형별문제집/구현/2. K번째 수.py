# 리스트 슬라이싱을 할때는 인덱스를 문제가 요구하는 것과 항상 맞추기
# 문제에서는 리스트가 1부터 시작한다. (종이에 써보고 코드 짜기)
import sys
sys.stdin = open('input.txt','rt')
t= int(input())
for i in range(t):
    n,s,e,k = map(int, input().split())
    arr = list(map(int,input().split()))
    new_arr = arr[s-1:e]
    new_arr.sort()
    print('#',i+1,new_arr[k-1])

