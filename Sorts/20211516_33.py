#Selection Sort

import random
i = 0
L = random.sample(range(1, 100), 10)

print('before sort : ', L)

while i<len(L):
    min_=L[i]
    for j in range(i, len(L)):
        if min_>L[j]:
            min_=L[j]
    min__=L.index(min_)
    L[i], L[min__]=L[min__], L[i]
    i+=1

print('after sort : ', L)
