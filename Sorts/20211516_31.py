#Bubble Sort

import random
L = random.sample(range(1, 100), 10)

print('before sort : ', L)
cnt=0

while cnt<len(L)-1:
    i=0
    while i<len(L)-1:
        if L[i]>L[i+1]:
            L[i], L[i+1]=L[i+1], L[i]
        i+=1
    cnt+=1

print('after sort :', L)
    
