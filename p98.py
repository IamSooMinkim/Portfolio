# x=-10
# if x>0:
#     print("양수")
#     print("조건이 참일때 수행")
# print("조건문 배워요")

# y=80
# if y>=90:
#     print("A+")
# else :
#     print("낮은 점수")
# print("모두 실행되는 곳")

# a=8
# b=10
# if a>= b :
#     print("a가 더 크다")
# else :
#     print("b가 더 크다")
# print("판단 끝")

# jumsu=74
# if jumsu>=90 :
#     print("A")
# elif jumsu>=80 :
#     print("B")
# elif jumsu>=70 :
#     print("C")
# elif jumsu>=60 :
#     print("D")
# else :
#     print("F")

#103p
# score1=75
# score2=90
# print(score1>=80 and score2>=80)
# print(score1>=80 or score2>=80)

# x=10
# print(x%2==0 or x%6==0)
# print(not(x != 10))

# #105p quiz
# a=5
# b=7
# c=a+b
# print(c==12)

# hobby1="영화감상"
# hobby2="수영"
# my_hobby="독서"
# print(my_hobby==hobby1 or my_hobby==hobby2)

# pilgi=90
# silgi=70
# print(pilgi>=80 and silgi>=80)

#예제 3-2
age=int(input("나이는?"))
ticket = 2000

if age >= 65 :
    ticket=0
elif 10<=age<=20 :
    ticket=1500
elif 5<=age<=9 :
    ticket=1200
elif 0<=age<=4 :
    ticket=1000

print("나이:%d세"%age)
print("입장료:%d원"%ticket)