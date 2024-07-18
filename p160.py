#예제 4-10
a=2
for b in range(1,10) :
    print("%dx%d=%d" %(a,b,a*b))

print("-" * 30)
for a in range(2,10) :
    for b in range(1,10) :
        print ("%dx%d=%d" %(a,b,a*b))
print("-"*30)

#코딩연습 C4-7
for i in range(5) :
    for j in range(10) :
        print("*", end=" ")
    print()

#코딩연습 C4-8
for i in range(9,0,-1) :
    for j in range(i) :
        print(i, end=" ")
    print()

#C4-8 반대로
for i in range(1,10,1) :
    for j in range(i) :
        print(i, end=" ")
    print()