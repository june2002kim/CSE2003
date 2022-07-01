#파일 입출력
fR=open('input_37.txt','r')
fW=open('output_37.txt','w')
Result={}
avgTot=0

for s in fR:
    Result[s.split()[0]]=[float(s.split()[1]), float(s.split()[2])]
    avgTot=avgTot+float(s.split()[1])+float(s.split()[2])

avgTot/=len(Result)*2

print('student'.ljust(17),end='', file=fW)
print('average',end=' ', file=fW)
print('pass/fail', file=fW)

for i in Result.keys():
    print(i.ljust(17),end='', file=fW)
    avg=(Result[i][0]+Result[i][1])/2
    print(f"{avg:.2f}",end='', file=fW)
    if avg>=avgTot:
        print('p'.rjust(4), file=fW)
    else:
        print('f'.rjust(4), file=fW)

print(f"total avg : {avgTot:.2f}", file=fW)

fR.close()
fW.close()

    
