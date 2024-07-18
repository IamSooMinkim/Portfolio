#키보드 이름을 입력 받아 보세요
name=input("이름은?")
#이름을 화면 출력하기
print("입력한 이름은 %s입니다." %name)
#키보드로 점수를 입력 받아 보세요
pointScore=input("포인트 점수를 입력하세요 : ")
print("포인트 점수는? %s" %pointScore)

#포인트 점수의 20%는 600점입니다. 출력
pointScore=input("포인트 점수를 입력하세요 : ")
print("포인트 점수는? %d" %pointScore)
#1단계: 문자형을 숫자형으로 변환 필요
#2단계 계산하기 *0.2
#3단계 출력하기
pointValue=int(pointScore)
point20Per=pointValue*0.2
print("포인트 점수의 20%는 %d점입니다." %point20Per)
print("포인트 점수의 20%", "는 %d점입니다"%point20Per,sep="")

#당신의 주소는? 강동구 강일동
address=input("당신의 주소는?")
print(address*10)
#몇 번 반복할래요? 5번
x=input("몇 번 반복할래요?")
print(address*int(x))
#출력 당신의 주소의 글자는 7글자입니다.
s=len(address)
print("당신의 주소의 글자는 %d입니다." %s)