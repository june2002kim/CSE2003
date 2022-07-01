#사전
fruit={'배':[2,1000],'자몽':[1,2000],'메론':[1,8000],'감':[6,800]}
result=0

a=input("먹고 싶은 과일은? : ")
if a in fruit:
    print(f"{a} 맛있게 드세요")
    fruit[a][0]-=1
else:
    print(f"{a} 준비되어 있지 않습니다")

for i in fruit.keys():
    if fruit[i][0]<5:
        result+=fruit[i][1]*(5-fruit[i][0])
    
print("\n각 과일당 최소 5개는 되도록 구입합니다")
print(f"구입에 필요한 총 금액은 : {result} 원 입니다")
