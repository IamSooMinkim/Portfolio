
phone1 = '82-02-123-4567'  
#집
phone2 = '82-10-8744-3334' 
#핸드폰
if len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 핸드폰번호입니다.')
elif len(phone1)==15 and len(phone2)==14 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 집번호입니다.')
elif len(phone1)==14 and len(phone2)==15 :
    print('phone1은 집번호입니다.')
    print('phone2는 핸드폰번호입니다.')
elif len(phone1)==14 and len(phone2)==14 :
    print('phone1은 집번호입니다.')
    print('phone2는 집번호입니다.')