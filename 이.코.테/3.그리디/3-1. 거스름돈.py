n = 1260
count= 0

money = [500,100,50,10]
for coin in money:
    count += n//coin #거스름돈을 coin으로 나눈 몫
    n %= coin
print(count)
