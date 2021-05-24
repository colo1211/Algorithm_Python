w, h, b = map(int, input().split(' '))
b /= 8 #bit를 byte화
pic_size = w*h*b/1024**2
print(format(round(pic_size,2),'.2f'), 'MB')
