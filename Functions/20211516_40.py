def Add(a, b):
    result=a+b
    return result

def Sub(a, b):
    result=a-b
    return result

def Mul(a, b):
    result=a*b
    return result

def Div(a, b):
    result=a/b
    return result

a, x, b=input("수식 입력(예: 20 * 40) : ").split()
a, b=float(a), float(b)

if x=='+':
    c=Add(a, b)
    print(f"{a:f} {x} {b:f} = {c:f}")

elif x=='-':
    c=Sub(a, b)
    print(f"{a:f} {x} {b:f} = {c:f}")

elif x=='*':
    c=Mul(a, b)
    print(f"{a:f} {x} {b:f} = {c:f}")

elif x=='/':
    if b==0:
        print(f"{b:f} 로 나누기를 수행할 수 없습니다.")
    else:
        c=Div(a, b)
        print(f"{a:f} {x} {b:f} = {c:f}")

else:
    print(f"{x} 지원하지 않는 연산자입니다")
