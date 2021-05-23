import time

n, k = map(int, input().split())
count = 0
# 최대한 많이 나누는 것이 최적의 해를 보장하는 것 (n이 1이 될 때 까지)
start_time = time.time()
# 나눠야 하는 수보다 클 때
while n > k:
    if n % k != 0:  # 나눠 떨어지지 않을 때
        n = n - 1
        count += 1
    elif n % k == 0:  # 나눠 떨어질 때
        n //= k
        count += 1

print(n, count)
while n > 0:
    n -= 1
    count += 1
end_time = time.time()
print(n, count, end_time-start_time) # 0 6 0.0
