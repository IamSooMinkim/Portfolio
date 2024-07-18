#코딩 연습 C4-5
# 입력받기 '477569040'
# 입력받은 숫자를 1개씩 가져다가 '4'
# 문자를 숫자로 변경한다. '4'-->4
# 홀수인지 판단한다. 5%2==1
# 갯수 세기 cnt=cnt+1

# number = input("숫자를 입력하세요 : ")
# cnt=0
# for i in number :
#     nVal=int(i)
#     if nVal%2==1 :
#         cnt=cnt+1
# print("홀수의 개수 : %d개" %cnt)


#10 20 30 ... 100을 출력하기
# for i in range(10,101,10) :
#     print(i, end=" ")

# for k in range(5) :
#     print()
#     for i in range(10,101,10) :
#         print(i, end=" ")

#1 2 3 4 5 을 10줄 출력하기
# for k in range(10) :
#     print()
#     for i in range(1,6,1) :
#         print(i, end=" ")


# 1 2 3 4 5 -> 2 3 4 5 6 출력하기
for k in range(1) :
    for i in range(1,6,1) :
        print(i, end=" ")
    print()
    for i in range(2,7,1) :
        print(i, end=" ")
    print()
    for i in range(3,8,1) :
        print(i, end=" ")
    print()
    for i in range(4,9,1) :
        print(i, end=" ")
    print()
    for i in range(5,10,1) :
        print(i, end=" ")
    print()
print("-"*10)

for k in range(5) :
    for i in range(k+1,k+6,1) :
        print(i, end=" ")
    print()

print("-"*10)

for k in range(5) :
    for i in range(1,6-k,1) :
        print(i, end=" ")
    print()

for i in range(5) :
    for x in range(1,6) :
        print(x+i, end=' ')
    print()

print("-"*10)

for j in range(5) :
    k=6-j
    for i in range(1,k) :
        print(i, end=" ")
    print()
    

#추가로 내용을 넣었다
