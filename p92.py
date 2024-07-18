
#E2-1 두 개의 변수를 이용하여 10과 20의 합을 구하는 프로그램을 작성하시오.
x=10
y=20
z=x+y
print("두 수의 합 :",z)

#E2-2 1번 문제의 실행 결과를 문자열 포맷팅을 이용하여 실행 결과와 같이 출력하는 프로그램을 작성하시오.
x=10
y=20
z=x+y
print("%d+%d=%d"%(x,y,z))

#E2-3
x=10
y=20
z=x+y
print(str(x)+"+"+str(y)+"="+str(z))

#E2-4
a=input("첫 번째 과일을 입력하세요 :")
b=input("두 번째 과일을 입력하세요 :")
print(a,"와(과)",b,"은(는)내가 좋아하는 과일이다.")

#E2-5
a=input("첫 번째 과일을 입력하세요:")
b=input("두 번째 과일을 입력하세요:")
print(a,"와(과)", b, "은(는)내가 좋아하는 과일이다.", sep="")

#E2-6
a=input("첫 번째 과일을 입력하세요:")
b=input("두 번째 과일을 입력하세요:")
print("%s와(과) %s은(는) 내가 좋아하는 과일이다." %(a,b))

#E2-7
a=int(input("첫 번째 숫자를 입력하세요 : "))
b=int(input("두 번째 숫자를 입력하세요 : "))
c=a/b
print("%d/%d=%f" %(a,b,c))

#E2-8
a=int(input("첫 번째 숫자를 입력하세요 : "))
b=int(input("두 번째 숫자를 입력하세요 : "))
c=a/b
print("%d/%d=%.2f" %(a,b,c))

#E2-9
email1=input("이메일 주소 앞 부분은?")
email2=input("이메일 도메인 이름은?")
email=email1+"@"+email2
print("-이메일 주소 :",  email)

#E2-10
name=input("이름을 입력하세요 :")
address=input("주소를 입력하세요 :")
phone=input("전화번호를 입력하세요 :")
print("-이름 :",name)
print("-주소 :",address)
print("-전화번호 :",phone)

#E2-11   #사다리꼴 면적:(윗변 길이+밑변길이)*높이/2
up=int(input("윗변의 길이는?"))
down=int(input("밑변의 길이는?"))
high=int(input("높이는?"))
area=(up+down)*high/2
print("- 사다리꼴의 면적 : %.1f" %area)

#E2-12
a="가는 말이 고와야 오는 말이 곱다."
print(a)
print("- 추출 문자 :", a[10:14])

#E2-13
num=input("열 자리의 숫자를 입력하세요 :")
print("- 추출된 두 숫자 :", num[-2:])

#S2-1 심화문제
kg=int(input("변환할 킬로그램(kg)은?"))

pound=kg*2.204623
ounce=kg*35.273962

print("-"*50)
print("킬로그램       파운드        온스")
print("-"*50)
print("%d            %.2f      %.2f" %(kg, pound, ounce))
print("-"*50)

#S2-2 심화문제
phone1=input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")
#010-3288-0958
phone2=phone1[0:3]+phone1[4:8]+phone1[9:]
print("-입력된 휴대폰 번호 : %s" %phone1)
print("-하이픈 삭제된 휴대폰 번호 : %s" %phone2)