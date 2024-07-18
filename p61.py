score=80
print( '성적 : '+ str(score) )

x='토끼'*10     #토끼가 10번 반복됨 = 반복연산자
print(x)

n=100*10     #연산이 됨
print(n)

n100='100' * 20    #100이 20번 반복됨
print(n100)

#200숫자를 15번 반복해서 출력하기
n200 = 200
print( str(n200) * 15 )

#64쪽 퀴즈
#1
x= "수학 성적 : "
print ( type(x) )
y=80
print ( type(y) )
z=x+str(y)
print(type(z))

#2
date = "20220301"
year = date[0:4]
month = date[4:6]
day = date[6:]
date2 = year + "-" + month + "-" + day
print(date2)


print(len(date))

# 자기 이름을 핸드폰번호 마지막자리의 갯수만큼 반복하기
name = '김수민'        #이름을 변수로 등록
num = '010-3288-0958' #번호를 변수로 등록
lastNumber = num[-1]  #마지막 자리의 번호를 변수로 등록
print ( name * int(lastNumber) )  #이름 변수와 마지막 자리 번호 변수를 반복

phone1 = '82-10-8744-3334'  #15글자면 한국 핸드폰번호 / 15글자가 아니면 한국 집번호
phone2 = '82-02-123-4567'
#결과 : phone1은 한국 핸드폰번호입니다.
#결과 : phone2은 한국 집번호입니다.
'''
if len(phone1)==15 :
    print('phone1은 한국 핸드폰번호입니다.')
else :
    print ('phone1은 한국 집번호입니다.')
if len(phone2)==15 :
    print('phone2은 한국 핸드폰번호입니다.')
else :
    print ('phone2은 한국 집번호입니다.')
'''
