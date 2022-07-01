n1, n2=input("두 자연수 N1과 N2를 입력하세요(0 < N1 <= N2) : ").split()
n1, n2=int(n1), int(n2)
sum_=0

if n1>n2 or n1<=0 or n2<=0:
    print("조건에 맞는 두 자연수를 입력하세요. (0 < N1 <=N2)")

else:

    if n1%2==0:
        s=n1
    else:
        s=n1+1

    if n2%2!=0:
        e=n2
    else:
        e=n2+1

    for i in range(s, e, 2):
        sum_+=i
    print(f"크기가 {n1} 이상이고 {n2} 이하인 모든 짝수의 합은 {sum_}입니다.")
    
