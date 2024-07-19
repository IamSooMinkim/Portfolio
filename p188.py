# nameList = ['a', 'b']
# noList=list(range(241001,241020))
# print(noList)
# print(nameList[1])
# for i in noList : 
#     print(i, end=" ")

# i=0   #len=20개
# while i < len(noList) :
#     print(noList[i], end=" ")
#     i=i+1

'''
nameList = ['이순신', '홍길동', '박수연']
#박수연을 박수현으로 바꾸기
nameList[2] = '박수현'
for i in nameList :
    print(i, end=" ")

print()
#정현희를 추가하기
nameList.append('정현희')
for i in nameList :
    print(i, end=" ")

print()
#'이순신 홍길동 박수현 정현희 --> 이순신 이승후 홍길동 박수현 정현희' 로 바꾸기('이승후' 삽입)
nameList.insert(1, '이승후')
for i in nameList :
    print(i, end=" ")

print()
'이순신 이승후 홍길동 박수현 정현희' 리스트에서 '박수현'이 몇 번째 인덱스에 있나?
j=input("찾고 싶은 학생을 입력하세요 : ")
try : 
    nameList2 = ['박수현', '이순신', '이승후', '홍길동', '정현희']
    searchIndex=nameList2.index('박수현',0,10)
    print(searchIndex)
    searchIndex=nameList2.index(j,0,10)
    print(searchIndex)
except ValueError :
    print("%s은 리스트에 없습니다." %j)

print("-"*50)

member=[1,2,3,4]
member.remove(2)
print(member)

member2=[1,2,3,4,2,2,2,2]
member2.pop(2)
print(member2)
member.clear()
print(member)


#199
p1=[1,3,5]
p2=[2,4,6]
p3=p1+p2
print(p3)

#200
p4=list(range(1,11))
print(p4)
p4Sum=sum(p4)
print(p4Sum)
# sum=0
# for i in p4 :
#     sum=sum+i
# print(sum)

p5=[100,8,90]
p5Sum=sum(p5)
print(p5Sum)

p5=list(range(100,8,90))
p5Sum=sum(p5)
print(p5Sum)
# p5Avg=p5Sum/len(p5)
# print(p5Avg)
# p5Max=max(p5)
# print(p5Max)
'''

p5.reverse()
print(p5)

p6=['apple', 'banana', 'orange']
print(p6, '1번째')
p6Copy=p6.copy()                  #깊은 복사가 된다. 별도의 메모리로 복사한다.
print(p6Copy, '2번째')

#p6의 리스트에서 apple 삭제하기
p6.remove('apple')
print(p6, '1번째')
print(p6Copy, '2번째')

# p6Copy의 리스트에서 'orange'를 'manggo'로 바꾸기
p6Copy[2]='manggo'
print(p6, '3번째')
print(p6Copy, '3번째')

print('-'*70)

p7=['apple', 'banana', 'orange']
p77 = p7        #얕은 복사:p7의 주소가 p77로 복사된다. p7이나 p77을 변경하면 같이 변경됨
print(p7)
print(p77)

print('-'*70)
#문제1) p7에 있는 apple 삭제하기
p7.remove('apple')
print(p7)
print(p77)
#문제2) p77에 있는 'orange'를 'mango'로 변경하기
p77[1]='mango'
print(p7)
print(p77,'변경')
#문제3)p7에 'bear' 추가하기
p7.append('bear')
print(p7)
print(p77)

