# def quick_sort(arr):
#     if len(arr)==0:
#         return arr
#     pivot = arr[0]
#     tail = arr[1:]
#     left = [x for x in tail if x>=pivot]
#     right = [x for x in tail if x<pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)
card = []
for i in range(0,21):
    card.append(i)

for _ in range(10):
    a,b = map(int,input().split())
    for i in range((b-a+1)//2):
        card[a+i],card[b-i]=card[b-i],card[a+i] #파이썬 SWAP 문법

card.pop(0)
for x in card:
    print(x, end=' ')