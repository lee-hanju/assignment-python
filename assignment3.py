Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2��

import turtle

t = turtle.Turtle()

t.shape('classic')



s = turtle.textinput('�Է�â', '�׸� ��: ')

t.color(s)



t.penup()

t.goto(31,73)

t.write('Stop', font=("Arial",15,"bold"))

t.home()

t.pendown()

t.forward(100)

t.left(60)

t.forward(100)

t.left(60)

t.forward(100)

t.left(60)

t.forward(100)

t.left(60)

t.forward(100)

t.left(60)

t.forward(100)

t.left(60)



#1��

name1 = input('�̸� ù°�ڴ� : ')

name2 = input('�̸� ��°�ڴ� : ')

name3 = input('�̸� ��°�ڴ� : ')

print('*' * len(name1 + name2 + name3))

print(chr(ord(name2[0])+32) + chr(ord(name3[0])+32) + chr(ord(name1[0])+32) + name1[1:])