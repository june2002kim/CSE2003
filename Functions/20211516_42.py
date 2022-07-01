#소수찾기
def isPrime(x):
    cnt=0
    
    for i in range(2, x):
        if x%i==0:
            cnt+=1

    if cnt==0 and x!=1:
        return True
    else:
        False

a, b=input("소수 찾기를 시작할 숫자와 소수 개수를 입력하시오: ").split()
a, b=int(a), int(b)
c=a
x=0

while True:
    if isPrime(c):
        print(c)
        x+=1
        
    if x==b:
        break
    c+=1

print(f"** {a}부터 {b} 개의 소수를 찾았습니다!")
