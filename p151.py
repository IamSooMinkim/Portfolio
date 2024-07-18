#예제 4-8
for i in range(5) :
    phone=input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요 : ")
    for x in phone :
        if x !="-" :
            print("%s"%x, end="")
    print()

#핸드폰 데이터안에 숫자말고 다른 문자가 섞여 있다면 / 예)!!909--++ㅁㅁㅁ888232423 / 요구사항: 숫자만 정제시키세요

hp=input("핸드폰 번호를 입력해주세요")
for i in hp :
    if not('a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'):
        print("%s"%i, end="")

hp2=input("핸드폰 번호를 입력해주세요")
for i in hp2 :
    if ('가'<=i<='힣'):
        print("%s"%i, end="")

#152p
print("-"*30)
print("  섭씨   화씨")
print("-"*30)

for c in range(-20, 31, 5) :
    f = c*9.0/5.0+32.0
    print("%5d %6.1f" % (c,f))

print("-"*30)

#154p C4-1
count=0
for i in range(200,801) :
    if not(i%5==0) :
        print("%d" %i, end="")
        count=count+1

if (count%10==0) :
    print()

#C4-2
print("-"*40)
print("  cm    mm    m    inch")
print("-"*40)

for cm in range(1,101,1) :
    mm=cm*10.0
    m=cm*0.01
    inch=cm*0.3937
    print("%4d %6.0d %5.2d %8.1d" %(cm, mm, m, inch))

print("-"*40)