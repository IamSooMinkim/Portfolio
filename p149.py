#20 22 24 26 ... 50
#합계구하기 -> sum=0, sum=sum+1 추가
cnt=0
sum=0
for i in range (20,51,2) :
    print (i, end=" ")
    cnt=cnt+1
    sum=sum+i
print()
print("20~50까지의 2개씩 증가 숫자 갯수는 %d 이다." %cnt)
print("20~50까지의 2개씩 증가 숫자 갯수의 합계는? %d이다." %sum)

#100 95 90 ... 0
cnt=0
sum=0
for i in range(100,-1,-5) :
    print(i, end=" ")
    cnt=cnt+1
    sum=sum+i
print()
print("100~0까지의 -5개씩 감소 숫자 갯수 %d" %cnt)
print("100~0까지의 -5개씩 감소 숫자의 합계 %d" %sum)
print("100~0까지의 -5개씩 감소 숫자의 평균 %.0f" %(sum//cnt))

print()
# 1~100까지 숫자의 합을 구하되 400이 넘으면 멈추기
sum=0
for i in range (1,101,1) :
    if sum >= 400 :
        print("합계가 400이 넘는 순간 i값은 %d" %i)
        break
    sum=sum+i
print()
print("1~100까지의 합계 : %d" %sum)

print()
#200~500까지 3개 증가하는 수를 출력하기
#갯수가 20개일때 멈추기
cnt=0
for i in range(200,501,3) :
    print(i, end=" ")
    cnt=cnt+1
    if cnt==20 :
        break
print(i)
print("%d개일 때 i값 %d" %(cnt,i))



print()

# 5~500까지 5의 배수를 출력하기
# 합계가 1000이상이거나 갯수가 30개 이상이면 멈추기
cnt=0
sum=0
for i in range (5,501,5) :
    print(i, end=" ")
    cnt=cnt+1
    sum=sum+i
    if 30<=cnt or 1000<=sum :
        break

print()
print("합계가 1000이상인 합계값은 : %d" %sum)
print("갯수가 30개 이상인 갯수값은 : %d" %cnt)
print("합계가 1000이상이거나 갯수가 30개 이상이면 멈춘 값: %d" %i)

#예제 4-6
sum=0
for i in range(100, 2011) :
    if i%5==0 :
        sum=sum+i
print("5의 배수의 합계 : %d" %sum)