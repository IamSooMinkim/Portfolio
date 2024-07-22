
# def hello() :
#     print('hello')
    
# for i in range(20) :
#     hello()

#1~100까지 합계 구하는 함수 정의하기
def uSum(uStart,uFinish) :
    sum=0
    for i in range(uStart,uFinish+1) :
        sum=sum+i
    print(sum)

'''
#만들어진 함수를 사용하는 쪽-비지니스로직
uSum() #함수호출 

def lineUp() :
    print('-'*70)
lineUp()

#합계가 3000이 넘는 순간 멈추기
def s3000(n) :
    sum=0
    for i in range(1,101) :
        if sum>=n :
            break
        sum=sum+i
    #합계, i 값 출력하기
    print("%d이상일 때의 %d값, 합계: %s" %(n, i, sum))
s3000(3000)

lineUp()
#합계가 4000이 넘는 순간 멈추기
s3000(4000) '''


#요구사항 입력 2개 받는다
#시작수? 50
#끝수? 200
#50~200까지 합 출력하기

startN=int(input("시작수? "))
finishN=int(input("끝 수? "))
sum=0
uSum(startN,finishN)