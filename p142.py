# for x in range(5) :
#     print(x)
#     print("Hello")
# print ("반복문 끝")

# sum = 0
# for i in range(0,11,2) :
#     sum=sum+i
#     print("i의 값 : %d => 합계: %d" %(i,sum))

# #에제4-4
# for i in range(10) :
#     print(i, end=" ")
# print()

# for i in range(1,11) :
#     print(i, end="")
# print()

# for i in range(1,10,2) :
#     print(i, end=" ")
# print()

# for i in range (20,0,-2) :
#     print(i, end=" ")
# print()

#149p
#5 10 15 20 ...100 까지 나오기
cnt=0
for i in range(5,101,5) :
    print (i, end= " ")
    cnt=cnt+1
print()
print("갯수:%d개" %cnt)

#4 8 12 16 ... 200 가지 나오기
cnt=0
for i in range(4,201,4) :
    print(i, end=" ")
    cnt=cnt+1
print()
print("갯수:%d개" %cnt)

#200 150 100 50 0 -50 -100 -150 -200
cnt=0
for i in range(200,-201,-50) :
    print(i, end=" ")
    cnt=cnt+1
print()
print("갯수:%d개" %cnt)
