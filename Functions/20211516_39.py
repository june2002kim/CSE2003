#사전으로 문자열에 쓰인 문자 개수 구하기
def countStr(x):
    x=x.lower()
    x=x.replace(' ','')

    D={}

    for i in range(len(x)):
        D[x[i]]=D.get(x[i],0)+1

    return D

x=input("문자열 입력 : ")
D=countStr(x)
for i in list(D):
    print(f"{i} : {D[i]}")
