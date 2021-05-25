n = int(input('n시를 입력하시오:'))
# 00시 00분 00초 ~ N시 59분 59초
# 하루 총 86400 가지 경우의 수
# 파이썬 1초 -> 2천만 처리

count =0

for hour in range(n+1):
    for minute in range(60):
        for sec in range(60):
            # if hour % 10 == 3 or (minute//10 == 3 or minute%10 == 3) or (sec//10==3 or sec%10==3):
                if '3' in str(hour)+str(minute)+str(sec):
                    count +=1
                # print(f'{hour}시 {minute}분 {sec}초')
print(count)