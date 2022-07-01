L=input("정수들을 입력 : \n").split()
n=0
plus=0
minus=0
sum_=0

while n<len(L):
    if int(L[n])>0:
        plus+=1
    elif int(L[n])<0:
        minus+=1
    sum_+=int(L[n])
    n+=1
if len(L)==0:
    print("입력한 숫자가 없습니다")
print(f"양수: {plus} 개, 음수 : {minus} 개, 합계 : {sum_}")

