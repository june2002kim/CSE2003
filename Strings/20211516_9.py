sample="abcABCdEFaBCDeFAbC"
sample=sample.lower()
s1='abc'
s2='def'

print('"%s 문자열 : %d 인덱스, %d 번 존재"' %(s1, sample.find(s1), sample.count(s1)))
print('"%s 문자열 : %d 인덱스, %d 번 존재"' %(s2, sample.find(s2), sample.count(s2)))
