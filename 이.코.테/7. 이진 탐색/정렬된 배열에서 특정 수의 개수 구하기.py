from bisect import bisect_left, bisect_right
import sys
n, m = map(int,(sys.stdin.readline().rstrip().split()))
arr= list(map(int,(sys.stdin.readline().rstrip().split())))

left = bisect_left(arr,m)
right = bisect_right(arr,m)

if left-right==0:
    print(-1)
else :
    print(right-left)


