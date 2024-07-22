def average(*args) :
    print(len(args))

#비지니스로직 부분(실제 코드 수행 부분) 함수 호출
average(85,96,87)
average(77,93,85,97,72)



def func(food) :
    for x in food :
        print(x, end=" ")

fruits=['사과', '오렌지', '바나나']
func(fruits)


#예제 7-9
def func(food) :
    food.append("딸기")
    food.append("수박")
fruits=['사과', '오렌지', '바나나']

print(fruits)
func(fruits)
print(fruits)

#코딩연습 C7-1
def add(a,b) :
    c=a+b
    print("%d+%d=%d" %(a,b,c))

add(12,15)
add(245,300)
add(-38,-12)

#코딩연습 C7-2
def sum_int(start,end) :
    total=0
    for i in range(start,end+1) :
        total = total+i
    print("%d ~ %d 정수 합계 : %d" %(start,end,total))

sum_int(20,50)
sum_int(600,800)

#코딩연습 C7-3
def member_join(*args):
    result=""
    for arg in args :
        result=result+arg+" "
    print("가입 회원:", result) 
member_join("김정연", "안서영")
member_join("황선형", "김철영", "이창연")
member_join("정수진", "김보람", "정수연", "함소영")

#코딩 연습 C7-4
못했어요