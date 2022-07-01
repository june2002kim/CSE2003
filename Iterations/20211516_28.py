#소수구하기
from math import *

n=int(input("구하려는 소수의 개수를 입력 : "))
i=1
cnt=1

while cnt<=n:
    prime=True
    i+=1
    j=2
    while j<=sqrt(i):
        if i%j==0:
            prime=False
            break
        j+=1
        
    if prime==True:
        print(i)
        cnt+=1
print(f"{n} 개의 소수를 찾았습니다.")


