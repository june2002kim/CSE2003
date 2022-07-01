#사전 정렬
D={'c':7,'f':3,'a':5}
keyList=sorted(D)
L=[]

for i in keyList:
    L.append((i,D.get(i)))

print(f"After sort : {L}")
