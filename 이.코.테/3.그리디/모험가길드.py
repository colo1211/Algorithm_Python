n = int(input())
friends = list(map(int,input().split()))
friends.sort()
group = 0
sum = 0
for i in range(n):
    sum += 1
    if sum >= friends[i]:
        group += 1
        sum = 0
print(group)
