#if 귀찮은거
def isPassword(x):
    cnt=0
    isValid=0
    
    if x.isalpha()==True:
        print("error! 숫자도 포함되어야 함")
        isValid+=1
    if x.isnumeric()==True:
        print("error! 영문도 포함되어야 함")
        isValid+=1
    if x.isalnum()==False:
        print("error! 영문자, 숫자로만 구성되어야 함")
        isValid+=1
    if len(x)<8:
        print("error! 8 글자 이상이어야 함")
        isValid+=1
   
    for i in range(len(x)):
        if x[i].isnumeric()==True:
            cnt+=1
                
    if cnt<2:
        print("error! 최소한 2개의 숫자를 포함해야 함")
        isValid+=1

    return isValid

for i in range(5):
    x=input("Enter password: ")
    a=isPassword(x)
    if a==0:
        print("Valid password")
        break
    else:
        print("Invalid password")            
                
