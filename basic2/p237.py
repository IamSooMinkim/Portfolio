#딕셔너리
member= {'name':'황예린', 'age':22, 'email':'yerin@hanmail.net', 'age':30}
print(member['name'])
print(member['age'])
print(member['email'])

score=dict([("국어", 80), ("영어", 90), ("수학", 100)])
score2=dict([["국어", 80], ["영어", 90], ["수학", 100]])
print(score)
print(score2)
print(score["국어"])
print(score2['수학'])
score["국어"] = 90
score2["국어"] = 90
print(score, "**")
print(score2,"===")

user={"id":'kim55', 'name':'강성준', 'lever':7, 'point':10000}
print(user)
print(user["id"])
print(user["name"])
print(user["point"])

scores = {'kor':90, 'eng':89, 'math':98}
print(scores)

scores["music"] = 100
print(scores)

words={"door":"문", "chair":"의자", "table": "책상", "house":"집"}
print(words)

words["table"]="테이블"
print(words)

words["house"]="하우스"
print(words)

car={"brand":"현대", "model":"아반떼", "start":1990, "year":2021}
print(car)

x=car.pop("start")
print(x)

print(car)

car2={"brand":"현대", "model":"아반떼", "start":1990, "year":2021}
print(car2)

car2.clear()
print(car2)

area_code={"서울":"02", '부산':'051', '대구':'053', '광주':'062'}
for key in area_code:
    print("%s 지역번호 : %s" %(key, area_code[key]))

#C6-2
scores={'김채린':85, '박수정':98, '함소희':94, '안예린':90, '연수진':93}
sum=0
for key in scores :
    sum=sum+scores[key]

    print("%s:%d" %(key,scores[key]))

avg=sum/len(scores)
print("합계 :%d, 평균: %.2f" %(sum,avg))

#C6-3
admin_info={'아이디':'admin', '비밀번호':'12345'}
input_id=input("아이디를 입력하세요 : ")
input_pw=input("비밀번호를 입력하세요 : ")

if input_id==admin_info['아이디'] and input_pw==admin_info['비밀번호'] :
    print("정보에 접근 권한이 있습니다!")
else :
    print("정보에 접근 권한이 없습니다!")

#C6-4
words={'꽃':'flower', '나비':'butterfly', '학교':'school', '자동차':'car', '비행기':'airplane'}
    
print("<영어 단어 맞추기 퀴즈")

for kor in words :
    input_word=input('"%s"에 해당되는 영어 단어를 입력해주세요: ' %kor)
    if input_word==words[kor] :
        print("정답입니다!")
    else :
        print("틀렸습니다!")