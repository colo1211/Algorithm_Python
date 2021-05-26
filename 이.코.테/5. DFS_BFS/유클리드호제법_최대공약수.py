def GCD(a,b):
    if a%b==0:
        return b
    else :
        print (b,a%b)
        return GCD(b,a%b)

print(GCD(192,162))
# 162 30
# 30 12
# 12 6
# 6
