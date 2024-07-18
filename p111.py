#117p
# char=input("영문 소문자 하나를 입력하세요 : ")
# if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" :
#     print("%s은(는) 모음이다." %char)
# else :
#     print("%s은(는) 자음이다." %char)

# # #코딩연습 C3-1
# start=int(input("시작 수는?"))
# end=int(input("끝 수는?"))
# num=int(input("정수를 입력하세요 :"))

# result = "%d은(는) %d~%d 사이에 없다." %(num, start, end)

# if (start<num) and (num<end) :
#     print("%d은(는) %d~%d 사이에 있다." %(num, start, end))
# else :
#     print(result)

# #코딩연습 C3-2
# month=input("월을 숫자로 입력하세요 : ")
# if month=="3" or month=="4" or month=="5" :
#     print("%s월은 봄입니다." %month)
# if month=="6" or month=="7" or month=="8" : 
#     print("%s월은 여름입니다." %month)
# if month=="9" or month=="10" or month=="11" :
#     print("%s월은 가을입니다." %month)
# if month=="12" or month=="1" or month=="2" :
#     print("%s월은 겨울입니다." %month)

# #코딩연습 C3-3 
# a=input("주민번호 뒷자리 첫 번째 숫자를 입력해 주세요 : ")
# if a=="1" or a=="3" :
#     print("남성입니다!")
# if a=="2" or a== "4" :
#     print("여성입니다!")

#코딩연습 C3-4
# a="apple"
# b=a.upper()
# print(b)
# char=input("영어 대문자 또는 소문자 하나를 입력하세요 : ")
# char2=char.upper()

# if char2=="A" or char2=="E" or char2=="I" or char2=="O" or char2=="U" :
#     print("%s->모음" %char)
# else :
#     print("%s->자음" %char)

#코딩연습 C3-5
# h=int(input("키는?"))
# w=int(input("몸무게는?"))
# s=(h-100)*0.9
# print("="*50)
# print("키:", h)
# print("몸무게:", w)

# if w>h :
#     print ("건강을 위해 다이어트가 필요합니다!")
# else :
#     print ("표준 또는 마른 체형입니다!")

#코딩연습 C3-6
# print("아르바이트 급여 계산 프로그램")
# print("※시급")
# print("- 주간 근무 : 9,500원 ")
# print("- 야간 근무 : 주간 시급 * 1.5")

# hour_pay=9500

# work=int(input("1(주간근무) 또는 2(야간근무)를 입력해주세요 : "))
# time=int(input("근무 시간을 입력해주세요 : "))

# if work==1 :
#     daynight="주간"
#     pay=hour_pay * time
# else :
#     daynight = "야간"
#     pay=hour_pay * 1.5 * time

# print ("%d시간동안 일한 %d급여는 %.0f입니다." %(time, daynight, pay))

#예제3-8
# score=int(input("점수는?"))

# if score>=90 :
#     grade="A"
# elif score>=80 :
#     grade="B"
# elif score >=70 :
#     grade="C"
# elif score >=60 :
#     grade="D"
# else :
#     grade="F"

# print("등급:", grade)


#예제 3-9
# print("기능 선택")
# print("1. 더하기")
# print("2. 빼기")
# print("3. 곱하기")
# print("4. 나누기")
# print()

# s=input("계산기 기능을 선택하세요(1/2/3/4): ")

# num1 =int(input("첫 번째 숫자를 입력하세요: "))
# num2 =int(input("두 번째 숫자를 입력하세요: "))

# if s=="1":
#     print("%d+%d=%d"%(num1, num2, num1+num2))
# elif s=="2":
#     print("%d-%d=%d" %(num1, num2, num1-num2))
# elif s=="3":
#     print("%dx%d=%d" %(num1, num2, num1*num2))
# elif s=="4":
#     print("%d/%d=%d" %(num1, num2, num1/num2))
# else :
#     print("입력 숫자가 잘못되었습니다!")
