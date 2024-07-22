list1 = [3,15,-12.5,'사과','딸기',True, False]
print(list1)
list2=list(range(1,21,2))
print(list2)

print(list1[4])
for i in range(7) :
    print (list1[i],end=" ")
print()
print('-'*50)
print(list2[-1: :2])

#응용문제 100 110 120 ... 200 리스트를 만들어 보기
list3=list(range(100,201,10))
print(list3)

cnt=0
for i in list3:
    cnt=cnt+1
print("리스트의 갯수는 %d" %cnt)

print(len(list3))

sum=0
for i in list3:
    sum=sum+i
print("리스트의 합계는 %d" %sum)

#185p
colors=["빨간색", "파란색", "노란색", "검정색", "초록색"]
for color in colors :
    print("나는 %s을 좋아한다" %color)

n=len(colors)
for i in range(0,n) :
    print("나는 %s을 좋아한다" %colors[i])

print('-'*50)

animal = ['코', '호', '사', '펭', '여']
i=0
while i<len(animal) :
    print(animal[len(animal)-1-i])
    i=i+1

# 성적 프로그램 작성하기
list1=['홍길동', 100, 80]
list2=['이순신', 90, 75]
list3=['최경미', 75, 100]
list4=['박경수', 85, 90]

print("이름  국어점수  수학점수  합계  평균")
print(list1[0], list1[1], list1[2], list1[1]+list1[2], (list1[1]+list1[2])/2)
print(list2[0], list2[1], list2[2], list2[1]+list1[2], (list2[1]+list2[2])/2)

#우리 반 이름: 홍길동, 이순신, 최경미
print("우리 반 이름: ", list1[0], ",", list2[0], ", ", list3[0])

#우리 반 국어점수 합계, 영어점수 합계 구하기
print("우리 반 국어점수 합계 : %s" %(list1[1]+list2[1]+list3[1]))
print("우리 반 영어점수 합계 : %s" %(list1[2]+list2[2]+list3[2]))

if list3[1] < list1[1] and list2[1] < list1[1] :   #list1이 젤 큰 경우
    topKorName = list1
elif list3[1] < list1[1] and list2[1] < list2[1] :   #list2이 젤 큰 경우
   topKorName = list2 
else :                                               #list3이 젤 큰 경우
    topKorName = list3
print("우리 반에서 국어점수 제일 잘 본사람의 이름은? %s" %topKorName[0])

#찾고 싶은 사람은? 박경수
#우리 반에 박경수가 없어요

#찾고 싶은 사람은? 이순신
#우리 반에 이순신이 있어요
x=input("찾고 싶은 사람은? : ")
if list1[0]==x or list2[0]==x or list3[0]==x :
    print("우리 반에 %s가 있어요" %x)
else :
    print("우리 반에 %s가 없어요" %x)