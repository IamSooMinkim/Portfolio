#108p
# #배수 교재 실습
# num=int(input("양의 정수를 입력하세요 : "))
# result="3의 배수도 4의 배수도 아니다"

# if num%3==0 :
#     reslt="3의 배수이다."
# if num%4==0 :
#     result="4의 배수이다."
# if num%3==0 and num%4 == 0 :
#     result="3의 배수이면서 4의 배수이다."

# print("%d은(는) %s" %(num, result))

#응용문제 / 숫자를 입력 받아서 "짝수이고 4의 배수"인 숫자이면 "행운의 수"라고 출력해주세요.
#아니라면 입력 받은 수를 출력해주세요.
#예1 4입력하면 "행운의 수"라고 출력
#예2 8입력하면 "행운의 수"라고 출력
#예3 3입력하면 3이라고 출력

# number=int(input("숫자를 입력하세요 : "))
# result="%d" %number

# if number%2==0 :
#     result="짝수이다"
# if number%4==0 :
#     result="4의 배수이다"
# if number%2==0 and number%4==0 :
#     result="행운의 수"
# else :
#     result=number

# print (result)

#예제 3-4
ans1=input("'사자'의 영어 단어는 무엇일까요? : ")
result="땡! 틀렸습니다."
if ans1=="lion" :
    result="딩동댕! 참 잘했어요~~~"
print (result)

ans2=input("'오렌지'의 영어 단어는 무엇일까요? : ")
result="땡! 틀렸습니다."
if ans2=="orange" :
    result="딩동댕! 참 잘했어요~~~"
print (result)

ans3=input("'기차'의 영어 단어는 무엇일까요? : ")
result="땡! 틀렸습니다."
if ans2=="train" :
    result="딩동댕! 참 잘했어요~~~"
print (result)