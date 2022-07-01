L=[[1,2,3],[4,5],[6],[7,8]]
R=[]

for i in range(len(L)):
    x=0
    for j in range(len(L[i])):
        x+=L[i][j]**2
    R.append(x)

print(R)
