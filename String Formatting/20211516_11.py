a, b, c=input("정수 숫자 3개를 입력 : ").split()

a=int(a)
b=int(b)
c=int(c)
sum_=a+b+c
avg_=sum_/3


print(f"입력 받은 값 : {a} {b} {c}")
print(f"총합 : {sum_}")
print(f"평균 : {avg_:.1f}")
