'''---------------------
성적관리 프로그램
---------------------

1. 학생 이름 삽입하기
   이름? 
2. 성적 입력하기
    누구의 성적 입력하래요? 홍길동
    국어점수 ?
    영어점수 ?
    수학점수 ?
3. 통계자료 보기
   1) 반 전체 통계
   2) 학생 통계 
4. 학생 자료 삭제하기
   삭제하려는 학생이름 ? 
5. 프로그램 종료하기 

==> 메뉴를 선택하세요(1/2/3/4/5)'''

name=[]
kor=[]
eng=[]
mat=[]
menu='1'
while menu != '5' :
    print('---------------------')
    print('성적관리 프로그램')
    print('---------------------')
    print('1. 학생 이름 삽입하기')
    print('2. 성적 입력하기')
    print('3. 통계자료 보기')
    print('4. 학생 자료 삭제하기')
    print('5. 프로그램 종료하기 ')
    menu=input("==> 메뉴를 선택하세요(1/2/3/4/5)")
    if menu=='1' :
        n=input("1. 학생 이름은? ")
        name.append(n)
        print(name)
    elif menu=='2' :
        try : 
            k=int(input("국어점수는? "))
            e=int(input("영어점수는? "))
            m=int(input("수학점수는? "))
            kor.append(k)
            eng.append(e)
            mat.append(m)
            print(kor, eng, mat)
        except ValueError :
            print ("점수는 숫자로 입력해주셔야 합니다")
    elif menu=='3' :
        print("1) 반 성적 검색")
        print("2) 개인 점수 검색")
        stMenu=input('번호를 선택하세요 (1/2) :  ')
        if stMenu=='1' :
            print()
            print('---------------------')
            print('이름   국어 영어 수학')
            print('---------------------')
            for i in range(len(name)) :
                print("%s  %d    %d    %d" %(name[i], kor[i], eng[i], mat[i]))
        elif stMenu=='2' :
            sName=input('점수를 알고 싶은 학생 이름은?  ')
            try :
                sIndex=name.index(sName)
                print("%s   %d   %d   %d"%(name[sIndex], kor[sIndex], eng[sIndex], mat[sIndex]))
            except ValueError :
                print("%s는 우리 반 학생이 아닙니다." %sName)
    elif menu=='4' :
        delName=input("삭제하려는 학생의 이름은?  ")
        try :
            sIndex = name.index(delName)
            name.pop(sIndex)
            kor.pop(sIndex)
            eng.pop(sIndex)
            mat.pop(sIndex)
        except ValueError :
            print("%s는 우리 반 학생이 아닙니다." %delName)
    elif menu=='5' :
        #5. 프로그램 종료하기
        break

'''검색 프로그램
sName=input('점수를 알고 싶은 학생 이름은?' )
        okName = -999
        for i in range(len(name)) :
            if sName == name[i] :
                okName = i
                break
        if okName == -999 :
            print("%s는 우리 반 학생이 아닙니다." %sName)
        else :
            print("%s   %d   %d   %d"%(name[okName], kor[okName], eng[okName], mat[okName]))'''