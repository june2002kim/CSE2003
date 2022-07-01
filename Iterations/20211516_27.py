sum_=[]
while True:
    a=int(input("정수를 입력 (0을 입력하면 종료) : "))
    if a==0:
        break
    sum_.append(a)
print(f"입력한 정수 리스트 : {sum_}")
print(f"합계 : {sum(sum_)}")
print(f"평균 : {sum(sum_)/len(sum_)}")
