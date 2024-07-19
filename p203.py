# 정렬
data = [12,8,15,32,-3,-20,15,34,6]
print(data)
data.sort()
print(data)

data2 = ['a', '가', '@', '1', 'bc']
print(data2)
data2.sort()
print(data2)
data2.sort(reverse=True)
print(data2)
data2.sort(reverse=False)
print(data2)

#205
string1=["사과는 맛있다. 나는 사과를 제일 좋아한다."]
print(string1)

x=string1[0].replace("사과", "딸기", -1)
string1=[x]
print(string1)

#207
hello="have a nice day"
print(hello)

list1=hello.split(" ")
print(list1)
print(type(list1))

for i in range(0,len(list1)) :
    print("list1[%d] : %s" %(i,list1[i]))     

#a,b,c,d,e,f 나누어 출력하기
list2='a,b,c,d,e,f'
print(list2)
listResult=list2.split(',')
print(listResult)                  


#나누세요
#출력형식 list2[0] = ['홍길동:100:20']
list3=['홍길동:100:20','이순신:90:80','최수연:100:75']

list22=[]
for i in list3 :
    list10=i.split(":")
    print(list10)
    for j in list10 :
        list22.append(j)
print(list22)                     

#나누세요
list5=['kbs-사장-200, mbc-부장-100', 'kbs-사원-50, sbs-대리-80']
list = []
list5 = ['kbs-사장-200,mbc-부장-100','kbs-사원-50,sbs-대리-80']
for i in list5 :
    list_5 = i.split('-')
    print(list_5)
    for j in list_5 :
        list__6 = j.split(',')
        print(list__6)
        for k in list__6 :
            list.append(k)
print('완성==>%s' %list)



#-------------------------------
#데이터를 사이트에서 검색해 오기

import requests as req
url = "http://search.naver.com/search.naver"
rData=req.get(url,params={ 'query' : '백일해 증상'})
print(rData.text)                                              

#208
names = ["황예린", "홍지수", "안지영"]
print(names)

x="/".join(names)
print(x)                                   

#212 2차원 리스트
list2D = [ [1,2], [3,4,5], [3,4,5], [1]]
print(list2D[1][1]) #4
print(list2D[0][1]) #2

list2DD = [ [1,2,3,4], [5,6,7] ]
print(list2DD[1][2]) #7

print(list2DD[0][0], end=" ") #1~7
print(list2DD[0][1], end=" ") #1~7
print(list2DD[0][2], end=" ") #1~7
print(list2DD[0][3], end=" ") #1~7
print()
print(list2DD[1][0], end=" ") #1~7
print(list2DD[1][1], end=" ") #1~7
print(list2DD[1][2], end=" ") #1~7

print(len(list2DD)) #2
print(len(list2DD[0])) #4
print(len(list2DD[1])) #3

for i in range(0,len(list2DD)) :
        for j in range(0,len(list2DD[i])) :
             print(list2DD[i][j], end=" " )
        print() 


list3D = [ [[1,2,3],[4,5]], [[6,7],[8]] ]
#8을 출력
print(list3D[1][1][0])
#1을 출력
print(list3D[0][0][0]) 

#218p~222p 문제 풀기
#218
questions=["s_hool", "compu_er", "deco_ation", "windo_", "hi_tory"]
answers=["c", "t", "r", "w", "s"]

for i in range(0,len(questions)) :
    q = "%s : 밑 줄에 들어갈 알파벳은?  " %(questions[i])
    quess=input(q)
    if quess == answers[i] :
        print("정답!")
    else :
        print("틀렸어요!")             

#219
scores=[]
while True :
    x=int(input("성적을 입력하세요(종료시 -1 입력) : "))
    if x==-1 :
        break
    else :
        scores.append(x)

sum=x
for score in scores :
    sum=sum+score

avg=sum/len(scores)
print("합계:%d, 평균:%.2f" %(sum, avg)) 

#220
s=[64,89,100,85,77,58,79,67,96,87,87,36,85,98,84,76,63,69,53,22]

soo=0 #90~100점
woo=0 #80~89점
mi=0 #70~79점
yang=0 #60~69점
ga=0 #0~59점

i=0
while i<len(s) :
    if 90<=s[i]<=100:
        soo=soo+1
    if 80<=s[i]<=89:
        woo=woo+1
    if 70<=s[i]<=79:
        mi=mi+1
    if 60<=s[i]<=69:
        yang=yang+1
    if 0<=s[i]<=59:
        ga=ga+1
    i=i+1
print("수: %d명" %soo)
print("우: %d명" %woo)
print("미: %d명" %mi)
print("양: %d명" %yang)
print("가: %d명" %ga)

#222
seats=[[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [1,1,1,0,0,0,0,0,1,0], [0,0,0,0,0,1,0,0,0,0], [0,1,0,0,0,1,0,1,0,0], [0,0,0,0,0,0,1,0,0,0], [1,0,1,0,0,0,0,0,0,1]]
for i in range(0,len(seats)) :
    for j in range(len(seats[i])) :
        if seats[i][j] == 0 :
            print("%3s" %'□', end=" ")
        else :
            print("%3s" %'■', end=" ")
    print()
