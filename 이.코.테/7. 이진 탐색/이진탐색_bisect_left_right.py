from bisect import bisect_left,bisect_right

arr = [1,2,4,4,8]
left = bisect_left(arr,4) #왼쪽에서 부터 탐색하여 Target Index 반환
right = bisect_right(arr,4) #오른쪽에서부터 탐색하여 Target Index 반환
print(left,right,'4의 총 개수:',right - left)
