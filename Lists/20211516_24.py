print("***** if조건문으로 작성 *****")
a=int(input("월을 입력하세요: "))

if a==1:
    b="January"
elif a==2:
    b="February"
elif a==3:
    b="March"
elif a==4:
    b="April"
elif a==5:
    b="May"
elif a==6:
    b="June"
elif a==7:
    b="July"
elif a==8:
    b="August"
elif a==9:
    b="September"
elif a==10:
    b="October"
elif a==11:
    b="November"
elif a==12:
    b="December"

print(f"{a}월은 {b}입니다")


L=["January","February","March","April","May","June","July","August","September","October","November","December"]
print("***** 리스트로 작성 *****")
a=int(input("월을 입력하세요: "))
print(f"{a}월은 {L[a-1]}입니다")
