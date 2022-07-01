a, b, c=input("세 개의 정수를 입력하시오 : ").split()
a, b, c=int(a), int(b), int(c)

if a>b:
    if a>c:
        max_=a
        if b>c:
            middle_=b
            min_=c
        else:
            middle_=c
            min_=b
    else:
        max_=c
        middle_=a
        min_=b

else:
    if b>c:
        max_=b
        if a>c:
            middle_=a
            min_=c
        else:
            middle_=c
            min_=a
    else:
        max_=c
        middle_=b
        min_=a

print(f"내림차순 정렬: {max_} {middle_} {min_}")
