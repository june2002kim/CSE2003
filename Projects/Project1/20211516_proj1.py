from time import *
from string import *

def countWords(fName,puncTable,startTag,lastTag):
    #단어의 사용 횟수 계산, {단어 : 사용횟수}의 사전 반환
    fp=open(fName,'r',encoding="utf-8")
    for s in fp:
        if s.startswith(startTag):
            break
    words={}
    for s in fp:
        if s.startswith(lastTag):
            break
        s=s.replace("'s","")
        s=s.replace("'S","")
        s=s.translate(puncTable)

        for w in s.split():
            w=w.lower()
            words[w]=words.get(w,0)+1

    fp.close()
            
    return words

def puncTableGen():
    #구두점 제거를 위한 map table 생성
    map_dict={}
    for ch in punctuation:
        map_dict[ch]=''
    map_dict['-']=' '
    table=str.maketrans(map_dict)
    
    return table

def sortWords(wDict):
    #사전을 내림차순으로 정렬, (사용횟수, 단어)의 리스트 반환
    wList=[]
    for key, val in wDict.items():
        wList.append((val,key))
    wList.sort(reverse=True)
       
    return wList

def countLeastWds(wList):
    #최소 사용된 단어와 그 횟수 계산 및 반환
    leastUsed=wList[len(wList)-1][0]

    cnt=0

    for i in range(len(wList)-1,-1,-1):
        if wList[i][0]!=leastUsed:
            break
        else:
            cnt+=1

    return leastUsed, cnt

def outWordStat(wDict,outFName,inFName):
    #단어 빈도 파일 출력
    wList=sortWords(wDict)
    leastUsed, wCnt=countLeastWds(wList)

    fp=open(outFName, 'w')
    print(f"전자서적 이름 : {inFName}\n", file=fp)
    print(f"사용된 단어의 개수 : {len(wList):,}\n", file=fp)
    print(f"사용회수가 가장 작은 단어 통계", file=fp)
    print(f"사용회수: {leastUsed}, 단어수: {wCnt:,}, 백분율: {int(wCnt/len(wList)*100)}%\n", file=fp)
    print(f"단어별 사용회수(내림차순)\n",end="", file=fp)
    for i in range(len(wList)):
        print(f"{wList[i][1]:<15}{wList[i][0]:>5,}", file=fp)

    fp.close()
    
inFName="Little_Princess.txt"
startTag="Produced by"
lastTag="End of Project"
outFName="Word_stat.txt"

startTime=time()

puncTable=puncTableGen()
wordsDict=countWords(inFName,puncTable,startTag,lastTag)

outWordStat(wordsDict,outFName,inFName)

execTime=time()-startTime

print("실행 완료 (소요 시간 = %.2f 초)" %execTime)
