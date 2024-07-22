def func(n):
    x=n+5
    return x

r=func(100)
print(r)

#함수정의
def inch_to_cm(inch) :
    cm=[]
    for i in range(inch,31,10) :
        k=i*2.54
        cm.append(k)
    return cm

#함수 호출
result=inch_to_cm(10)
print(result)

 #5*4*3*2*1=120 프로그램 만들기
def p(n) :
    result=[]
    answer=1
    for i in range(n,0,-1) :
        answer=answer*i
    result.append(answer)
    answer=0
    for i in range(1,n+1) :
        answer=answer+i
    result.append(answer)
    answer=0
    for i in range(1,n+1) :
        answer=answer+i
    result.append(answer)
    return answer
print(p(5))