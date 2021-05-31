import sys
# sys.stdin = open('input.txt','rt')

def quick_sort(card):
    if len(card)==0:
        return card
    pivot = card[0]
    tail = card[1:]
    left = [x for x in tail if x>=pivot]
    right = [x for x in tail if x<pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

n,k = map(int,input().split())
card = list(map(int,input().split()))
card = (quick_sort(card))
sum = set()
for i in range(0,len(card)):
    for j in range(i+1,len(card)):
        for m in range(j+1, len(card)):
            sum.add(card[i]+card[j]+card[m])
sum=quick_sort(list(sum))
print(sum[k-1])

#set은 중복제거용
# 내장함수 사용하지 말고 퀵소트_2 리스트 컴프리헨션 익숙해지기