#E3-6
# num =int(input("수를 입력하세요: "))

# if num<10 :
#     print ("%d은(는) 한 자리 숫자이다." %num)
# else :
#     print ("%d은(는) 한 자리 숫자가 아니다." %num)

# num2 =int(input("수를 입력하세요: ")) 
# if 99<num2<1000 :
#     print ("%d은(는) 세 자리 숫자이다." %num2)
# else :
#     print ("%d은(는) 세 자리 숫자가 아니다." %num2)

# num3 =int(input("수를 입력하세요: ")) 
# if 1000<num3 :
#     print("오류! %d은(는) 범위(0~999) 이외의 숫자이다." %num3)

# #다른 방법
# number=input("수를 입력하세요 : ")
# inputLength = len(number)
# if inputLength == 1 :
#     print ("%s은(는) 한자리 숫자이다" %number)
# elif inputLength == 2 :
#     print ("%s은(는) 두자리 숫자이다" %number)
# elif inputLength == 3 :
#     print ("%s은(는) 세자리 숫자이다" %number)
# elif not(0<=inputLength<=999) :
#     print("오류! %s는 범위 0~999 이외의 숫자이다." %number)

#E3-8
# num1 = int(input("첫 번째 숫자를 입력하세요 : "))
# num2 = int(input("두 번째 숫자를 입력하세요 : "))
# print("원하는 연산은?")
# operater = input("+, -, *, / 중 하나를 선택하세요 : ")

# if not (operater == '+' or operater == '-' or operater == '*' or operater == '/') :
#     print("선택 오류!")
# elif operater == '+' :
#     print("%d+%d=%d" %(num1,num2,num1+num2))
# elif operater == '-' :
#     print("%d-%d=%d" %(num1,num2,num1-num2))
# elif operater == '*' :
#     print("%d*%d=%d" %(num1,num2,num1*num2))
# elif operater == '/' :
#     print("%d/%d=%d" %(num1,num2,num1/num2))

#139p S3-2
hour1 = int(input("첫 번째 시간의 시를 입력하세요 : "))
minute1 = int(input("첫 번째 시간의 분을 입력하세요 : "))
hour2 = int(input("두 번째 시간의 시를 입력하세요 : "))
minute2 = int(input("두 번째 시간의 분을 입력하세요 : "))

#잘못 입력한 부분을 오류 검출
#조건문을 써서 빠른 시간을 출력
if not(0<=hour1<=24 or 0<=hour2<=24 or 0<=minute1<=59 or 0<=minute2<=59) :
    print("시간과 분을 잘못 입력하셨어요")
elif hour1 < hour2 :
    print("- 빠른 시간 : %d:%d" %(hour1,minute1))
    print("- 느린 시간 : %d:%d" %(hour2,minute2))
elif hour1==hour2 and minute1 < minute2 :
    print("- 빠른 시간 : %d:%d" %(hour1,minute1))
    print("- 느린 시간 : %d:%d" %(hour2,minute2))
elif hour1 == hour2 and minute1 > minute2 :
    print("- 빠른 시간 : %d:%d" %(hour2,minute2))
    print("- 느린 시간 : %d:%d" %(hour1,minute1))
else : 
    print("- 빠른 시간 : %d:%d" %(hour2,minute2))
    print("- 느린 시간 : %d:%d" %(hour1,minute1))