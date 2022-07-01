<Language modeling 프로젝트>



Language modeling은 다음에 오는 단어를 예측하는 문제로 n-gram이라는 연속되는 n개의 단어 조각이 등장하는 통계를 수집하고, 이를 사용하여 다음 단어를 예측하는 프로그램을 작성.



사용한 함수
1. preprocess()
소설책 데이터를 전처리하는 함수
Bigram LM을 학습하기 위해서 입력받은 텍스트파일의 앞과 뒤에 있는 소설과 관계없는 내용과 목차와 같은 완전한 문장이 아닌 내용을 제거한다.
Project1에서 진행한 내용과 유사하게 구두점 제거 및 문장을 끝내는 기호를 마침표로 통일하는 등 추가적인 전처리를 진행한다.
이 모든 전처리 과정들을 거친 후 완전한 문장 형태로 처리된 output file을 생성한다. ("preprocessed_Little_Lord_Fauntleroy.txt")


2. countingBigrams()
소설책에 등장하는 bigram을 수집
이때 문장의 시작을 의미하는 <s>와 문장의 끝을 의미하는 </s> 기호를 추가하여 bigram을 count한다.
본 프로젝트에서는 문장을 끝내는 기호를 "."으로 통일하였으므로 이를 </s>로 간주하고 bigram을 count한다.


3. outBigramsStat()
학습한 bigram LM의 통계를 형식에 맞게 출력
프로그램의 출력엔 다음과 같은 정보들을 포함한다.
(1) 사용된 bigram의 총 개수
(2) bigram별 사용회수를 내림차순으로 정렬하여 상위 1%를 출력


4. outShannonVisualization()
학습한 bigram LM을 평가하기 위해 Shannon Visualization 결과를 출력
<s>부터 시작하여 학습한 bigram 내에서 가장 빈도가 높은 bigram들을 선택하여 다음 단어를 선택하고 최종단어르 </s>가 선택될 때까지 이를 반복한다.
이 함수를 통해 얻은 Shannon Visualization 결과는 선택한 소설책을 대표하는 문장이라고 생각할 수 있다. (Little_Lord_Fauntleroy.txt의 Shannon Visualization : He had been a little boy and the earl)
