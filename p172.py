#1~200 출력하기
#for문
for i in range(1,201,1) :
    if i==100 :
        continue
    print(i, end=" ")
print()
print("-"*100)

#while문
i=1
while i<=200 :
    if i==100 :
        continue
    print(i,end=" ")
print()
print("-"*100)

#100이면 멈추기
for i in range(1,201,1) :
    print(i, end=" ")
    if i==100 :
        break
print()
print("-"*100)

#100이면 찍지 않고 건너 뛰어서 101 찍기 (반복문은 계속) #continue
