'''
animals=("토끼", "거북이", "사자", "여우")
print(animals)

numbers=tuple(range(10))
print(numbers)

#출력하기
print(animals[1]) #거북이
print(numbers[3]) #3

#수정하기
# animals[2]= '호랑이' 수정 불가능

#튜플 병합하기
anNu = animals + numbers
print(anNu)

#튜플 요소 추출하기
n=tuple(range(10,21))
print(n)

print("n[0]=", n[0])
print("n[2:5]=", n[2:5])
print("n[2:]=", n[2:])
print("n[:5]=", n[:5])
print("n[-2]=", n[-2])
print("n[::1]=", n[::1])

tup1=(10,20,30,40,50,60)
for i in range(len(tup1)) :
    print(tup1[i])

#튜플에 관리자 정보 저장
admin_info= ("admin", "12345", "webmaster@naver.com")
print("관리자 정보")
print('아이디:'+admin_info[0])
print('비밀번호:'+admin_info[1])
print('이메일:'+admin_info[2])

#for 문
s=0
n2 = tuple(range(101))
for i in n2 :
    s += i
print(s)
print(sum(n2))                       '''

print("구구단표")
print("="*30)

dans=(2,3,4,5,6,7,8,9)
for dan in dans :
    print(str(dan)+'단')
    for i in range(1,10) :
        print("%dx%d=%d" %(dan, i , dan*i))