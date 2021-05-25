a,b,c=map(int,input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)


# lcm : 최소공배수 , gcd : 최대공약수
# 언제 같은날 방문하는 지 묻는 문제이므로 최대공배수를 구하면 됨.