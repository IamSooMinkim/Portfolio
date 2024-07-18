'''name = input("이름은")
print(name)'''

'''age = input("당신의 나이는?")
print("당신의 나이는 %s살입니다"%age)
print("당신의 나이는 %d살입니다"%int(age))'''

'''year = input("당신이 태어난 년도가 언제입니까?")
age = input(str(2024-2005) + "입니다")
print("%d"%age)'''

'''#p73 quiz
a=input("첫 번째 정수를 입력하세요: ")
print("12")
b=input("두 번째 정수를 입력하세요: ")
print("15")
c=a+b
print(c)

#2번문제
a=input("첫 번째 정수를 입력하세요: ")
print("10")
b=input("두 번째 정수를 입력하세요: ")
print("20")
c=int(a)+int(b)
print(c)'''

'''
#심화문제
aVal = int(input("첫 번째 정수를 입력하세요: "))
bVal = int(input("두 번째 정수를 입력하세요: "))
if aVal > bVal :
    print(input(aVal))
    '''


a = int(input("첫 번째 숫자는?"))
b = int(input("두 번째 숫자는?"))
c = int(input("세 번째 숫자는?"))
if c<a<b or a<c<b : #a>b, a>c
    print(b)
elif c<b<a or b<c<a :
    print(a)
elif a<b<c or b<a<c :
    print(c)

