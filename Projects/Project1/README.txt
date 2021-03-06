<텍스트 단어 카운팅 프로젝트>



http://www.gutenberg.org에서 다운받은 소공녀 전자사적의 단어 분석을 위한 python 프로그램 작성
(소공녀 : http://www.gutenberg.org/cache/epub/146/pg146.txt)


본 프로그램은 파일에서 읽은 문자열을 단어로 분리하고, 각 단어의 사용횟수를 계산 및 출력하는 기능을 한다.



사용한 함수
1. countWords()
단어의 사용 횟수를 계산하는 함수

입력받은 텍스트파일의 앞과 뒤에 소설과 관계없는 내용이 있으므로 문자열 method startswith()로 읽은 line의 첫 부분에 찾고자 하는 패턴이 포함되는지 확인한다.
소설이 시작되는 바로 전 line에 "Produced by ..."라는 패턴을 찾을 때까지는 읽은 line을 무시하고 같은 원리로 소설이 끝난 후에는 "End of Project"라는 패턴을 찾으면 그 이상의 내용은 읽지 않도록 한다.

문자열 method maketrans() 와 translate()를 이용하여 영문 소설의 구두점을 제거한다.
maketrans()를 사용하여 각 구두점을 빈 문자열로 변환하기 위한 map table을 구성하고, translate()를 사용하여 구두점을 실제로 제거한다.
이 과정에서 map table을 만드는데 puncTableGen() 함수를 사용하였다.
참고
구두점을 제거함과 동시에 문자열 method replace()를 사용해 's 또는 'S도 제거해주고, 부호 '-'는 적절한 단어 분리를 위해 삭제가 아니라 빈칸으로 수정한다.
문자열의 대소문자 구분으로 같은 단어를 다른 단어로 인식하면 안되므로 문자열의 모든 영문자는 문자열 method lower()을 사용해 소문자로 바꾸어준다.

최종적으로 추출한 각 단어의 사용횟수를 구하여 반환한다.
추출한 단어 명단은 단어:사용횟수 쌍이며 이를 구현하기 위해 dictionary를 사용한다.

함수 작성에 필요한 변수
inFname		 : 	입력 파일 이름(문자열), 전자서적, utf-8 포맷
outFname	 : 	출력 파일 이름(문자열), 단어 빈도 출력 파일
startTag	 : 	전반부 제거를 위한 패턴(문자열)
lastTag		 : 	후반부 제거를 위한 패턴(문자열)
pucTable	 : 	구두점 제거를 위한 map table
wordsDict	 : 	함수 countWords()가 반환한 사전	


2. outWordStat()
단어의 사용 횟수를 출력하는 함수

프로그램의 출력엔 다음과 같은 세 가지 사항이 포함된다.
(1) 사용한 총 단어 개수
(2) 사용 횟수가 가장 적은 단어에 대한 통계. 즉, 사용 횟수가 가장 적은 단어들의 개수를 구하고, 전체 단어 개수 대비 이 단어 개수의 백분율을 구한다.
(3) 사용 횟수가 가장 많은 단어부터 내림차순으로 단어와 사용 횟수를 출력.

Dictionary는 원소간에 순서가 없으므로 리스트와 같은 순서가 있는 유형으로 변환하여 정렬할 필요가 있다.
따라서 sortWords(wDict)라는 함수를 정의하여 정렬된 wList를 반환한다. 해당 list의 끝 부분에는 사용 횟수가 가장 작은 단어들이 저장되어있다.
이들의 사용 횟수를 leastUsed라고 할때, 사용 횟수가 leastUsed인 단어들의 개수를 구하는 함수 countLeastWds()를 선언한다.
