from random import*
import turtle

# 1번 문제

a = int(input("a 입력: "))
b = int(input("b 입력: "))

if a>b :
    print("a가 b보다", a-b,"만큼 더 크다")


elif b>a :
    print("b가 a보다", b-a,"만큼 더 크다")

else :
    print("a와 b는 같다")

# 2번 문제

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

# 3번 문제

t = turtle.Turtle()
t.shape('classic')
n1 = int(turtle.textinput('입력창', '변1: '))
n2 = int(turtle.textinput('입력창', '변2: '))
n3 = int(turtle.textinput('입력창', '변3: '))


if (n3*n3) == (n2*n2) + (n1 * n1):
    t.forward(n1*100)
    t.left(90)
    t.forward(n2*100)
    t.home()
else:
    t.write('직각삼각형이 아님.', font=("Arial",10))
