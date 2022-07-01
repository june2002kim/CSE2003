for i in range(10):
    n=int(input("Enter a number : "))
    if n<0:
        x='음수'
    elif n>0:
        x='양수'
    else:
        break
        
    if n%2==0:
        y='짝수'
    else:
        y='홀수'
    print(f"{n} : {x}, {y}")
print("입력 받은 수가 0 입니다")
print("프로그램을 종료합니다")
