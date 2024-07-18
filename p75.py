#75
'''
year=2024
month=7
day=12
print(year,month,day,sep="/")

hp1="010"
hp2="1234"
hp3="5678"
print(hp1, hp2, hp3, sep = "-")

price=1000
print(price, "원")
print(price, "원", sep = "")
'''

'''
print("안녕하세요\n반갑습니다")
print("안녕하세요\t반갑습니다")
print("안녕하세요\\반갑습니다")
print("안녕하세요\'반갑습니다")
print("안녕하세요\"반갑습니다")
#'안녕'
print("\'안녕\'")
#"안녕"
print('\"안녕\"')
'''

'''
#80 Quiz
kor=input("국어 성적을 입력하세요: ")
eng=input("영어 성적을 입력하세요: ")
math=input("수학 성적을 입력하세요: ")
sum=int(kor)+int(eng)+int(math)
avg=sum/3
print("합계:%d, 평균:%.2f"%(sum,avg))
'''
'''
#p86 C2-1
year=input("년은?")
month=input("월은?")
day=input("일은?")
print(year, month, day, sep=".")
'''

#C2-2
width=int(input("사각형의 너비는?"))
height=int(input("사각형의 높이는?"))
round=2*width+2*height
print(round)
area=width*height
print(area)
print("면적: %dcm2" %area)

'''
#C2-3
r=float(input("반지름을 입력하세요 : "))
length=2*r*3.14
area=r*r*3.14

print("반지름:%.2fcm"%r)
print("원의 둘레:%.2fcm" %length)
print("원의 면적:%.2fcm2"%area)
'''
'''
#C2-4
inch=float(input("인치는?"))
cm=print(int(inch)*2.54)
print("%.1fcm"(inch,cm))
모르겠다...


#C2-5
#결제 금액 : 책값-(책값*(할인율/100))+배송료

#C2-5
#결제 금액 : 책값-(책값*(할인율/100))+배송료

price=int(input("책 값은?"))
discount=int(input("할인율은?"))
delivery=int(input("배송료는?"))

pay=int( price-(price+(discount/100))+delivery )
print(int(pay))
'''
