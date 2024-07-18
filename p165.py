#while문
# while 조건식 :
#     참이면 수행하는 문장
# 조건식이 거짓이면 처리
# 또는 조건식 다음으로 처리


#1~10까지 합계 구하기
# i=1
# sum=0
# while i<=10 :
#     sum=sum+i
#     i=i+1
# print("합계는 %d" %sum)

# #500~600까지의 정수 중 5의 배수 합계를 구하는 프로그램
# i=500
# sum=0
# while i<=600 :
#     if i%5==0 :
#         sum=sum+i
#     i=i+1
# print("합계는 %d이다" %sum)

# print("-"*20)
# #1~1000까지 정수 중 100의 배수를 제외하고 합계를 구하기
# i=1
# sum=0
# while i<=1000 :
#     if i%100 != 0 :
#         sum=sum+i
#     i=i+1
# print("합계는 %d이다" %sum)

# print("-"*50)

#예제 4-14
# s="Python is widely used by a number of big companies"
# i=0
# count=0
# print("문자열의 길이는 %d" %len(s))
# print("모음:", end=" ")

# while i <=len(s)-1 :
#     if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U' :
#        count=count+1
#        print(s[i], end=" ")
#     i=i+1

# print()
# print("모음 개수 : %d" %count)

# #숫자 2개를 입력 받아서 덧셈하기
# yN = "y"
# while yN=="y" :
#     num1 = int(input("숫자1 ? "))
#     num2 = int(input("숫자2 ? "))
#     sum = num1+num2
#     print("합계는 %d" %sum)
#     yN = input("계속 하시겠습니까? (y:계속, n:그만)")

#문자열 2개 입력 받아서 합치기
#문자1: Hello / 문자2: Love
#출력 결과: H L e o l v l e o
#계속하시겠습니까? (y/n)
#전체 반복횟수 = 문자 1의 길이 (5글자) + 문자2의 길이(4글자)
# yN="y"
# while(yN=="y") :
#     w=input("문자 1 :")
#     s=input("문자 2 :")
#     ws=""
#     for i in range(len(w)+len(s)) :  #0,1,2,...,8
#         if i <= len(w)-1 : #i<=4 0,1,2,3,4
#             ws = ws + w[i]
#         if i <= len(s)-1 :   #i<=3 0,1,2,3
#             ws = ws + s[i]
#     print(ws)
#     yN=input("계속하실래요? (y/n)")


while True : 
    w=input("문자 1 :")
    s=input("문자 2 :")
    ws=""
    for i in range(len(w)+len(s)) :  #0,1,2,...,8
        if i <= len(w)-1 : #i<=4 0,1,2,3,4
            ws = ws + w[i]
        if i <= len(s)-1 :   #i<=3 0,1,2,3
            ws = ws + s[i]
    print(ws)
    yN=input("계속하실래요? (y/n)")
    if yN=='n' :
        break