Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle

bd = int(input("정수="))
bd_n1 =  bd // 1000
bd_n2 = (bd - (bd_n1 * 1000)) // 100 
bd_n3 = (bd - ((bd_n1 * 1000) + (bd_n2 * 100))) // 10
bd_n4 = bd % 10

print(bd_n1 + bd_n2 + bd_n3 +bd_n4)

n = input("반지름 값을 입력해주세요 : ")
t = turtle.Pen()
t.left(90)
t.forward(n/2)
t.circle(n/2)
t.forward(n/2)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)