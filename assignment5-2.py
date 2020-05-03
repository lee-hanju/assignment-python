import random

a = input('가위/바위/보 : ')

if a== '가위':
    a = 1
elif a =='바위' :
    a=2
elif a== '보':
    a =3

b = random.randint(1,3)

if b == 1:
    b='가위'
if b==2:
    b='바위'
if b==3:
    b='보'

print('컴퓨터 :',b)

if b =='가위':
    b=1
if b =='바위':
    b=2
if b=='보':
    b=3

if a+1==b or a-2==b:
    print('패배')
elif a-1==b or a+2 == b:
    print('승리')
else:
    print('무승부')
