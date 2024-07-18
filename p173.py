# # C4-9
# n=1
# sum=0
# count=0
# while n<=100 :
#     if n%2==1 :
#         sum=sum+n
#         print("%6d" %sum,end="")
#         count=count+1
#     if count%10==0 :
#         print()

#     n=n+1

# # C4-10
# print("-"*30)
# print("   달러    원화     유로")
# print("-"*30)

# dollar=10
# while dollar<=100 :
#     won=dollar*10800
#     euro=dollar*0.81
#     print("%7d %8.0f %7.1f" %(dollar, won, euro))
#     dollar=dollar+10
# print("-"*30)

# # C4-11
# sentence=input("문장을 입력해주세요: ")
# i=len(sentence)-1
# while i>=0 :
#     if sentence[i]==" " :
#         print("-", end="")
#     else :
#         print("%s" %sentence[i], end="")
#     i=i-1

# p177 연습문제 
# for i in range(1,10,2) :
#     print(i)

# #4-2
# sum=0
# for i in range(1,101,1) :
#     if i%3==0 :
#         sum=sum+i
# print()
# print("1~100까지의 3의 배수 합계 : %d" %sum)

# #4-3
# #for문을 이용하여 1~100까지의 수 중에서 5의 배수를 출력하는 프로그램을 작성하시오
# sum=0
# for i in range(1,101) :
#     if i%5==0 :
#         print(i, end=" ")

#4-4
# cnt=0
# for i in range(1,101) :
#     if i%5==0 :
#         print(i, end=" ")
#         cnt=cnt+1
# if cnt%5==0 :
#     print()

print("="*70)
#구구단
for i in range(1,10) :
    for j in range(2,10) :
        print("%3dx%3d=%3d" %(j,i,j*i), end=" ")
    print()

print("="*70)
for i in range(2,10) :
    for j in range(1,10) :
        print("%3dx%3d=%3d" %(i,j,j*i), end=" ")
    print()

print("="*70)
#소수 구하기 (179p 3번 문제)
#소수는 1과 자기 자신 외에는 나누어 떨어지지 않는 수
start=int(input("시작 수를 입력해주세요 : "))
end=int(input("끝 수를 입력해주세요 : "))
for x in range(start, end+1) :
    for i in range(2,x) :
        if x%i==0 :
            break
        if x==i+1 :
            print("%d는 소수이다" %x)