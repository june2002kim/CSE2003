#이상한거
N=input("N : ")

cnt=0

if len(N)==1:
    N='0'+N
    
NN=N
N_=''

while NN!=N_:
    if len(N)==1:
        N='0'+N
    
    M=str(int(N[0])+int(N[1]))
    
    if len(M)==1:
        M_=M
    else:
        M_=M[1]

    N_=N[1]+M_
    cnt+=1

    N=N_

print(f"Cycle : {cnt}")
