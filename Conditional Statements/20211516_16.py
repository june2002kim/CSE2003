a, b=input("두 자리 정수 두개를 입력 : ").split()
a, b=int(a), int(b)

a_1=a//10
a_2=a%10
b_1=b//10
b_2=b%10

if a==b:
    print(f"두 정수는 모두 {a} 로 같은 정수입니다.")

elif 10*a_2+a_1==b:
    print(f"{a} , {b} : 자리 값만 다른 정수입니다.")

elif a_1!=b_1 and a_1!=b_2 and a_2!=b_1 and a_2!=b_2:
    print(f"{a} , {b} : 일치하지 않는  정수입니다.")

else:
    print(f"{a} , {b} : 하나의 숫자만 일치합니다.")
