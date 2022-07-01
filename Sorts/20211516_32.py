#Insertion Sort

import random
L = random.sample(range(1, 100), 10)

print('before sort : ', L)

for i in range(1, len(L)):
    j=i
    while j>0:
        if L[j]<L[j-1]:
            L[j], L[j-1]=L[j-1], L[j]
        else:
            break
        j-=1
    
print('after sort : ', L)
