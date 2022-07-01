L=[1, 3, 5, 7, 9]

a=L[0]
for i in range(len(L)):
    if i==len(L)-1:
        L[i]=a
    else:
        L[i]=L[i+1]
print(L)
