num1, op, num2=input("수식 입력(예: 20 * 40) : ").split()
num1, op, num2=float(num1), str(op), float(num2)

if op=='+':
    result=num1+num2
    print(f"{num1:f} + {num2:f} = {result:f}")

elif op=='-':
    result=num1-num2
    print(f"{num1:f} - {num2:f} = {result:f}")

elif op=='*':
    result=num1*num2
    print(f"{num1:f} * {num2:f} = {result:f}")

elif op=='/':
    if num2==0:
        print(f"{num2:f} 로 나누기를 수행할 수 없습니다.")
    else:
        result=num1/num2
        print(f"{num1:f} / {num2:f} = {result:f}")

else:
    print(f"{op} 지원하지 않는 연산자입니다.")

