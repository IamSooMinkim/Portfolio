#문제1
a, b = 5, 7
result=a*b
print( result )

#문제2
portion = 12345 // 789
the_rest = 12345 % 789
print ( '몫: ', portion, '나머지: ', the_rest )

#문제3
#x,y에 각각 11, 22를 할당하고, z를 사용하여 x 값과 y 값을 바꾸시오
x, y = 11, 22
z = x
x = y
y = z
print( "x=", x , "y=", y )

#3-1 파이썬에서 변수 값 교환하기
x, y = 100, 200
x, y = y, x 
print( "x=", x , "y=", y )

#문제4
r=7 #반지름
#원넓이구하는 공식: 반지름*반지름*3.14
area = r*r*3.14
print( r, '의 반지름의 원넓이는 ', area )
