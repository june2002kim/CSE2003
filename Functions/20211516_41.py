#random
from random import *

def CoinHead(x):
    cnt=0
    for i in range(x):
        if randint(0,1)==0:
            cnt+=1
        result=int(cnt/(i+1)*100)
        if i<10 or (i+1)%10==0:
            print(f"  {i+1} 번째까지 던지기에서 앞면이 나온 확률 : {result}%")

    return cnt

x=int(input("동전 던지기 시도 횟수를 입력(1 - 100) : "))
y=CoinHead(x)

result=int(y/x*100)

print("")
print("*"*66)
print(f"총 {x}번 동전 던지기에서 앞면이 나올 확률 : {result}%")
